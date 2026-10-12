---
title: "IPDMWDocument Interface Members"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument_members"
member: ""
kind: "members"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html"
---

# IPDMWDocument Interface Members

The following tables list the members exposed by [IPDMWDocument](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Attachments | Gets the non-SOLIDWORKS attachments for this SOLIDWORKS document. |
| Property | Configurations | Gets the configurations available for the specified document and revision. |
| Property | DateModified | Gets the date and time that this document was last modified. |
| Property | Description | Gets the description of the document. |
| Property | ExtReferences | Gets the links to external documents that this document references. |
| Property | ExtWhereUsed | Gets the links to external document that reference this document. |
| Property | HasPDF | Gets whether this drawing document has a PDF file in the vault. |
| Property | IsTopLevel | Gets whether this document is at the top-level project. |
| Property | Name | Gets or sets the name of the document. |
| Property | Notes | Gets the notes associated with this document. |
| Property | Number | Gets the number of this document. |
| Property | Owner | Gets the current owner of this document, which may be different from the author of the document. |
| Property | project | Gets the name of the project to which this document belongs. |
| Property | Properties | Gets the properties of this document. |
| Property | References | Gets the links to the documents referenced by this document. |
| Property | Revision | Gets the revision for this document. |
| Property | RevisionLabels | Gets the next suggested revisions for the document. |
| Property | Revisions | Gets all of the revisions of this document, in order from the oldest to newest. |
| Property | Size | Gets the size (in bytes) of a document smaller than 2GB or the size that represents the 32 low-order bits of a document larger than 2GB. |
| Property | SizeH | Gets the size that represents the 32 high-order bits of a document larger than 2GB. |
| Property | SolidWorksVersion | Gets the SOLIDWORKS version of the document. |
| Property | UpdateStamp | Gets the date on which this document was last updated. |
| Property | WhereUsed | Gets the links to the documents that reference this document. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddNote | Adds a note to the document. |
| Method | BumpRevision | Changes the revision number of the document. |
| Method | ChangeOwner | Changes the document's owner. |
| Method | ChangeProject | Moves the document to the specified project. |
| Method | ChangeStatus | Changes the lifecycle status of the document to the specified lifecycle status. |
| Method | GetDocumentSize | Gets the size (in bytes) of the document. |
| Method | GetEmbeddedEDWAsBase64 | Gets embedded eDrawing data with Base64 encoding, if available. |
| Method | GetStatus | Gets the lifecycle status of the document. |
| Method | ReleaseOwnership | Allows you to release ownership of a document. |
| Method | Save | Copies the document. |
| Method | SaveAsPDF | Gets the PDF file for this drawing document from the vault, if the setting to create a PDF file of a drawing document in the vault during check-in was selected. |
| Method | SaveEmbeddedEDW | Saves the eDrawings embedded in the SOLIDWORKS document, if one exists. |
| Method | TakeOwnership | Allows you to take ownership of a document. |

[Top](#topBookmark)

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[PDMWorks.Interop.pdmworks Namespace](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks_namespace.html)
[IPDMWDocuments Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments.html)
