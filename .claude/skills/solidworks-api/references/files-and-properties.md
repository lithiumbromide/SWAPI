# Files and custom properties
Opening, saving and exporting documents, looping configurations, and reading or writing custom properties with the SOLIDWORKS API.
## Contents
- [Opening documents](#opening-documents)
- [Saving and exporting](#saving-and-exporting)
- [Export format options](#export-format-options)
- [PDF](#pdf)
- [DXF and DWG](#dxf-and-dwg)
- [Configuration loops](#configuration-loops)
- [Custom properties](#custom-properties)
- [Batch processing](#batch-processing)
## Opening documents
- `ISldWorks.OpenDoc6(FileName, Type, Options, Configuration, Errors, Warnings)`: Type from `swDocumentTypes_e` matching the extension (`swDocPART`, `swDocASSEMBLY`, `swDocDRAWING`), Options from the `swOpenDocOptions_e` bitmask (`swOpenDocOptions_Silent`, `swOpenDocOptions_ReadOnly`, `swOpenDocOptions_LoadLightweight`, `swOpenDocOptions_ViewOnly` for Large Design Review). An empty or unknown Configuration opens the last-used configuration. It returns Nothing on failure; decode Errors and Warnings ([errors and warnings](correctness-rules.md#errors-and-warnings)).
- `ISldWorks.OpenDoc7` takes an `IDocumentSpecification` from `ISldWorks.GetOpenDocSpec(path)`. Set `DocumentType`, `ReadOnly`, `Silent`, `ConfigurationName`, `DisplayState`, `LightWeight`, `ViewOnly` or `LoadExternalReferencesInMemory` on it, then read `Error` and `Warning` afterwards. Use it when you need a display state or the specification properties; otherwise `OpenDoc6` is equivalent.
- References of assemblies and drawings are resolved from the Search Folders (`ISldWorks.GetSearchFolders`, `ISldWorks.SetSearchFolders`) and then from the current working directory, which `OpenDoc6` and `OpenDoc7` do not change. To mimic File > Open, call `ISldWorks.SetCurrentWorkingDirectory` with the file's folder first.
- If the file is already loaded as a reference, the call returns that document without activating it ([active and visible documents](correctness-rules.md#active-and-visible-documents)).
- Files from newer releases open since 2012 SP5 without an error; test with `IModelDocExtension.IsFutureVersion`.
- STEP, IGES and other foreign formats are imported with `ISldWorks.LoadFile4`, using import options from `ISldWorks.GetImportFileData`.
## Saving and exporting
- Save under the current name with `IModelDoc2.Save3(Options, Errors, Warnings)`.
- Save as or export with `IModelDocExtension.SaveAs3(Name, Version, Options, ExportData, AdvancedSaveAsOptions, Errors, Warnings)`. The extension of Name selects the format (`.sldprt`, `.step`, `.igs`, `.x_t`, `.stl`, `.pdf`, `.dxf`, `.dwg`, `.edrw`); Version is normally `swSaveAsCurrentVersion` (use `swSaveAsDetachedDrawing` or `swSaveAsStandardDrawing` to convert drawings). Options come from `swSaveAsOptions_e`: `swSaveAsOptions_Silent`, `swSaveAsOptions_Copy` to keep editing the original, `swSaveAsOptions_SaveReferenced` for assemblies and drawings; the help notes these options target native formats. Pass Nothing or null for ExportData and AdvancedSaveAsOptions when unused.
- `SaveAs3` overwrites existing files unless they are read-only and fires FileSaveNotify; its selection and active-document requirements are under [selection](correctness-rules.md#selection) and [active and visible documents](correctness-rules.md#active-and-visible-documents).
- `IModelDocExtension.GetAdvancedSaveAsOptions(Options)` returns an `IAdvancedSaveAsOptions` for saving a subset of configurations (`IAdvancedSaveAsOptions.ConfigurationsToSave`), renaming or relocating references (`IAdvancedSaveAsOptions.ModifyItemsNameAndPath`), prefixes or suffixes (`IAdvancedSaveAsOptions.SetPrefixSuffixToAll`) and `IAdvancedSaveAsOptions.SaveAllAsCopy`; call it before `SaveAs3`.
- STEP AP242 with MBD (PMI) does not go through `SaveAs3`: with the MBD add-in loaded, fill the `IMBDSTEP242Data` from `IModelDocExtension.GetMBDSTEP242Data` (`IMBDSTEP242Data.PublishFileName`, `IMBDSTEP242Data.STEP242Edition`) and call `IModelDocExtension.PublishSTEP242File2` (2025 SP3 and later); older targets use the now obsolete `IModelDocExtension.PublishSTEP242File`.
- An assembly saved after renaming components needs its references saved too (`swFileSaveRequiresSavingReferences`); see [assemblies.md](assemblies.md#renaming-and-replacing).
## Export format options
Export settings are system options, so read them, set them, export, and restore them ([user preferences](correctness-rules.md#user-preferences)). The swconst topics `markdown/swconst/FileSaveAs*Options.md` map every dialog option to its enum and value.
- STEP: `swStepAP` integer (203 or 214), `swStepExportPreference` with `swAcisOutputGeometryPreference_e`, toggles `swStepExportConfigurationData`, `swStepExportFaceEdgeProps`, `swStepExportAppearances`, `swStepExportSplitPeriodic`, `swStepExport3DCurveFeatures`, and `swStepExportAtomicSave` to write assembly components as separate files.
- IGES: `swIGESRepresentation`, `swIGESSystem`, `swIGESCurveRepresentation` plus the `swIGES*` toggles. Parasolid: `swParasolidOutputVersion`. ACIS: `swAcisOutputVersion`, `swAcisOutputUnits`.
- STL: `swSTLQuality`, `swExportStlUnits`, toggles `swSTLBinaryFormat` and `swSTLComponentsIntoOneFile`.
- PDF: toggles `swPDFExportInColor`, `swPDFExportEmbedFonts`, `swPDFExportHighQuality`, `swPDFExportPrintHeaderFooter`, `swPDFExportUseCurrentPrintLineWeights`, integers `swPDFExportShadedDraftDPI` and `swPDFExportOleDPI`.
- DXF and DWG: `swDxfVersion`, `swDxfOutputFonts`, `swDxfOutputLineStyles`, `swDxfMultiSheetOption` (`swDxfMultisheet_e`), toggles `swDxfMapping`, `swDxfExportSplinesAsSplines`, `swDxfEndPointMerge`.
## PDF
- Drawings: get an `IExportPdfData` from `ISldWorks.GetExportFileData(swExportPdfData)`, choose sheets with `IExportPdfData.SetSheets(swExportDataSheetsToExport_e, Sheets)` (`swExportData_ExportAllSheets`, `swExportData_ExportCurrentSheet`, `swExportData_ExportSpecifiedSheets`), and pass it as ExportData to `SaveAs3` with a `.pdf` name. ExportData Nothing exports all sheets.
- For specified sheets the VBA example passes a Variant holding sheet names, while the C# example passes `ISheet` objects wrapped in `DispatchWrapper[]` ([arrays and Variants](correctness-rules.md#arrays-and-variants)); sheet names come from `IDrawingDoc.GetSheetNames`.
- `IExportPdfData.ExportAs3D` produces a 3D PDF from parts and assemblies; `IExportPdfData.ViewPdfAfterSaving` opens the result. Saving to PDF from a view-only document is not supported.
## DXF and DWG
- Drawings export through `SaveAs3` with a `.dxf` or `.dwg` name; `swDxfMultiSheetOption` decides between the active sheet, one file per sheet and one multi-sheet file.
- Parts, flat patterns and faces export with `IPartDoc.ExportToDWG2(FilePath, ModelName, Action, ExportToSingleFile, Alignment, IsXDirFlipped, IsYDirFlipped, SheetMetalOptions, Views)`. Action is `swExportToDWG_ExportSheetMetal`, `swExportToDWG_ExportSelectedFacesOrLoops` or `swExportToDWG_ExportAnnotationViews`. Alignment is 12 doubles (new origin, x direction, y direction, face normal); 12 zeros keep the default orientation.
- SheetMetalOptions is a bitmask: 1 flat-pattern geometry, 2 hidden edges, 4 bend lines, 8 sketches, 16 merge coplanar faces, 32 library features, 64 forming tools, 2048 bounding box (geometry plus bend lines plus sketches is 13). Multi-body sheet metal needs the flat-pattern features selected first. `IPartDoc.ExportFlatPatternView` and `IPartDoc.ExportToDWG` are obsolete.
## Configuration loops
- Follow [configurations](correctness-rules.md#configurations): remember the active configuration, loop `IModelDoc2.GetConfigurationNames`, activate each with `IModelDoc2.ShowConfiguration2`, rebuild when needed, export, and reactivate the original.
- Configuration names can contain characters that are invalid in file names (`\ / : * ? " < > |`); replace them before building output paths.
- Every export inside the loop obeys the [selection](correctness-rules.md#selection) and [active and visible documents](correctness-rules.md#active-and-visible-documents) rules.
## Custom properties
- Scope: `IModelDocExtension.CustomPropertyManager("")` (C#: `get_CustomPropertyManager("")`) is the file-level Custom tab; `IModelDocExtension.CustomPropertyManager(configName)` or `IConfiguration.CustomPropertyManager` is configuration-specific; weldment and sheet-metal cut-list items expose `IFeature.CustomPropertyManager`. The obsolete `IModelDoc2.CustomInfo2` family maps to these ([current members only](correctness-rules.md#current-members-only)).
- Read one: `ICustomPropertyManager.Get6(FieldName, UseCached, ValOut, ResolvedValOut, WasResolved, LinkToProperty)` returns `swCustomInfoGetResult_e` (`swCustomInfoGetResult_NotPresent` when missing). ValOut is the raw text, which may be an expression such as `"SW-Mass@Part1.SLDPRT"`; ResolvedValOut is the evaluated value. Pass UseCached False for current values.
- Read all: `ICustomPropertyManager.GetNames`, or `ICustomPropertyManager.GetAll3` (names, types, evaluated values, resolution status, link flags); `ICustomPropertyManager.Count` and `ICustomPropertyManager.GetType2` give count and `swCustomInfoType_e`.
- Write: `ICustomPropertyManager.Add3(FieldName, FieldType, FieldValue, OverwriteExisting)` with `swCustomInfoType_e` (`swCustomInfoText`, `swCustomInfoDate`, `swCustomInfoNumber`, `swCustomInfoDouble`, `swCustomInfoYesOrNo`, `swCustomInfoEquation`) and `swCustomPropertyAddOption_e` (`swCustomPropertyReplaceValue` to upsert, `swCustomPropertyDeleteAndAdd` to change the type, `swCustomPropertyOnlyIfNew`); it returns `swCustomInfoAddResult_e`. `ICustomPropertyManager.Set2` changes only existing properties (`swCustomInfoSetResult_e`); `ICustomPropertyManager.Delete2` returns `swCustomInfoDeleteResult_e`.
- Linked properties cannot be edited directly; test with `ICustomPropertyManager.IsCustomPropertyEditable`.
- Values are strings; changes stay in memory until the document is saved with `Save3`.
- Title-block links in drawings are covered in [drawings.md](drawings.md#notes-and-title-blocks); reading properties of many files without SOLIDWORKS is covered in [document-manager.md](document-manager.md).
## Batch processing
- One session for the whole batch. Per file: `OpenDoc6` with `swOpenDocOptions_Silent` (plus `swOpenDocOptions_ReadOnly` when nothing is saved), process, `Save3` only if changed, `ISldWorks.CloseDoc(fullPath)`, then release the objects ([COM object lifetime](correctness-rules.md#com-object-lifetime)). Log failures and continue with the next file.
- Apply the [batch performance](correctness-rules.md#batch-performance) settings around the loop.
- Control reference loading with `swLoadExternalReferences` (`swLoadExternalReferences_e`) and `swOpenDocOptions_LoadExternalReferencesInMemory`; open references read-only with the `swExtRefOpenReadOnly` toggle.
- Drawings that open slowly through the API can use background processing: `ISldWorks.EnableBackgroundProcessing`, `IDrawingDoc.BackgroundProcessingOption`, `ISldWorks.IsBackgroundProcessingCompleted`.
## Sources
- `markdown/sldworksapiprogguide/Overview/Import_and_Export_File_Options.md`
- `markdown/sldworksapiprogguide/Overview/Default_Paths.md`
- `markdown/sldworksapiprogguide/Overview/System_Options_and_Document_Properties.md`
- `markdown/sldworksapiprogguide/Miscellaneous/Obsolete_and_New_Custom_Properties_Methods_and_Properties.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocSpec.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAdvancedSaveAsOptions.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExportFileData.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~SetSheets.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ExportToDWG2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CustomPropertyManager.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get6.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Add3.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Delete2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll3.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnableBackgroundProcessing.md`
- `markdown/sldworksapi/Save_File_as_PDF_Example_CSharp.md`
- `markdown/sldworksapi/Save_File_as_PDF_Example_VB.md`
- `markdown/sldworksapi/Get_Custom_Properties_for_Configuration_Example_CSharp.md`
- `markdown/sldworksapi/Export_SOLIDWORKS_MBD_to_STEP_242_Example_VB.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishSTEP242File2.md`
- `markdown/swconst/FileSaveAsSTEPOptions.md`
- `markdown/swconst/FileSaveAsPDFOptions.md`
- `markdown/swconst/FileSaveAsDXFOptions.md`
- `markdown/swconst/SO_ExternalReferences.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveAsOptions_e.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swOpenDocOptions_e.md`
