# Versions and release changes
How to read availability data, map years to revision and file-version numbers, target older SOLIDWORKS installs, and answer what changed in the 2026 API.
## Contents
- [Reading availability](#reading-availability)
- [Revision numbers](#revision-numbers)
- [File version numbers](#file-version-numbers)
- [Interop assemblies and older targets](#interop-assemblies-and-older-targets)
- [Saving for older releases](#saving-for-older-releases)
- [64-bit safe members](#64-bit-safe-members)
- [Answering what changed](#answering-what-changed)
- [What changed in 2026](#what-changed-in-2026)
- [What changed in 2025](#what-changed-in-2025)
## Reading availability
- `since` comes from each member's Availability line: `SOLIDWORKS 2020 SP02, Revision Number 28.2` becomes `2020 SP2`, `FCS` is the first customer shipment (SP0). Add-on modules use their product name with the same years: `SOLIDWORKS Simulation API 2012 SP0`, `SOLIDWORKS Document Manager API 2019 SP0`, `SOLIDWORKS Visualize Add-in API 2026 FCS`.
- A member is usable on a target when its `since` is at or below the target release and service pack; how to apply this, and the obsolete chain, are covered by [version availability](correctness-rules.md#version-availability) and [current members only](correctness-rules.md#current-members-only).
- Release notes and Availability can disagree (the 2026 Document Manager release-note page is still headed 2025 while its new members say `2026 SP0`); trust the member's Availability line.
## Revision numbers
- The major revision is the release year minus 1992, from SOLIDWORKS 2000 (8) onward: 2019 is 27, 2020 is 28, 2021 is 29, 2022 is 30, 2023 is 31, 2024 is 32, 2025 is 33, 2026 is 34.
- `ISldWorks.RevisionNumber` returns `major.minor.hotfix` as a string, the minor part being the service pack (`8.1.0` for 2000 SP1, `8.2.0` for SP2); parse the text before the first dot.
- Add-on ProgIDs derive from it: `SldWorks.Simulation.<major - 15>` ([simulation.md](simulation.md#getting-the-simulation-object)) and `SWDesignChecker.SWDesignCheck.<major + 1992>` ([addon-apis.md](addon-apis.md#design-checker)).
## File version numbers
`ISldWorks.VersionHistory` and `IModelDoc2.VersionHistory` (one entry per release that saved the file) and the Document Manager's `ISwDMDocument.GetVersion` use the same internal numbers:

| Release | Number |
| --- | --- |
| 99 | 1137 |
| 2000 | 1500 |
| 2001 | 1750 |
| 2001Plus | 1950 |
| 2003 to 2012 | 2200, 2500, 2800, 3100, 3400, 3800, 4100, 4400, 4700, 5000 |
| 2013 and later | 1000 times (year minus 2007): 2013 is 6000, 2024 is 17000, 2025 is 18000, 2026 is 19000 |

A file saved by a newer release opens in an older one only if it was saved to that older format ([saving for older releases](#saving-for-older-releases)); test loaded documents with `IModelDocExtension.IsFutureVersion`.
## Interop assemblies and older targets
- The interop assemblies carry the revision as their major version (a 2026 SP4.1 installation ships `SolidWorks.Interop.sldworks` 34.4.1.x). SOLIDWORKS never changes an existing COM member and adds new ones under new names, which is why obsolete members keep working and suffixes grow.
- Code compiled against an older release's interops runs on newer releases. Code compiled against newer interops runs on an older release only while it calls members that release has; anything newer fails at run time. Either build against the oldest supported release's `api\redist` folder (the templates' `$(SolidWorksApiRedist)` property, see [dotnet-addins.md](dotnet-addins.md#project-and-interop-references)), or build against the newest and run `swapi.py check FILE --target YEAR`.
- When one binary must use newer members where available, compare the major revision from `ISldWorks.RevisionNumber` and branch, for example `IView.InsertBomTable6` on 33 or later and `IView.InsertBomTable4` otherwise.
- VBA macros bind to the type libraries of the installation that runs them; upgrade problems are covered in [vba-macros.md](vba-macros.md#64-bit-vba-and-upgrades).
## Saving for older releases
- `swSaveAsVersion_e` has no year values: `swSaveAsCurrentVersion` is the normal save, the other members convert drawings (`swSaveAsDetachedDrawing`, `swSaveAsStandardDrawing`).
- From 2024, `IAdvancedSaveAsOptions.SaveAsPreviousVersion` takes a file version number from the table above; the help requires renaming or relocating every reference with `IAdvancedSaveAsOptions.ModifyItemsNameAndPath`, because overwriting the same files is not supported. Pass the options object to `IModelDocExtension.SaveAs3`.
- From 2026 SP3, `IModelDocExtension.CheckVersionCompatibility(swSaveToVersion_e, swCompatibilityDialogOptions_e, out Incompatibilities, out Warnings)` reports what prevents saving to the previous (`swSaveToVersion_Penultimate`) or second previous (`swSaveToVersion_Antepenultimate`) release as `IVersionCompatibilityItem` objects (`IVersionCompatibilityItem.Message`, `IVersionCompatibilityItem.Action`) and returns `swVersionCompatibilityResult_e`; `DSldWorksEvents_FileSaveToVersionFailNotifyEventHandler` fires when such a save fails.
## 64-bit safe members
SOLIDWORKS has been 64-bit only since 2016. The 2026 programming guide lists members that pass window handles or pointers as 32-bit integers, which can be silently truncated and crash later; replace them with their x64 counterparts: `IFrame.GetHWndx64`, `IModelView.GetViewHWndx64`, `IFeatMgrView.GetFeatMgrViewWndx64`, `ISldWorks.PostMessageToApplicationx64`, `ISldWorks.PreviewDocx64`, `IModelViewManager.DisplayWindowFromHandlex64`, `ITaskpaneView.DisplayWindowFromHandlex64`, `IPropertyManagerPage2.SetTitleBitmapx64`, and for FeatureManager views `IModelDocExtension.AddFeatureMgrView3x64` and `IModelDocExtension.ActivateFeatureMgrViewx64` (2026 SP1). The help marks the 32-bit members obsolete, so `swapi.py check` reports them.
## Answering what changed
1. Run `swapi.py changes --since 2026` for members first available in 2026, narrowed with `--module` (`sldworksapi`, `cworksapi`, `swdocmgrapi`, `swvisualizeapi`) and `--kind added,obsoleted`.
2. Read the module's release-note topic with `swapi.py topic "Release Notes"`; the notes are grouped by service pack, so quote the SP with every item.
3. For a domain question (drawings, BOMs, balloons), filter the results by interface (`IDrawingDoc`, `IView`, `ISheet`, `IBomTableAnnotation`, `IAutoBalloonOptions`) and say plainly when a release added nothing for that domain.
4. Check `since` and obsolete status of each item before recommending it for the user's target ([version availability](correctness-rules.md#version-availability)).
## What changed in 2026
SOLIDWORKS API 2026 release notes (product renamed SOLIDWORKS Design in example titles):
- SP0: Dassault Systemes physically based rendering appearances (`IDSPBRMaterial`, `IRenderMaterial.GetDSPBRMaterial`, `IRenderMaterial.HasDSPBRProperties`); family tables in drawings (`ISheet.InsertFamilyTable`, `IFamilyTableAnnotation`, `IFamilyTableFeature`); top-level body-folder items (`IBodyFolder.GetTopLevelFeatureCount`, `IBodyFolder.GetTopLevelFeatures`) and solid body folder reorder events; `ISldWorks.ShadedEdgeThickness`; moving parent drawing views independently (`IView.SetViewPosition`, `DDrawingDocEvents_ViewPositionChangeNotifyEventHandler`).
- SP1: `IBoundingBoxFeatureData.CoordinateSystem`; texture properties on `IDSPBRMaterial`; 64-bit FeatureManager view methods on `IModelDocExtension`; `IModelView.UpAxisFlyout`.
- SP2: `IComponent2.HasAssemblyFeatures`; DimXpert angle-between dimensions and reference-plane features; all-over symbols (`IGtol.GetAllOver`, `IGtol.SetAllOver`); `IView.RootDrawingComponent2`, which obsoletes `IView.RootDrawingComponent`.
- SP3: version compatibility checks (`IModelDocExtension.CheckVersionCompatibility`, `IVersionCompatibilityItem`), the FileSaveToVersionFailNotify application event, and AddDependencyNotify and DeleteDependencyNotify events for parts, assemblies and drawings.
- Drawings, BOMs and balloons: 2026 adds family tables, view positioning, `IView.RootDrawingComponent2` and the dependency events, but no new balloon or BOM-table members; the newest BOM insert remains `IView.InsertBomTable6` from 2025.
- STEP AP242: `IModelDocExtension.PublishSTEP242File2` with `IMBDSTEP242Data` (2025 SP3) obsoletes `IModelDocExtension.PublishSTEP242File`.
- Simulation API 2026: cable connectors (`ICWCable`, `ICWLoadsAndRestraintsManager.AddCable`, `ICWLoadsAndRestraintsManager.GetCable`, cable mass in `ICWMassPropertiesManager`), general spring connectors (`ICWGeneralSpringConnector`) and `ICWBucklingStudyOptions.ExtractPositiveBucklingFactorsOnly`.
- Document Manager: `ISwDMDocument30.SavedInLDREditMode` (2026 SP0) and untrimmed sheet data on `ISwDMDocument31` (`ISwDMDocument31.GetSheetNamesUntrimmed`, 2026 SP2).
- New module: the SOLIDWORKS Visualize Add-in API (`swvisualizeapi`), see [addon-apis.md](addon-apis.md#visualize).
- New programming-guide topics: Eliminating 32-bit only API use ([64-bit safe members](#64-bit-safe-members)) and SOLIDWORKS Design connected to the 3DEXPERIENCE platform.
## What changed in 2025
For users upgrading from 2024:
- SP0: `IView.InsertBomTable6` obsoletes `IView.InsertBomTable5`; `IView.ImportAnnotations` imports annotations into drawings; `IModelDocExtension.ReloadWithReferences` reloads only selected references; new `IRenderMaterial` surface-finish properties replace the bump-map members.
- SP1: `ICoordinateSystemElement`; `IView.GetFirstNote2` and sibling `GetFirst*` methods replace the older view iterators; `IPackAndGo.SetSaveToName2` obsoletes `IPackAndGo.SetSaveToName`, and `IPackAndGo.FolderStructureOption` is new.
- SP2: `IConvertSolidFeatureData` and `ILibraryFormToolFeatureData` replace `IFeatureManager.InsertConvertToSheetMetal2` and `IFeatureManager.InsertFormToolFeature`.
## Sources
- `markdown/sldworksapi/ReleaseNotes-sldworksapi.md`
- `markdown/cworksapi/ReleaseNotes-swsimulationapi.md`
- `markdown/swdocmgrapi/ReleaseNotes-swdocmgrapi.md`
- `markdown/swvisualizeapi/ReleaseNotes.md`
- `markdown/sldworksapiprogguide/Overview/Eliminating_32-Bit_Only_API_Use.md`
- `markdown/sldworksapiprogguide/Overview/Accessing_Add-ins.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RevisionNumber.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SaveAsPreviousVersion.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CheckVersionCompatibility.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishSTEP242File2.md`
- `markdown/swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveAsVersion_e.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveToVersion_e.md`
