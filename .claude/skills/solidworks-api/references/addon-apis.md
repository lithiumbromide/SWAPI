# Add-on APIs
Entry objects, interop assemblies, data modules and traps for the SOLIDWORKS add-on APIs outside `sldworksapi`; look members up with `swapi.py find QUERY --module MODULE` before writing any call.
## Contents
- [Common access pattern](#common-access-pattern)
- [DimXpert](#dimxpert)
- [Costing](#costing)
- [Routing](#routing)
- [Motion Study](#motion-study)
- [Toolbox](#toolbox)
- [eDrawings](#edrawings)
- [Utilities](#utilities)
- [Sustainability](#sustainability)
- [3D Printer](#3d-printer)
- [Inspection](#inspection)
- [Design Checker](#design-checker)
- [FeatureWorks](#featureworks)
- [Scan to 3D](#scan-to-3d)
- [HTML Control](#html-control)
- [Visualize](#visualize)
- [Commands](#commands)
## Common access pattern
- Three access styles exist: a document accessor (`IModelDocExtension.GetCostingManager`, `IModelDocExtension.GetSustainability`, `IModelDocExtension.GetMotionStudyManager`, `IModelDocExtension.DimXpertManager`, `IModelDocExtension.GetScanto3D`, `IAssemblyDoc.GetRouteManager`); an add-in object from `ISldWorks.GetAddInObject` (Utilities, Design Checker, FeatureWorks, Inspection, Toolbox Browser, Simulation); or an interface that your code implements or hosts (3D Printer, HTML Control, Toolbox Configurator, eDrawings ActiveX control).
- Load the add-in before asking for its object, because `ISldWorks.GetAddInObject` returns nothing for an add-in that is not loaded: tick it in Tools > Add-Ins or call `ISldWorks.LoadAddIn` with the add-in DLL path and treat both `swSuccess` and `swAddinAlreadyLoaded` of `swLoadAddinError_e` as success.
- Pass a GUID to `ISldWorks.GetAddInObject` in curly braces (`"{GUID}"`), because a bare GUID string is interpreted as a ProgID.
- Prefer version-specific ProgIDs where they exist (Simulation, Design Checker), because with several SOLIDWORKS installs the version-independent ProgID resolves to the latest install and fails with type mismatches from an older session; derive the major version from the first two digits of `ISldWorks.RevisionNumber`.
- Reference the add-on interop assembly from `install_dir\api\redist` the same way as the core interops, see [dotnet-addins.md](dotnet-addins.md); VBA references the matching type library instead.
- Check every entry object for null, because accessors return nothing when the product is not licensed (Costing, Sustainability need Professional or Premium); see [null checks](correctness-rules.md#null-checks-and-return-values).
- Simulation (`cworksapi`) has its own reference: [simulation.md](simulation.md).
## DimXpert
- Entry: `IDimXpertManager` (in `sldworksapi`) for a configuration, then `IDimXpertManager.DimXpertPart` returns `IDimXpertPart` from the DimXpert module.
- Obtain: `IModelDocExtension.DimXpertManager` (configuration name, create-schema flag) or `IConfiguration.DimXpertManager`; selected DimXpert items come back from `ISelectionMgr.GetSelectedObject6` as `IDimXpertManager` or `IFeature`.
- Interop: `SolidWorks.Interop.swdimxpert`; the examples reference `install_dir\api\redist\swdimxpert.dll`. Module: `swdimxpertapi`.
- In C# the parameterized property is called as `get_DimXpertManager(configName, true)`, because C# cannot index COM properties with arguments.
- Iterate with `IDimXpertPart.GetFeatures` and `IDimXpertPart.GetAnnotations`; auto-dimensioning starts from `IDimXpertPart.GetAutoDimSchemeOption`.
- DimXpert data can also be read without SOLIDWORKS through `ISwDMConfiguration12.DimXpertPart` ([document-manager.md](document-manager.md)); that path returns CAD identifiers only for parts saved in a current release, so open and resave older parts first.
## Costing
- Entry: `ICostManager`; chain `ICostManager.CostingModel` to `ICostPart`, then `ICostBody`, `ICostAnalysis` and `ICostFeature`.
- Obtain: `IModelDocExtension.GetCostingManager` on an open part. Interop: `SolidWorks.Interop.sldcostingapi` (VBA: SldCostingAPI type library). Module: `swcostingapi`.
- Available only in SOLIDWORKS Professional and Premium; the manager is null when Costing is not licensed.
- Call `ICostManager.WaitForUIUpdate` right after getting the manager, as the examples do, because Costing updates its UI asynchronously; call `ICostManager.Close` when done.
- Template folders come from `ISldWorks.GetUserPreferenceStringValue` with `swFileLocationsCostingTemplates` and `swFileLocationsCostingReportTemplateFolder`; restore any you change, see [user preferences](correctness-rules.md#user-preferences).
## Routing
- Entry: `IRouteManager` (routes, cables, wires, from-to lists, flattened routes).
- Obtain: `IAssemblyDoc.GetRouteManager` on the top-level assembly that contains the route subassembly. Interop: `SolidWorks.Interop.SWRoutingLib` (`SWRoutingLib.tlb` for VBA). Module: `routingapi`.
- Load the Routing add-in first; the examples call `ISldWorks.LoadAddIn` with `ISldWorks.GetExecutablePath` plus `\sldrtadd.dll`.
- Start from `IRouteManager.GetRouteProperty` or `IRouteManager.ImportFromToList`, and look up the rest with `swapi.py members IRouteManager`.
## Motion Study
- Entry: `IMotionStudyManager`, then `IMotionStudy` from `IMotionStudyManager.GetMotionStudy` or `IMotionStudyManager.CreateMotionStudy`.
- Obtain: `IModelDocExtension.GetMotionStudyManager`. Interop: `SolidWorks.Interop.swmotionstudy`. Module: `swmotionstudyapi`.
- The manager also returns Simulation studies, so check `IMotionStudy.StudyType` against `swMotionStudyType_e` before using motion members.
- `IMotionStudy.Calculate` works only on the active study (`IMotionStudy.IsActive`, `IMotionStudy.Activate`).
- Motion Analysis studies (`swMotionStudyTypeCosmosMotion`) need the SOLIDWORKS Motion add-in loaded and a Premium licence; Animation studies return no results.
## Toolbox
- Purpose: lets a third-party PDM control Toolbox part files; it does not insert fasteners (insert Toolbox parts as ordinary components, see [assemblies.md](assemblies.md)).
- Browser entry: `IApplication`, then `IApplication.PDMDocManager` returns `IPDMDocManager`, whose events gate copying, writing and deleting Toolbox documents. Interop: `SolidWorks.Interop.swbrowser`.
- Obtain the browser from an add-in's `ISwAddin.ConnectToSW` with `ISldWorks.GetAddInObject("{ED783340-D5DB-11d4-BD5A-00C04F019809}")` and cast to `IApplication`.
- Configurator: implement `IToolboxConfiguratorAddin` in a class with its own GUID; its Connect receives `IToolBoxConfiguratorApplication`. Interop: `SolidWorks.Interop.sldtoolboxconfigureaddin`. Debug by attaching to `SldToolboxConfigure.exe`.
- On drag and drop the PDM handler answers the FileDropPreNotify event with `IAssemblyDoc.SetDroppedFileName`. Module for both: `toolboxapi`.
## eDrawings
- Entry: `IEModelViewControl` (viewer ActiveX control) and `IEModelMarkupControl`; this API drives the eDrawings viewer, not SOLIDWORKS. Interop namespaces: `eDrawings.Interop.EModelViewControl`, `eDrawings.Interop.EModelMarkupControl`. Module: `emodelapi`.
- Host the control in a Windows Forms application built for x64; Getting Started generates the 64-bit interop with `tlbimp.exe` from `EModelView.dll` because Visual Studio itself is 32-bit.
- `IEModelViewControl.OpenDoc` returns before loading finishes; wait for the OnFinishedLoadingDocument event before touching the model, otherwise the host can hang or crash. Pass `""` (not null) as its command string.
- The legacy `emodeltoolkit` module documents a C++ (non-COM) library that writes `.eprt`, `.easm` and `.edrw` files; use it only for existing C++ code.
## Utilities
- Entry: `IUtilities`, then `IUtilities.GetToolInterface` with a `gtSwTools_e` value (compare documents, features or geometry, geometry and thickness analysis, power select, feature paint, find and replace annotations) and an error out parameter.
- Obtain: `ISldWorks.GetAddInObject("Utilities.UtilitiesApp")` (version-independent ProgID only). Interop: `SolidWorks.Interop.gtswutilities`. Module: `swutilitiesapi`.
- Open the documents to compare before getting the tool, and set angular or position tolerances before comparing faces.
## Sustainability
- Entry: `ISustainabilityApp`; impact factors come from `ISustainabilityApp.GetSustainabilityMaterial`, `ISustainabilityApp.GetSustainabilityManufacturing`, `ISustainabilityApp.GetSustainabilityTransportation`, `ISustainabilityApp.GetSustainabilityEndOfLife` and the part or assembly use/process getters; results from `ISustainabilityApp.GetSustainabilityEnvironmentalImpact`.
- Obtain: `IModelDocExtension.GetSustainability` on an open part or assembly. Interop: `SolidWorks.Interop.sustainability`. Module: `sustainabilityapi`. Professional or Premium only.
- Call `ISustainabilityEnvironmentalImpact.UpdateResults` before reading carbon, energy, air or water results or saving a report, because the getters otherwise return stale values; set `ISustainabilityEnvironmentalImpact.DurationOfUse` first.
## 3D Printer
- Entry: `ISw3DPrinter`, which a printer vendor implements; SOLIDWORKS calls `ISw3DPrinter.OnStartup` when the user picks the vendor's printer in the Print3D dialog and `ISw3DPrinter.OnOk` or `ISw3DPrinter.OnCancel` when the dialog closes.
- Interop: `SolidWorks.Interop.sw3dprinter`. Module: `sw3dprinterapi`. Not a client API: do not try to obtain it from `ISldWorks`.
## Inspection
- Entry: `IInspectionAddinMgr`; create `IInspectionProjectData` with `IInspectionAddinMgr.CreateInspectionProjectData`, then a project with `IInspectionAddinMgr.CreateInspectionProject`, and export with `IInspectionProject.ExportToExcel` and its PDF and eDrawings siblings.
- Obtain: `ISldWorks.GetAddInObject("Inspection.ExtSwAddin")`. Interop: `SolidWorks.Interop.swinspectionAddIn`. Module: `swinspectionapi`.
- Needs SOLIDWORKS Professional or Premium 2022 or later plus a licensed SOLIDWORKS Inspection add-in that is active.
- Getting Started abbreviates the calls; the real signatures take a template path (`.swidot`, under `install_drive:\ProgramData\SOLIDWORKS\SolidWorks Inspection yyyy Addin\Templates`) and return an error out parameter, so check them with `swapi.py sig` before coding.
## Design Checker
- Entry: `ISWDesignCheck`; run checks with `ISWDesignCheck.RunDesignCheck5` (earlier `RunDesignCheck` variants are obsolete) and build standards with `ISWDesignCheck.CreateChecksFromSWFile`.
- Obtain: `ISldWorks.GetAddInObject("SWDesignChecker.SWDesignCheck")` or the version-specific `SWDesignChecker.SWDesignCheck.<year>`, where year is the major revision plus 1992. Interop: `SolidWorks.Interop.dsgnchk`. Module: `dsgnchkapi`.
- `ISWDesignCheck.RunDesignCheck5` returns a `dsgnchkError_e` code and a result summary of failure counts separated by `@` (Critical, High, Medium, Low; pre and post values when auto-correct is on); a Word report needs Microsoft Word installed, otherwise XML is written.
## FeatureWorks
- Entry: `IFeatureWorksApp`; recognize with `IFeatureWorksApp.RecognizeFeatureAutomatic` (bitmask of `fwAutomaticRecognitionOptions_e`) or `IFeatureWorksApp.RecognizeFeatureInteractive`, then build with `IFeatureWorksApp.CreateFeatures`.
- Obtain: `ISldWorks.GetAddInObject("FeatureWorks.FeatureWorksApp")`. Interop: `SolidWorks.Interop.fworks`. Module: `fworksapi`. The FeatureWorks DLLs must be loaded first.
- Combining, re-recognizing, pattern recognition, local recognition and Recognize Similar are not supported through the API.
## Scan to 3D
- Entry: `IScanto3D`, read-only access to point-cloud mesh data: `IScanto3D.GetMeshCount`, then `IScanto3D.GetMeshDataCountAtIndex` and `IScanto3D.GetMeshDataAtIndex` per mesh feature.
- Obtain: `IModelDocExtension.GetScanto3D` with the Scanto3D add-in active. Interop: `SolidWorks.Interop.swscanto3d`. Module: `swscanto3dapi`.
## HTML Control
- Entry: `ISwHtmlInterface`, created inside each Quick Tips HTML page with `CreateObject("SwHtmlControl.SwHtmlInterface")`; it shows bubble tooltips (`ISwHtmlInterface.ShowBubbleTooltip`, `ISwHtmlInterface.ShowBubbleTooltipAt`) and flashes add-in toolbar buttons.
- The add-in side implements `ISwQuickTip` and registers it with `ISldWorks.InstallQuickTipGuide`, updates pages with `ISwQuickTip.AppState` plus `ISldWorks.RefreshQuickTipWindow`, and removes it with `ISldWorks.UnInstallQuickTipGuide`. Interop: `SolidWorks.Interop.swhtmlcontrol`. Module: `swhtmlcontrolapi`.
## Visualize
- Entry: `IVisualizeAddin2` (or `IVisualizeAddin`), then `IVisualizeAddin2.GetAddinManager2` returns `IVisualizeAddinManager2`; the add-in renders SOLIDWORKS models photorealistically through SOLIDWORKS Visualize and writes Visualize project files (`.svpj`).
- Obtain: `ISldWorks.GetAddInObject("SolidWorks.Visualize.Implementation.VisualizeAddin")` with the SOLIDWORKS Visualize add-in active and Visualize installed. Interop assembly and namespace: `SolidWorks.Visualize.Interfaces`. Modules: `swvisualizeapi` and `swvisualizeapiVB6`; members are marked `SOLIDWORKS Visualize Add-in API 2025 FCS` or `2026 FCS`, and the module first appears in the 2026 help.
- Configure `IVisualizeAddinManager2.RenderOptions` (`IRenderOptions.OutputFolder`, `IRenderOptions.JobName`, `IRenderOptions.ImageFormat` with `ImageFormat_e`, `IRenderOptions.Width`, `IRenderOptions.Height`, `IRenderOptions.FrameCount`, `IRenderOptions.DenoiserEnabled`), then call `IVisualizeAddinManager2.Render`, which blocks until the render finishes and can take long on weak hardware.
- Asynchronous renders: `IVisualizeAddinManager2.StartRender2` with your `IRenderNotificationHandler2` implementation; SOLIDWORKS calls `IRenderNotificationHandler2.SetCallbackHandler` once with an `IRenderCallbackHandler` for previews or cancellation. Export a project with `IVisualizeAddinManager2.SaveWithPartGrouping` (`PartGroupingMode_e`) and open Visualize with `IVisualizeAddinManager2.LaunchVisualize`.
- 2026 obsoleted `IVisualizeAddin.GetAddinManager`, `IVisualizeAddinManager.StartRender`, `IVisualizeAddinManager.Save` and `IRenderNotificationHandler` in favor of the `2` interfaces ([current members only](correctness-rules.md#current-members-only)); keep the old ones only for 2025 targets.
## Commands
- `swCommands_e` (module `swcommands`, interop `SolidWorks.Interop.swcommands`) lists about 2,190 toolbar and menu command IDs; run one with `ISldWorks.RunCommand` or `IModelDocExtension.RunCommand`, passing a PropertyManager title or `""`.
- Use it only when no dedicated API exists, because `ISldWorks.RunCommand` returns only whether the command started and many IDs are valid only in a document type or mode stated in the enum description (for example Edit Sheet Format in drawings); check `ISldWorks.IsCommandEnabled` first and `ISldWorks.GetRunningCommandInfo` afterwards.
- `swMouse_e` holds the flags for synthesized mouse input through `IModelView.GetMouse` and `IMouse.MoveXYZ`.
- Look up IDs by name with `swapi.py enum swCommands_e --grep TEXT`, and pass enum names, not numbers, see [enums](correctness-rules.md#enums-and-bitmasks).
## Sources
- `markdown/sldworksapiprogguide/Overview/Accessing_Add-ins.md`
- `markdown/sldworksapiprogguide/Overview/Quick_Tips_and_Bubble_ToolTips.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetAddInObject.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunCommand.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCostingManager.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSustainability.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMotionStudyManager.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DimXpertManager.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetRouteManager.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager.md`
- `markdown/sldworksapi/Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_CSharp.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLoadAddinError_e.md`
- `markdown/swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.md`
- `markdown/swdimxpertapi/Auto_Dimension_Scheme_Example_CSharp.md`
- `markdown/swdocmgrapi/Code_Example_CSharp.md`
- `markdown/swcostingapi/GettingStarted-swcostingapi.md`
- `markdown/swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager.md`
- `markdown/swcostingapi/Create_Machining_Costing_Analyses_Example_CSharp.md`
- `markdown/routingapi/GettingStarted-routingapi.md`
- `markdown/routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.md`
- `markdown/routingapi/Get_and_Set_Routing_Component_Properties_Example_CSharp.md`
- `markdown/swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager.md`
- `markdown/swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Calculate.md`
- `markdown/swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.swMotionStudyType_e.md`
- `markdown/toolboxapi/GettingStarted-toolboxapi.md`
- `markdown/emodelapi/GettingStarted-emodelapi.md`
- `markdown/emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenDoc.md`
- `markdown/emodeltoolkit/Introduction.md`
- `markdown/swutilitiesapi/GettingStarted-swutilitiesapi.md`
- `markdown/swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities~GetToolInterface.md`
- `markdown/swutilitiesapi/Compare_Documents_VB6.md`
- `markdown/sustainabilityapi/GettingStarted-sustainabilityapi.md`
- `markdown/sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~UpdateResults.md`
- `markdown/sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter_namespace.md`
- `markdown/swinspectionapi/Getting Started.md`
- `markdown/swinspectionapi/Release Notes.md`
- `markdown/dsgnchkapi/SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.ISWDesignCheck~RunDesignCheck5.md`
- `markdown/fworksapi/GettingStarted-fworksapi.md`
- `markdown/fworksapi/Recognizing_Features_Automatically.md`
- `markdown/swscanto3dapi/SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D.md`
- `markdown/swhtmlcontrolapi/SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface.md`
- `markdown/swcommands/SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swCommands_e.md`
- `markdown/swvisualizeapi/Welcome.md`
- `markdown/swvisualizeapi/GettingStarted.md`
- `markdown/swvisualizeapi/ReleaseNotes.md`
- `markdown/swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.md`
- `markdown/swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~StartRender2.md`
