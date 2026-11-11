# Files and output
Opening, creating, saving and closing drawings, batch runs, export to PDF, SVG and images, printing and drawing properties. Saving and batch rules are in [correctness-rules.md](correctness-rules.md#saving).
## Open, create, close
- Open: `IApplication.OpenDocument2(PathName, dsDocumentOpenOption_e, dsEncoding_e)`; the shipped examples pass `dsDocumentOpen_Default` and `dsEncoding_Default`. `dsDocumentOpen_ReadOnly` and `dsDocumentOpen_Hidden` suit batch reads. It returns Nothing when the file cannot be opened; there is no error out parameter, so check the path first and report the file.
- Already open: loop `IApplication.GetDocuments` (a Variant or `object[]` of `Document`) and compare `IDocument.GetPathName` case-insensitively before opening again.
- New: `IApplication.NewDocument(TemplateName)` with the full path of a `.dwt` template; no document is created when the template does not exist, and the template folder depends on the installation and profile, so ask or read it from the user's setup.
- Active document: `IApplication.GetActiveDocument`; switch with `IDocument.Activate`.
- Close: `IApplication.CloseDocument(PathName, SaveChanges)` with the document's `GetPathName`.
- State checks: `IDocument.IsReadOnly(out ReadOnly)` (an out parameter, not a return value), `IsDirty()`; `IDocument.SetDirty` (2020 SP4) marks a document as modified so a later save writes it.
## Save
- `IDocument.Save()` returns `dsDocumentSaveError_e`.
- `IDocument.SaveAs2(Name, dsDocumentSaveAsOption_e, Overwrite, out dsDocumentSaveError_e)`: DWG members are `dsDocumentSaveAs_R12_DWG` to `dsDocumentSaveAs_R2018_DWG`, DXF members end in `_ASCII_DXF` or `_BINARY_DXF`, templates use `dsDocumentSaveAs_TEMPLATE_DWT`. The help does not say which format `dsDocumentSaveAs_Default` writes, so name the format explicitly. Run `swapi.py enum dsDocumentSaveAsOption_e` for the full list.
- Write part of a drawing to its own file: `IDocument.WriteBlockByName`, `WriteBlockBySpecifiedEntities`, `WriteBlockByAllEntities` (2017 SP2).
- Purge and audit: `IDocument.Clean`, `IDocument.ErrorCheck`.
## Batch runs
1. Connect and call `AbortRunningCommand`.
2. For each file: skip files already open or reuse them; `OpenDocument2`; on Nothing record the failure and continue.
3. Process model space and each sheet ([model and sheets](correctness-rules.md#model-and-sheets)).
4. Save to the output path with `SaveAs2` or export, record `dsDocumentSaveError_e` flags, then `CloseDocument(path, False)` for documents the script opened.
5. Print a summary of processed and failed files and return a non-zero exit code from EXEs when anything failed.

The standalone template [Program.cs](../assets/csharp-standalone/Program.cs) follows these steps for PDF export.
## Export
- PDF: `IDocument.GetDocumentExporter()`, `IDocumentExporter.CreateExportSettings()` (2018), set `IExportSettings.Sheets` to a String array of sheet names (from `GetSheets2` and `ISheet.Name`), optionally `PaperSize` (one of `GetAvailablePaperSizes`), `PrintStyleTable` (`monochrome.ctb`), `SetPrintMargins`, `EnableLayersInPDFFile`, then `ExportToPdf2(PathName, ExportSettings)`, which returns True on success. The obsolete `ExportToPdf` took page sizes directly.
- Images of the current view: `IDocumentExporter.ExportToPng`, `ExportToJpg`, `ExportToBmp`, `ExportToTiff`, `ExportToEmf`, `ExportToSvg`; read each signature for size and resolution parameters. Activate the sheet or view to export first.
- SVG of a drawing file without opening it in the UI: `IApplication.ExportToSvg2(DrawingFilePath, SvgFilePath, GrayScale, out Success)` (2021).
- Preview bitmaps: `IApplication.GetPreviewBitmapFile`, `GetPreviewBitmapBytes`, `GetPreviewOfEntities`.
## Printing
`IApplication.GetPrintManager()` returns `IPrintManager`: set `Printer` (one of `GetAvailablePrinters`), `PaperSize`, `Orientation`, `StyleTable`, `ScaleToFit` or `SetStandardScale`, `SetPrintRange`, then `SetSheets(SheetNameStrArray)` and `PrintOut(Copies, FileName)`. The Remarks require `SetSheets` before `PrintOut`; an empty `FileName` prints to the printer, a path prints to that file and overwrites an existing one. Record and restore the printer settings you change, because they persist for the user. See `swapi.py example "Get and Set Print Options Example (C#)"`.
## Drawing properties
`IDocument.GetDrawingProperties()` returns `IDrawingProperties` with the standard properties (author, title, subject, keywords) and `GetCustomProperty(Key)`, `SetCustomProperty(Key, Value)` for custom ones; save the document afterwards. See `swapi.py examples "Drawing Properties"`.
