---
title: "IEdmReference5 Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference5_members"
member: ""
kind: "members"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5_members.html"
---

# IEdmReference5 Interface Members

The following tables list the members exposed by [IEdmReference5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | File | Gets the file. |
| Property | FileID | Gets the ID of the file. |
| Property | Folder | Gets the file's parent folder. |
| Property | FolderID | Gets the ID of the file's parent folder. |
| Property | FoundPath | Gets the file system path where the file was found. |
| Property | IsLocked | Gets whether the file is checked out. |
| Property | LockedByUser | Gets the the user who checked out the file. |
| Property | LockedInFolder | Gets the folder in which the file is checked out. |
| Property | LockedOnComputer | Gets the name of the computer on which the file is checked out. |
| Property | LockPath | Gets the file's check-out path. |
| Property | Name | Gets the name of the file. |
| Property | ReferencedAs | Gets how the file is included by the referencing file. |
| Property | VersionLocal | Gets the local version number of the file. |
| Property | VersionRef | Gets the referenced version number of the file. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetCustomData | Gets data stored with IEdmReference5::SetCustomData in this file reference. |
| Method | GetFirstChildPosition | Obsolete. Superseded by IEdmReference7::GetFirstChildPosition2 . |
| Method | GetFirstParentPosition | Obsolete. Superseded by IEdmReference7::GetFirstParentPosition2 . |
| Method | GetNextChild | Enumerates the files referenced by this file. |
| Method | GetNextParent | Enumerates the files referencing this file. |
| Method | SetCustomData | Stores an arbitrary piece of data in this object. |

[Top](#topBookmark)

## See Also

[IEdmReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmReference7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7.html)
[IEdmReference8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference8.html)
[IEdmReference9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference9.html)
