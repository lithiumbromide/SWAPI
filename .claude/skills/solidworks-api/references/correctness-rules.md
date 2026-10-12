# Correctness rules
Single home of the SOLIDWORKS API correctness rules: each section names the failure it prevents, the rule, and the lookup that verifies it. Domain references link here instead of repeating these facts.
## Contents
- [Current members only](#current-members-only)
- [Version availability](#version-availability)
- [Enums and bitmasks](#enums-and-bitmasks)
- [Errors and warnings](#errors-and-warnings)
- [Units](#units)
- [Selection](#selection)
- [Null checks and return values](#null-checks-and-return-values)
- [Arrays and Variants](#arrays-and-variants)
- [Configurations](#configurations)
- [Lightweight and suppressed components](#lightweight-and-suppressed-components)
- [Active and visible documents](#active-and-visible-documents)
- [User preferences](#user-preferences)
- [VBA declarations](#vba-declarations)
- [COM object lifetime](#com-object-lifetime)
- [Batch performance](#batch-performance)
- [Persistent references](#persistent-references)
## Current members only
Failure: code calls an obsolete member that still compiles (obsolete members stay in the interop and type library, so nothing warns) but lacks newer options, or calls an invented suffix (`SaveAs4`, `SelectByID3`, `OpenDoc8`) that fails at compile time in C# and at run time in late-bound VBA.
Rule: take every member from `sig` or `find` output. When a row reads `OBSOLETE -> ... current X`, use X. Chains that unaided code gets wrong most often:
- `IModelDoc2.SaveAs3` -> `IModelDocExtension.SaveAs` -> `IModelDocExtension.SaveAs2` -> `IModelDocExtension.SaveAs3`
- `IModelDoc2.SelectByID` -> `IModelDocExtension.SelectByID2`
- `IModelDoc2.AddCustomInfo3`, `IModelDoc2.GetCustomInfoValue` -> `IModelDocExtension.CustomPropertyManager`; `ICustomPropertyManager.Get5` -> `Get6`, `Add2` -> `Add3`, `Set` -> `Set2`, `Delete` -> `Delete2`, `GetAll2` -> `GetAll3`
- `ISldWorks.ActivateDoc2` -> `ISldWorks.ActivateDoc3`; `ISldWorks.CreateTaskpaneView2` -> `ISldWorks.CreateTaskpaneView3`; `ISldWorks.SetAddinCallbackInfo` -> `ISldWorks.SetAddinCallbackInfo2`
- `ICommandManager.CreateCommandGroup` -> `CreateCommandGroup2`; `ICommandGroup.AddCommandItem` -> `AddCommandItem2`; `ICommandManager.RemoveCommandGroup` -> `RemoveCommandGroup2`
- `IComponent2.GetModelDoc` -> `GetModelDoc2`, `GetSuppression` -> `GetSuppression2`, `Name` -> `Name2`; `IConfiguration.GetRootComponent` -> `GetRootComponent3`
- `IModelDoc2.InsertSketch2` -> `ISketchManager.InsertSketch`; `IFeatureManager.FeatureExtrusion2` -> `FeatureExtrusion3`; `IAssemblyDoc.AddMate5` -> `IAssemblyDoc.CreateMate`
- `IDrawingDoc.AutoBalloon4` -> `AutoBalloon5`; `IView.InsertBomTable4` -> `InsertBomTable5` -> `InsertBomTable6`; `ITableAnnotation.Text` -> `Text2`

Verify: `swapi.py check FILE` flags obsolete and near-miss names; `swapi.py members IModelDocExtension --obsolete` lists what to avoid on one interface.
## Version availability
Failure: the newest member compiles against the newest interop but fails on the user's older install (C#: missing method at run time; VBA: error 438 "Object doesn't support this property or method").
Rule: the `since` value must not exceed the target release. If it does, walk back the obsolete chain to the newest member whose `since` fits. Example: `IView.InsertBomTable6` is 2025, `InsertBomTable5` is 2024, `InsertBomTable4` is 2013, so an add-in that must run on 2023 calls `InsertBomTable4` and states why. An empty `since` means the help lists no availability (old member); treat it as available. Revision numbers, interop versions and release-note lookups are in [versions.md](versions.md).
Verify: `swapi.py check FILE --target 2023`; `swapi.py sig IView.InsertBomTable6`.
## Enums and bitmasks
Failure: bare numbers that are wrong for the parameter, change meaning between enums, or hide intent.
Rule: pass swconst member names. `sig` annotates each enum-typed parameter after a colon (`int Options:swSaveAsOptions_e`); look the enum up instead of guessing. C# casts the member to `int` (`(int)swSaveAsOptions_e.swSaveAsOptions_Silent`); VBA uses the bare member name (`swSaveAsOptions_Silent`), which resolves only when the Constant type library is referenced. Combine flags of bitmask enums (`swSaveAsOptions_e`, `swOpenDocOptions_e`) with `Or` or `|`; adding values works only while each flag appears once. Decode returned bitmasks (`swFileLoadError_e`, `swFileSaveError_e`, `swActivateDocError_e`) with `And` or `&` per flag. Some enums carry no numeric values in the help (`swUserPreferenceToggle_e`, `swUserPreferenceIntegerValue_e`); always use their names.
Verify: `swapi.py enum swSaveAsOptions_e`; reverse lookup `swapi.py enum swStepAP`.
## Errors and warnings
Failure: a call returns False or Nothing and the code continues blind, or a successful save hides warnings.
Rule: declare, pass and inspect every Errors and Warnings parameter, and every result code:
- `ISldWorks.OpenDoc6`: `swFileLoadError_e` and `swFileLoadWarning_e`; an assembly can open and still report `swFileNotFoundError` for a missing component. After `ISldWorks.OpenDoc7`, read `IDocumentSpecification.Error` and `IDocumentSpecification.Warning`.
- `IModelDocExtension.SaveAs3` and `IModelDoc2.Save3`: `swFileSaveError_e` and `swFileSaveWarning_e`; the Boolean return is False only for errors, warnings arrive with True.
- `ISldWorks.ActivateDoc3`: `swActivateDocError_e`; `ICommandManager.CreateCommandGroup2`: `swCreateCommandGroupErrors`; `ISldWorks.RunMacro2`: `swRunMacroError_e`.
- `ICustomPropertyManager` returns result codes (`swCustomInfoGetResult_e`, `swCustomInfoAddResult_e`, `swCustomInfoSetResult_e`, `swCustomInfoDeleteResult_e`); `Add3` reports a type mismatch instead of throwing.

VBA declares them `Long` and passes them ByRef. The help prints C# by-reference parameters as `out`, but the interop declares many of them `ref` (the shipped C# examples pass `ref errors, ref warnings` to `OpenDoc6`, `SaveAs`, `Save3`, `ActivateDoc3` and `CreateCommandGroup2`, and `out` to `Get6`); initialize to 0 and use the keyword the compiler demands. Report decoded enum names, not raw integers.
Verify: `swapi.py enum swFileSaveError_e`; `swapi.py doc ISldWorks.OpenDoc6`.
## Units
Failure: millimeters or degrees passed where the API expects meters or radians, producing parts 1000 times too large or wrong angles without any error.
Rule: unless a member says otherwise, the API takes and returns meters, radians, kilograms, square meters and cubic meters. Convert once at the boundary (`mm / 1000`, `deg * PI / 180`). Document unit settings only change display: `IModelDoc2.GetUserUnit` returns an `IUserUnit` whose properties are read-only, and units are changed through `IModelDocExtension.SetUserPreferenceInteger`. Read the parameter text for exceptions: `IDimension.SetSystemValue3` takes meters while `IDimension.SetValue3` takes the owning document's units; drawing view locations (`IDrawingDoc.CreateDrawViewFromModelView3`) are sheet meters; Simulation methods take an explicit unit argument ([simulation.md](simulation.md)).
Verify: `swapi.py doc IDimension.SetSystemValue3`.
## Selection
Failure: `IModelDocExtension.SelectByID2` returns False, or selects the wrong entity after the view changes.
Rule:
- When you already hold the object, select it directly: `IEntity.Select4` with an `ISelectData` from `ISelectionMgr.CreateSelectData`, `IFeature.Select2`, `IComponent2.Select4`, or `ISelectionMgr.AddSelectionListObject` to add without preselecting in the UI. Keep `SelectByID2` for name-only cases; it is also the method that behaves correctly while a PropertyManager page or command is running.
- Type is the uppercase string from the `swSelectType_e` table (`seltype`): `PLANE`, `FACE`, `EDGE`, `COMPONENT`, `DIMENSION`, `BODYFEATURE`, `SKETCH`, `DRAWINGVIEW`. A point in the active sketch is `SKETCHPOINT`, otherwise `EXTSKETCHPOINT`. A wrong type makes the call return False.
- Name is exact and case-sensitive. In an assembly qualify it with the component path (`Plane4@Part1-1@Assem1`); qualify dimensions with the document (`D1@Sketch2@Part1.SLDPRT`). Default plane names depend on the template and UI language, so traverse to the feature and call `IFeature.GetNameForSelection` (returns the name and type `SelectByID2` expects; `IFeature.Name` does not), or `IComponent2.GetSelectByIDString` for components.
- The calling `IModelDoc2` must be open and visible. The document returned by `IComponent2.GetModelDoc2` usually is not; select through the assembly with the qualified name.
- Pass X, Y, Z as 0 for named items. Coordinates are model space and view dependent; for faces and edges prefer `IEntity.Select4` or `IModelDocExtension.SelectByRay`.
- Append False clears the list first; call `IModelDoc2.ClearSelection2(True)` before building a new set. Ordered selections use Mark: 2 for loft guide curves, 4 for sweep paths; sweeps take the profile with 1, guide curves with 2 and a direction vector with 128.
- Read back with `ISelectionMgr.GetSelectedObject6(index, -1)` (index starts at 1) and `ISelectionMgr.GetSelectedObjectType3`. The returned interface depends on the type: planes and sketches come back as `IFeature`, dimensions as `IDisplayDimension`, components in a drawing as `IDrawingComponent`.
- A leftover selection changes other calls: `IModelDocExtension.SaveAs3` exports only the selected faces or bodies, so clear the selection before exporting.

Verify: `swapi.py seltype PLANE`; `swapi.py doc IModelDocExtension.SelectByID2`.
## Null checks and return values
Failure: a null object propagates and fails later with an unrelated message (VBA error 91, `NullReferenceException`).
Rule: test every returned object and array before use and stop with a message that names the reason. Common nulls: `ISldWorks.ActiveDoc` with no open document; `ISldWorks.OpenDoc6` on failure; `IComponent2.GetModelDoc2` for suppressed or lightweight components; `IConfiguration.GetRootComponent3(False)` for an inactive configuration; `IComponent2.GetChildren` on a part; `IFeature.GetDefinition` for unsupported feature types; `ISelectionMgr.GetSelectedObject6` for unsupported types. VBA returns Empty or Null Variants; test with `IsEmpty` and `IsNull`. Boolean results must be checked too: `IModelDoc2.ShowConfiguration2`, `SelectByID2`. `IFeature.ModifyDefinition` can return True and still leave a rebuild error, so read `IFeature.GetErrorCode2` afterwards. In C++ an S_OK HRESULT only means the call was dispatched; check the output value.
Verify: `swapi.py doc` on each getter and read the Return Value and Remarks.
## Arrays and Variants
Failure: type mismatch on array arguments, or a call that silently does nothing because the array element size is wrong.
Rule:
- VBA: receive arrays in a `Variant`, test `IsEmpty`, loop `LBound` to `UBound`. Pass input arrays by assigning a typed array (Long or Double, never Integer) to a Variant and passing that Variant.
- .NET: array returns are `object`; cast to `object[]` for interfaces, `string[]` for names (`IModelDoc2.GetConfigurationNames`, `IDrawingDoc.GetSheetNames`) and `double[]` for numeric data (`IMathTransform.ArrayData`).
- .NET input arrays of SOLIDWORKS interfaces must be wrapped in `System.Runtime.InteropServices.DispatchWrapper[]`; the help names `IAssemblyDoc.ReorderComponents`, `IExportPdfData.SetSheets`, `ILibraryFeatureData.SetReferences`, `ISheet.InsertTitleBlock` and `IView.Bodies`.

Verify: `swapi.py sig` shows `object` parameters; `swapi.py examples --symbol IExportPdfData.SetSheets --lang csharp`.
## Configurations
Failure: values are read from or written to whichever configuration happens to be active, and the user's active configuration is left changed.
Rule: record `IConfigurationManager.ActiveConfiguration` (`IConfiguration.Name`) first, iterate `IModelDoc2.GetConfigurationNames`, activate with `IModelDoc2.ShowConfiguration2` and check its result, rebuild with `IModelDoc2.EditRebuild3` when the target configuration needs it, and reactivate the original at the end. Read configuration-specific custom properties from `IModelDocExtension.CustomPropertyManager(configName)` or `IConfiguration.CustomPropertyManager`; an empty string addresses file-level properties. `ICustomPropertyManager.Get6` with UseCached False returns up-to-date values but may cycle configurations; rebuild with `IModelDoc2.ForceRebuild3` afterwards to restore the model. Assembly traversal, component bodies and transforms depend on the active configuration; suppression states across configurations come from `IConfigurationManager.GetConfigurationParams`.
Verify: `swapi.py members IConfigurationManager`.
## Lightweight and suppressed components
Failure: `GetModelDoc2` returns Nothing, bodies are missing, or `IsSuppressed` reports True for a component that is only lightweight.
Rule: check `IComponent2.GetSuppression2` (`swComponentSuppressionState_e`) before reading model data. Resolve with `IComponent2.SetSuppression2(swComponentResolved)` or `IAssemblyDoc.ResolveAllLightWeightComponents`, never while a PropertyManager page is open (`SetSuppression2` refuses). `IComponent2.IsHidden` and `IsSuppressed` return True for lightweight components. Opening behavior comes from `swOpenDocOptions_LoadLightweight` with `swOpenDocOptions_OverrideDefaultLoadLightweight`, the `swAutoLoadPartsLightweight` toggle and `swResolveLightweight`; Large Design Review (`swOpenDocOptions_ViewOnly`) loads no model data at all.
Verify: `swapi.py enum swComponentSuppressionState_e`.
## Active and visible documents
Failure: export, selection or view updates silently do nothing because the document is open but not active or not visible.
Rule:
- `OpenDoc6` and `OpenDoc7` do not activate a document that is already loaded as a reference of an assembly or drawing, and `ISldWorks.ActiveDoc` will not return it. Activate with `ISldWorks.ActivateDoc3`, passing the name with its extension (a part and an assembly can share a base name).
- STEP, IGES and STL export through `IModelDocExtension.SaveAs3` requires the document to be the active document.
- `SelectByID2` requires an open, visible document.
- A document loaded invisibly after `ISldWorks.DocumentVisible(False, type)` cannot be shown with `IModelDoc2.Visible`; close and reopen it.
- Some operations, notably drawing view updates, need SOLIDWORKS visible (`ISldWorks.Visible`); when something does not update, retry with the application visible.
- Saving to PDF from a document opened view-only is not supported.

Verify: `swapi.py doc IModelDocExtension.SaveAs3`.
## User preferences
Failure: a macro changes a system option (STEP AP, PDF color, component-rename behavior) and every later session silently inherits it.
Rule: system options (`ISldWorks.GetUserPreferenceToggle`, `SetUserPreferenceToggle`, `GetUserPreferenceIntegerValue`, `SetUserPreferenceIntegerValue`, `SetUserPreferenceStringValue`) persist across sessions; document properties (`IModelDocExtension.GetUserPreferenceToggle`, `SetUserPreferenceToggle`, `GetUserPreferenceInteger`, `SetUserPreferenceInteger`) persist in the file. Read the current value, set yours, do the work, and restore in a cleanup path that also runs after errors. To find the enum for a dialog option, record a macro while changing it, or use the swconst option topics such as `markdown/swconst/FileSaveAsSTEPOptions.md` (`swStepAP` takes 203 or 214).
Verify: `swapi.py enum swUserPreferenceIntegerValue_e --grep Step`.
## VBA declarations
Failure: overflow or type-mismatch errors, undeclared typos that evaluate to Empty, and late-bound calls without IntelliSense or compile checks.
Rule: start every module with `Option Explicit`; reference the SOLIDWORKS type library and the Constant type library and declare variables with their types (`Dim swApp As SldWorks.SldWorks`); use `Long` for every API integer (VBA `Integer` is 16-bit) and `Variant` for arrays; pass `Nothing` for unused object parameters (Callout, ExportData, AdvancedSaveAsOptions); mark Win32 `Declare` statements `PtrSafe` with `LongPtr` handles. Details and the skeleton are in [vba-macros.md](vba-macros.md).
Verify: `swapi.py sig IModelDocExtension.SaveAs3 --vba`.
## COM object lifetime
Failure: memory growth or a hung SOLIDWORKS process in long standalone runs, "COM object that has been separated from its underlying RCW cannot be used", and add-ins that break other add-ins.
Rule:
- Objects obtained from a document are invalid after `ISldWorks.CloseDoc` closes it; fetch them again from a fresh `IModelDoc2`.
- Out-of-process .NET loops: release per-file objects with `Marshal.ReleaseComObject` once you are completely done with them, then drop the reference; never use a variable after releasing it, and never release an object that another variable or a cache still uses.
- In-process add-ins: do not call `Marshal.ReleaseComObject` on shared objects during the session; the SDK template releases `ISldWorks` once in `DisconnectFromSW` and then forces `GC.Collect` and `GC.WaitForPendingFinalizers` twice.
- Unmanaged C++: every returned interface pointer carries a reference you must release, or use `CComPtr`.

Verify: compare with the add-in template in [dotnet-addins.md](dotnet-addins.md).
## Batch performance
Failure: batch jobs that run for hours because every call redraws, rebuilds trees, or shows dialogs.
Rule: around a sequence of calls, and restoring each setting afterwards:
- Out-of-process programs set `ISldWorks.CommandInProgress` to True (it has no effect in-process).
- Disable redraw and tree updates: `IModelView.EnableGraphicsUpdate` (view from `IModelDoc2.ActiveView`), `IFeatureManager.EnableFeatureTree` plus `EnableFeatureTreeWindow`, `IConfigurationManager.EnableConfigurationTree`. For sketch creation set `ISketchManager.AddToDB` and `ISketchManager.DisplayWhenAdded`; both stay set after the program ends.
- `IAssemblyDoc.EnableAssemblyRebuild` is True to suspend assembly rebuilds and applies to the root assembly only; set it after each load.
- Open with `swOpenDocOptions_Silent` (`IDocumentSpecification.Silent`) and read-only when nothing is saved; hide documents with `ISldWorks.DocumentVisible(False, type)` before opening and restore it.
- Close every document you open with `ISldWorks.CloseDoc`; in a background session started by your program with `ISldWorks.UserControl` False, closing the last document ends the session.
- For metadata of many files (custom properties, configurations, references) use the Document Manager API instead of opening models ([document-manager.md](document-manager.md)).

Verify: `swapi.py doc ISldWorks.CommandInProgress`.
## Persistent references
Failure: code stores feature names or traversal indexes, which change when users rename or reorder features.
Rule: store a persistent ID from `IModelDocExtension.GetPersistReference3` and resolve it later with `IModelDocExtension.GetObjectByPersistReference3`, checking its ErrorCode. Identify features by `IFeature.GetTypeName2` and `IFeature.GetSpecificFeature2`, not by default names such as `Plane1`.
Verify: `swapi.py doc IModelDocExtension.GetObjectByPersistReference3`.
## Sources
- `markdown/sldworksapiprogguide/Overview/Units.md`
- `markdown/sldworksapiprogguide/Overview/Selection_Criteria.md`
- `markdown/sldworksapiprogguide/Overview/Bitmasks.md`
- `markdown/sldworksapiprogguide/Overview/Return_Values.md`
- `markdown/sldworksapiprogguide/Overview/Arrays.md`
- `markdown/sldworksapiprogguide/Overview/SafeArraysVB.md`
- `markdown/sldworksapiprogguide/Overview/IDispatch_Object_Arrays_as_Input_in_.NET.md`
- `markdown/sldworksapiprogguide/Overview/Long_vs_Integer.md`
- `markdown/sldworksapiprogguide/Overview/Interface_Pointers.md`
- `markdown/sldworksapiprogguide/Overview/API_Functionality_Dependent_on_SolidWorks_Being_Visible.md`
- `markdown/sldworksapiprogguide/Overview/Suspend_Automatic_Rebuilds.md`
- `markdown/sldworksapiprogguide/Overview/Persistent_Reference_IDs.md`
- `markdown/sldworksapiprogguide/Overview/System_Options_and_Document_Properties.md`
- `markdown/sldworksapiprogguide/Overview/Components,_Configurations,_and_Suppression_States.md`
- `markdown/sldworksapiprogguide/Overview/Work_with_Lightweight_Components.md`
- `markdown/sldworksapiprogguide/Overview/Sweep_Features_and_SweepFeatureData_Objects.md`
- `markdown/sldworksapiprogguide/Miscellaneous/Selection_Lists.md`
- `markdown/apihelp/ContactingAPISupport/RefLeaks.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc3.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DocumentVisible.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CommandInProgress.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNameForSelection.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelDoc2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get6.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EnableFeatureTree.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EnableAssemblyRebuild.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md`
- `markdown/sldworksapi/Create_TaskPaneView_Add-in_Example_CSharp.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.md`
- `markdown/swconst/FileSaveAsSTEPOptions.md`
