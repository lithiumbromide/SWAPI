---
title: "IPageSetup Interface Members"
project: "SOLIDWORKS API Help"
interface: "IPageSetup_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html"
---

# IPageSetup Interface Members

The following tables list the members exposed by [IPageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CenterFooter | Gets or sets the page footer in the center of the page. |
| Property | CenterHeader | Gets or sets the page header in the center of the page. |
| Property | DrawingColor | Sets the color of the drawing for printing. |
| Property | FooterTextFormat | Gets or sets the text format for the page footer. |
| Property | HeaderTextFormat | Gets or sets the text format for the page header. |
| Property | HighQuality | Gets or sets whether to print a drawing in high quality. |
| Property | LeftFooter | Gets or sets the page footer on the left side of the page. |
| Property | LeftHeader | Gets or sets the page header on the left side of the page. |
| Property | Orientation | Gets or sets the page orientation. |
| Property | PrinterPaperLength | Gets or sets the user-defined printer paper length for this document or sheet. |
| Property | PrinterPaperSize | Gets or sets the printer paper size for this document or sheet. |
| Property | PrinterPaperSource | Gets or sets the printer paper source for this document or sheet. |
| Property | PrinterPaperWidth | Gets or sets the user-defined printer paper width for this document or sheet. |
| Property | RightFooter | Gets or sets the page footer on the right side of the page. |
| Property | RightHeader | Gets or sets the page header on the right side of the page. |
| Property | Scale2 | Gets or sets the scale for printing the page. |
| Property | ScaleDraftEdges | Gets or sets whether to scale draft edges when printing a drawing in high quality. |
| Property | ScaleToFit | Enables or disables scaling the page to fit the printer. |
| Property | UsePageSetupOnSheets | Obsolete. Superseded by IModelDocExtension::UsePageSetup . |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetHeaderFooterString | Gets the specified standard string that can be used in headers and footers. |
| Method | GetResolution | Gets the current printer resolution on documents and drawing sheets. |
| Method | GetUseDefaultResolution | Gets whether the printer default resolution is in use on documents and drawing sheets. |
| Method | SetFooter | Sets the entire page footer. |
| Method | SetHeader | Sets the entire page header. |
| Method | SetResolution | Sets the current printer resolution on documents and drawing sheets. |

[Top](#topBookmark)

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
