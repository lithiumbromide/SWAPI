---
title: "IEdmSearch5 Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch5_members"
member: ""
kind: "members"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5_members.html"
---

# IEdmSearch5 Interface Members

The following tables list the members exposed by [IEdmSearch5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | FileName | Gets or sets the name of the file or folder for which to search. |
| Property | FindFiles | Gets or sets whether to return files in the search. |
| Property | FindFolders | Gets or sets whether to return folders in the search. |
| Property | FindHistoricStates | Gets or sets whether to find all files that have ever been in the state specified by IEdmSearch5::State . |
| Property | FindLockedFiles | Gets or sets whether to include checked-out files in the search result. |
| Property | FindUnlockedFiles | Gets or sets whether to include checked-in files in the search result. |
| Property | Recursive | Gets or sets whether to search recursively in subfolders. |
| Property | StartFolderID | Gets or sets the ID of the folder in which to search. |
| Property | State | Gets or sets the ID or name of the workflow state in which to search. |
| Property | VersionComment | Gets or sets the version comment substring for which to search. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddVariable | Obsolete. Superseded by IEdmSearch8::AddVariable2 . |
| Method | Clear | Resets all search properties to their default values |
| Method | GetFirstResult | Gets the first file or folder that matches the search criteria. |
| Method | GetNextResult | Gets the next file or folder that matches the search criteria. |

[Top](#topBookmark)

## See Also

[IEdmSearch5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
