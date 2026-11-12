---
title: "IEdmLabel5 Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel5_members"
member: ""
kind: "members"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5_members.html"
---

# IEdmLabel5 Interface Members

The following tables list the members exposed by [IEdmLabel5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Comment | Gets the label comment. |
| Property | Time | Gets the date and time of label creation. |
| Property | User | Gets the user who created the label. |
| Property | UserID | Gets the ID of the user who created the label. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddFile | Sets this label on the latest version of the specified file. |
| Method | AddFolder | Sets this label on the specified folder and all of the files in that folder. |
| Method | GetFirstFilePosition | Starts an enumeration of the files set with this label. |
| Method | GetFirstFolderPosition | Starts an enumeration of the folders set with this label. |
| Method | GetNextFile | Gets the next file with this label in the enumeration. |
| Method | GetNextFileID | Gets the next ID of a file with this label in the enumeration. |
| Method | GetNextFolder | Gets the next folder with this label in the enumeration. |
| Method | GetNextFolderID | Gets the next ID of a folder with this label in the enumeration. |
| Method | GetVersionNo | Gets the version of the specified file on which this label is set. |

[Top](#topBookmark)

## See Also

[IEdmLabel5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmFile16::CreateLabel Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile16~CreateLabel.html)
[IEdmFolder5::CreateLabel Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateLabel.html)
