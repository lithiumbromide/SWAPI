---
title: "ISwDMDocument Interface Members"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument_members"
member: ""
kind: "members"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html"
---

# ISwDMDocument Interface Members

The following tables list the members exposed by [ISwDMDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Application | Gets the application for this document. |
| Property | Author | Gets or sets the name of the person who authored this document. |
| Property | Comments | Gets or sets the comments for this document. |
| Property | ConfigurationManager | Gets the ConfigurationMgr for this document. |
| Property | CreationDate | Gets the date in string format that this document was created. |
| Property | FullName | Gets the full path and filename of this document. |
| Property | Keywords | Gets or sets the keywords for this document. |
| Property | LastSavedBy | Gets the name of the person who last saved this document. |
| Property | LastSavedDate | Gets the date in string format that this document was last saved. |
| Property | Subject | Gets or sets the subject text for this document. |
| Property | Title | Gets or sets the title for this document. |
| Property | ToolboxPart | Gets or sets whether this file is a SOLIDWORKS Toolbox file. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddCustomProperty | Adds a custom property to document. |
| Method | CloseDoc | Closes the document. |
| Method | DeleteCustomProperty | Deletes the specified custom property from this document. |
| Method | GetAllExternalReferences | Obsolete. Superseded by ISwDMDocument5::GetAllExternalReferences2 . |
| Method | GetCustomProperty | Gets the specified custom property for this document. |
| Method | GetCustomPropertyCount | Gets the number of custom properties for this document. |
| Method | GetCustomPropertyNames | Gets the names of the custom properties for this document. |
| Method | GetEDrawingsData | Obsolete as of SOLIDWORKS Document Manager API 2005 FCS. Not superseded . |
| Method | GetHyperLinkAt | Gets the embedded hyperlinks at the specified index for this document. |
| Method | GetHyperLinksCount | Gets the number of embedded hyperlinks for this document. |
| Method | GetLastUpdateStamp | Gets the date on which this document was last updated. |
| Method | GetVersion | Gets the version of this document. |
| Method | GetXmlStream | Gets the embedded XML data for this assembly and saves it to an XML document. |
| Method | IsDetachedDrawing | Gets whether this file is a detached drawing. |
| Method | ModifyHyperLinkAt | Sets the embedded hyperlink at the specified index for this document. |
| Method | ReplaceReference | Changes all instances of the specified original reference to the specified replacement reference in this document. |
| Method | Save | Saves the document. |
| Method | SaveAs | Saves the document as the specified filename. |
| Method | SetCustomProperty | Obsolete. Superseded by ISwDMDocument29::SetCustomProperty2 . |
| Method | WhereUsed | Gets the names of the files that reference this document using the specified search options. |

[Top](#topBookmark)

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMDocument3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3.html)
[ISwDMDocument4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4.html)
[ISwDMDocument5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5.html)
[ISwDMDocument6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6.html)
[ISwDMDocument7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument7.html)
[ISwDMDocument8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8.html)
[ISwDMDocument10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10.html)
[ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.html)
[ISwDMDocument14 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14.html)
[ISwDMDocument15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15.html)
[ISwDMDocument16 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument16.html)
[ISwDMDocument17 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17.html)
[ISwDMDocument18 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument18.html)
[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.html)
[ISwDMDocument20 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20.html)
[ISwDMDocument21 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument21.html)
[ISwDMDocument22 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22.html)
[ISwDMDocument24 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument24.html)
[ISwDMDocument25 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument25.html)
[ISwDMDocument26 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument26.html)
[ISwDMDocument27 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument27.html)
[ISwDMDocument28 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28.html)
[ISwDMDocument29 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29.html)
[ISwDMDocument30 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument30.html)
