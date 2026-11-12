# Drawings
Creating drawings, sheets and views, traversing them, and working with annotations, notes, title blocks, balloons and BOM tables.
## Contents
- [New drawings and sheets](#new-drawings-and-sheets)
- [Creating views](#creating-views)
- [Traversing sheets and views](#traversing-sheets-and-views)
- [Annotations and dimensions](#annotations-and-dimensions)
- [Notes and title blocks](#notes-and-title-blocks)
- [Balloons](#balloons)
- [Bill of materials](#bill-of-materials)
- [Tables](#tables)
- [Updating and exporting](#updating-and-exporting)
## New drawings and sheets
- Create the document with `ISldWorks.NewDocument(TemplateName, PaperSize, Width, Height)`; take the template from `ISldWorks.GetUserPreferenceStringValue(swDefaultTemplateDrawing)` unless the user names one. PaperSize uses `swDwgPaperSizes_e`; Width and Height (meters) apply only to user-defined sizes. Cast the result to `IDrawingDoc`.
- Add sheets with `IDrawingDoc.NewSheet4` and change them with `IDrawingDoc.SetupSheet6` or `ISheet.SetProperties2` (`ISheet.GetProperties2` reads them). TemplateIn uses `swDwgTemplates_e`; pass `swDwgTemplateCustom` with a full sheet-format path, or `swDwgTemplateNone` with a paper size.
- Sheet formats: `ISheet.GetTemplateName`, `ISheet.SetTemplateName` and `ISheet.ReloadTemplate`; edit the format's own geometry between `IDrawingDoc.EditTemplate` and `IDrawingDoc.EditSheet2` (2024 SP2 and later; `IDrawingDoc.EditSheet` before that, see [version availability](correctness-rules.md#version-availability)).
## Creating views
- Standard three views: `IDrawingDoc.Create3rdAngleViews2(ModelPath)` or `IDrawingDoc.Create1stAngleViews2(ModelPath)`; they follow the document's automatic scaling setting.
- One view: `IDrawingDoc.CreateDrawViewFromModelView3(ModelPath, ViewName, X, Y, Z)` places the view center at sheet coordinates in meters. ModelPath is the full path with extension (`IModelDoc2.GetPathName` of an open model); ViewName must match the model view exactly, including the asterisk of standard views (`*Front`, `*Isometric`). The view scale follows `swAutomaticScaling3ViewDrawings`, and on an empty sheet the sheet scale changes too.
- View palette: `IDrawingDoc.GenerateViewPaletteViews(ModelPath)` then `IDrawingDoc.DropDrawingViewFromPalette2(PaletteViewName, X, Y, Z)`.
- Sheet metal flat pattern view: `IDrawingDoc.CreateFlatPatternViewFromModelView3`.
- Scale and display: `IView.ScaleRatio` or `IView.ScaleDecimal`, `IView.SetDisplayMode4`, `IView.ReferencedConfiguration` to switch the configuration shown.
## Traversing sheets and views
- Sheets: `IDrawingDoc.GetSheetNames`, `IDrawingDoc.ActivateSheet(Name)`, `IDrawingDoc.GetCurrentSheet`, `IDrawingDoc.Sheet(Name)`; `ISheet.GetViews` lists the views of any sheet without activating it.
- Views of the current sheet: `IDrawingDoc.GetFirstView` returns the sheet itself (it carries sheet sketches and notes); the first real drawing view is the next `IView.GetNextView`. Skip the sheet with `IView.Type` (`swDrawingViewTypes_e`, `swDrawingSheet`).
- Per view: `IView.GetName2`, `IView.Type`, `IView.ReferencedDocument` (the model, or Nothing for detached or unloaded models), `IView.GetReferencedModelName`, `IView.ReferencedConfiguration`. Load detached models with `IView.LoadModel` after checking `IView.IsModelLoaded`.
- Model geometry seen in a view: `IView.GetVisibleComponents` and `IView.GetVisibleEntities2(Component, swViewEntityType_e)` return components, edges, faces and vertices related to model topology; select them with `IEntity.Select4` using an `ISelectData` whose View is set. `IView.GetPolylines7` returns raw polylines without that relationship.
- `IDrawingDoc.ActivateView(ViewName)` and `IDrawingDoc.ActiveDrawingView` work with the active view; selected views come back from `ISelectionMgr.GetSelectedObject6` as `IView`.
## Annotations and dimensions
- Model annotations into views: `IDrawingDoc.InsertModelAnnotations3` (2005 and later) or `IDrawingDoc.InsertModelAnnotations4` (2024 and later) with option and type bitmasks; check `since` against the target release.
- Read annotations with `IView.GetAnnotations`, or walk `IView.GetFirstAnnotation3` and `IAnnotation.GetNext3`; display dimensions select as `DIMENSION` and come back as `IDisplayDimension` ([selection](correctness-rules.md#selection)).
- Note text size: approximate the bounding box from `IAnnotation.GetPosition`, `INote.GetUpperRight`, `INote.GetHeight` and `INote.GetLineCount`.
## Notes and title blocks
- Insert notes with `IModelDoc2.InsertNote(Text)` (returns an `INote`); change text with `INote.SetText`.
- `INote.GetText` returns the resolved text and `INote.PropertyLinkedText` the link source; the help's example link is `$PRPVIEW:"SW-Long Date"`. SOLIDWORKS link syntax also uses `$PRP:"Name"` for the drawing's own custom properties and `$PRPSHEET:"Name"` for the model shown on the sheet.
- Title blocks usually show model properties through such links, so fill the model's custom properties ([files-and-properties.md](files-and-properties.md#custom-properties)) or the drawing's own instead of editing note text; `ISheet.InsertTitleBlock` defines title-block fields, and its array input needs `DispatchWrapper` in .NET ([arrays and Variants](correctness-rules.md#arrays-and-variants)).
## Balloons
- Automatic: select the views (or a sheet for all its views), create options with `IDrawingDoc.CreateAutoBalloonOptions`, set `IAutoBalloonOptions.Layout` (`swBalloonLayoutType_e`), `IAutoBalloonOptions.Style`, `IAutoBalloonOptions.Size`, `IAutoBalloonOptions.UpperTextContent`, `IAutoBalloonOptions.IgnoreMultiple`, `IAutoBalloonOptions.ItemOrder` and `IAutoBalloonOptions.ItemNumberStart`, then call `IDrawingDoc.AutoBalloon5`; it returns the created notes. `IDrawingDoc.AutoBalloon4` is obsolete.
- Single BOM balloon: select the edge or face and call `IModelDocExtension.InsertBOMBalloon2` with balloon options.
- Balloons number from a BOM table; insert the BOM first so item numbers exist.
## Bill of materials
- Insert with the newest `IView.InsertBomTable*` your target release has: `IView.InsertBomTable6` (2025), `IView.InsertBomTable5` (2024), `IView.InsertBomTable4` (2013); see [version availability](correctness-rules.md#version-availability). Arguments: anchor or X and Y in meters, `swBOMConfigurationAnchorType_e`, `swBomType_e` (`swBomType_TopLevelOnly`, `swBomType_PartsOnly`, `swBomType_Indented`), configuration, template path (`.sldbomtbt`, under `install_dir\lang\<language>`), hidden flag, `swNumberingType_e` for indented BOMs, cut-list and grouping flags.
- For `swBomType_TopLevelOnly` leave Configuration empty and set configurations with `IBomFeature.SetConfigurations`; an empty Configuration otherwise means the configuration active when the drawing was created. An invalid configuration for parts-only and indented BOMs creates no table.
- Read an existing BOM: `IView.GetTableAnnotations` or the BOM feature's `IBomFeature.GetTableAnnotations`; cast to `IBomTableAnnotation` and `ITableAnnotation`. Cell text from `ITableAnnotation.Text2(Row, Column, IncludeHidden)` with `ITableAnnotation.RowCount`, `ITableAnnotation.ColumnCount` and `ITableAnnotation.GetColumnTitle2`; components per row from `IBomTableAnnotation.GetComponentsCount2(Row, Configuration, ItemNumber, PartNumber)` and `IBomTableAnnotation.GetComponents2`.
- Sort: `IBomTableAnnotation.GetBomTableSortData`, set the `IBomTableSortData` properties, `IBomTableAnnotation.Sort`; reapply a saved scheme with `IBomTableAnnotation.ApplySavedSortScheme`.
- Model-side BOM tables in parts and assemblies use `IModelDocExtension.InsertBomTable4`.
## Tables
- General tables: `IDrawingDoc.InsertTableAnnotation2(UseAnchorPoint, X, Y, AnchorType, TableTemplate, Rows, Columns)`, then write cells through `ITableAnnotation.Text2`; insert columns with `ITableAnnotation.InsertColumn2`.
- Selected tables come back from `ISelectionMgr.GetSelectedObject6` as `ITableAnnotation`; cast to the specific interface (`IBomTableAnnotation`, `IHoleTableAnnotation`, `IGeneralTableAnnotation`, `IWeldmentCutListAnnotation`) before sorting.
## Updating and exporting
- Rebuild only what changed with `IModelDocExtension.Rebuild` and `swRebuildOptions_e` (`swCurrentSheetDisp`, `swUpdateDirtyOnly`). View updates can depend on SOLIDWORKS being visible ([active and visible documents](correctness-rules.md#active-and-visible-documents)).
- Set document-level line weights rather than system-level ones; legacy (2008 and earlier) documents need system line weights set before opening.
- PDF and DXF export are in [files-and-properties.md](files-and-properties.md#pdf) and [DXF and DWG](files-and-properties.md#dxf-and-dwg).
## Sources
- `markdown/sldworksapiprogguide/Overview/Drawing_Views_and_Model_Entities.md`
- `markdown/sldworksapiprogguide/Overview/Sorting_Tables.md`
- `markdown/sldworksapiprogguide/Overview/Bounding_Box_and_Note_Text.md`
- `markdown/sldworksapiprogguide/Overview/Line_Weights.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~NewDocument.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet4.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon5.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations4.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable6.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable5.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable4.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PropertyLinkedText.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text2.md`
- `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet2.md`
- `markdown/sldworksapi/Insert_BOM_Table_and_BOM_Balloon_Example_CSharp.md`
- `markdown/sldworksapi/Get_Components_in_Each_BOM_Table_Row_Example_CSharp.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDrawingViewTypes_e.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBomType_e.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBalloonLayoutType_e.md`
- `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRebuildOptions_e.md`
