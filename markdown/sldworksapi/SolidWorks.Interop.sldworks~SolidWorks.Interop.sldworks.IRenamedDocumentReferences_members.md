---
title: "IRenamedDocumentReferences Interface Members"
project: "SOLIDWORKS API Help"
interface: "IRenamedDocumentReferences_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.html"
---

# IRenamedDocumentReferences Interface Members

The following tables list the members exposed by [IRenamedDocumentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CompletionAction | Gets or sets whether to update references to the renamed file in unopened documents. |
| Property | IncludeFileLocations | Gets or sets whether to search the folders listed under Referenced Documents in Tools > Options > System Options > File Locations . |
| Property | UpdateWhereUsedReferences | Gets or sets whether to update the references to the new file name. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddSearchFolder | Adds the specified folder in which to search for documents whose references to update. |
| Method | GetSearchPath | Gets the folders to search. |
| Method | ReferencesArray | Gets the pathnames of the documents with references to this renamed document. |
| Method | RemoveReference | Removes the specified reference from the list of references to update. |
| Method | RemoveSearchFolder | Removes the specified folder in which to search for documents whose references to update. |
| Method | Search | Searches for documents whose references to update. |

[Top](#topBookmark)

## See Also

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDocExtension::HasRenamedDocuments Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasRenamedDocuments.html)
[IModelDocExtension::RenameDocument Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDocument.html)
