---
title: "IEdmFolder5 Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5_members"
member: ""
kind: "members"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html"
---

# IEdmFolder5 Interface Members

The following tables list the members exposed by [IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ID | Gets the database ID of this folder. |
| Property | LocalPath | Gets the full file system path to this local folder. |
| Property | Name | Gets the name of the folder. |
| Property | ObjectType | Gets the type of object. |
| Property | ParentFolder | Gets the interface to the parent folder of this folder. |
| Property | Vault | Gets the file vault to which this folder belongs. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddFile | Obsolete. Superseded by IEdmFolder8::AddFile2 . |
| Method | AddFileShared | Shares a file in another folder with this folder. |
| Method | AddFolder | Creates a subfolder in this folder. |
| Method | CopyFile | Obsolete. Superseded by IEdmFolder8::CopyFile2 . |
| Method | CreateCardView | Obsolete. Superseded by IEdmFolder10::CreateCardView2 . |
| Method | CreateFolderPath | Creates all subfolders in a path relative to this folder. |
| Method | CreateLabel | Creates a label on this folder and its subfolders. |
| Method | DeleteFile | Deletes a file having the specified ID from this folder. |
| Method | DeleteFolder | Deletes the specified subfolder from this folder. |
| Method | GetCard | Gets the interface to a data card of a file of the specified file type or the interface to the data card of this folder. |
| Method | GetCardID | Gets the ID of the data card of a file with the specified extension or the ID of the data card of this folder. |
| Method | GetFile | Gets the interface to a file with the specified name in this folder. |
| Method | GetFirstFilePosition | Starts an enumeration of the files in this folder. |
| Method | GetFirstLabelPosition | Starts an enumeration of the labels in this folder. |
| Method | GetFirstSubFolderPosition | Starts an enumeration of the subfolders in this folder. |
| Method | GetNextFile | Gets the next file in the enumeration. |
| Method | GetNextLabel | Gets the next label in the enumeration. |
| Method | GetNextSubFolder | Gets the next subfolder in the enumeration. |
| Method | GetSubFolder | Gets the interface to the subfolder with the specified name. |
| Method | HasRights | Obsolete. Superseded by IEdmFolder5::HasRightsEx . |
| Method | HasRightsEx | Gets whether the user has the specified rights for the specified file in this folder. |
| Method | IsKindOf | Checks whether the object is of a certain type. |
| Method | Refresh | Refreshes the file listing for the folder. |

[Top](#topBookmark)

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
