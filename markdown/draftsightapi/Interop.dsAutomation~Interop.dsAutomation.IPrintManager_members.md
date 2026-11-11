---
title: "IPrintManager Interface Members"
project: ""
interface: "IPrintManager_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html"
---

# IPrintManager Interface Members

The following tables list the members exposed by [IPrintManager](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | HideGeometryOnSheet | Gets or sets whether the geometry of the model shown in Viewports is printed with hidden lines removed. |
| Property | Orientation | Sets the page orientation for printing. |
| Property | PaperSize | Gets or sets the name of the size of the paper. |
| Property | Printer | Gets or sets the name of the printer to use. |
| Property | PrintInBackground | Gets or sets whether to print the drawing in the background. |
| Property | PrintInverse | Gets or sets whether to flip the drawing for printing. |
| Property | PrintOnCenter | Gets or sets whether to use same-size margins at the top, bottom, left, and right for print offset. |
| Property | PrintSheetLast | Gets or sets whether to print first the geometry of the model in Viewports or the geometry of the Sheet in the graphics area. |
| Property | Quality | Gets or sets print quality. |
| Property | ScaleLineWeight | Gets or sets whether to scale LineWeight to the print scale. |
| Property | ScaleToFit | Gets or sets whether to scale the printout to fit the paper. |
| Property | StyleTable | Gets or sets the name of the PrintStyle table. |
| Property | UseAssignedLineWeight | Gets or sets whether to print entities in the LineWeights assigned in the Layers . |
| Property | UseAssignedPrintStyle | Gets or sets whether PrintStyles applied to Layers and entities are printed. |
| Property | UserScale | Gets or sets whether to use a user-defined scale when printing. |
| Property | ViewDisplayStyle | Gets or sets the display state for Shaded views when printing the Model view. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AvailablePaperSizes | Gets the names of the available paper sizes. |
| Method | AvailablePaperSizesInLocale | Gets the names of the localized paper sizes for this locale. |
| Method | GetAvailablePrinters | Gets the names of the available printers. |
| Method | GetAvailablePrintStyleTables | Gets the currently available PrintStyle tables. |
| Method | GetPaperSize | Gets the size of the paper. |
| Method | GetPrintMargins | Gets the size of the margins of the paper size specified to use for printing. |
| Method | GetPrintOffset | Gets the margins for print offset. |
| Method | GetPrintRange | Gets the area to print. |
| Method | GetSheets | Gets the sheets to print. |
| Method | GetStandardScale | Gets the standard scale and value of the scale for printing. |
| Method | GetUserScaleValue | Gets the user-defined paper and drawing units (millimeters or inches) for printing. |
| Method | PaperSizeInLocale | Gets the name of the localized paper size that corresponds to the specified non-localized paper size. |
| Method | PrintOut | Prints the specified number of copies of the active document to the specified file or printer. |
| Method | SetClosestValidPaperSize | Sets the size of the paper to a valid size for the printer that is closest to the specified length and width. |
| Method | SetPrintMargins | Sets the size of the margins for the paper size specified to use for printing. |
| Method | SetPrintOffset | Sets the margins for print offset. |
| Method | SetPrintRange | Sets the area to print. |
| Method | SetSheets | Sets the sheets to print. |
| Method | SetStandardScale | Sets the standard scale for printing. |
| Method | SetUserScaleValue | Sets the user-defined paper and drawing units (millimeters or inches) for printing. |

[Top](#topBookmark)

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocumentSupportFiles::PrintSettingsPath ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~PrintSettingsPath.html)
