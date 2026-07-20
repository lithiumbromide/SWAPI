---
title: "IPackAndGo Interface Members"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html"
---

# IPackAndGo Interface Members

The following tables list the members exposed by[IPackAndGo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AddPrefix | Gets or sets a prefix for all filenames for Pack and Go. |
| Property | AddSuffix | Gets or sets a suffix for all filenames for Pack and Go. |
| Property | FlattenToSingleFolder | Gets or sets whether to save all files to the root directory of the Pack and Go destination folder. |
| Property | FolderStructureOption | Gets or sets the folder structure to save to with Pack and Go. |
| Property | IncludeDrawings | Gets or sets whether to add the model's drawing documents to Pack and Go. |
| Property | IncludeSimulationResults | Gets or sets whether to add the model's SOLIDWORKS Simulation results to Pack and Go. |
| Property | IncludeSuppressed | Gets or sets whether to included suppressed components in Pack and Go. |
| Property | IncludeToolboxComponents | Gets or sets whether to include SOLIDWORKS Toolbox components in Pack and Go. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddExternalDocuments | Adds non-SOLIDWORKS files to Pack and Go. |
| Method | GetDocumentNames | Gets the original paths and filenames of all of the model's documents for Pack and Go. |
| Method | GetDocumentNamesCount | Gets the number of documents comprising the model for Pack and Go. |
| Method | GetDocumentSaveToNames | Gets the paths and filenames to which to save the model's documents for Pack and Go set by IPackAndGo::SetDocumentSaveToNames . |
| Method | GetExternalDocuments | Gets the paths and filenames of the non-SOLIDWORKS files added to Pack And Go. |
| Method | GetSaveToName | Gets the path or the path and filename of the Zip file for Pack and Go set by IPackAndGo::SetSaveToName . |
| Method | IGetDocumentNames | Gets the original paths and filenames of all of the model's documents for Pack and Go. |
| Method | IGetDocumentSaveToNames | Gets the paths and filenames to which to save the model's documents for Pack and Go set by IPackAndGo::ISetDocumentSaveToNames . |
| Method | ISetDocumentSaveToNames | Sets the paths and filenames of the documents to save in Pack and Go. |
| Method | RemoveExternalDocuments | Removes the specified non-SOLIDWORKS files from Pack and Go. |
| Method | SetDocumentSaveToNames | Sets the paths and filenames of the documents for Pack and Go. |
| Method | SetSaveToName | Obsolete. Superseded by IPackAndGo::SetSaveToName2 . |
| Method | SetSaveToName2 | Overrides the paths and filenames of the documents set by IPackAndGo::SetDocumentSaveToNames or IPackAndGo::ISetDocumentSaveToNames with the specified path or the path and name of the Zip file. |

[Top](#topBookmark)

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
