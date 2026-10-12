---
title: "IEdmFile5 Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5_members"
member: ""
kind: "members"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html"
---

# IEdmFile5 Interface Members

The following tables list the members exposed by [IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CurrentRevision | Gets the file's current revision. |
| Property | CurrentState | Gets the file's current workflow state. |
| Property | CurrentVersion | Gets the file's current version number. |
| Property | ID | Gets the database ID of this file. |
| Property | IsLocked | Gets whether the file is checked out. |
| Property | LockedByUser | Gets the user who has the file checked out. |
| Property | LockedByUserID | Gets the ID of the user who has the file checked out. |
| Property | LockedInFolder | Gets the folder in which this file is checked out. |
| Property | LockedInFolderID | Gets the ID of the folder in which this file is checked out. |
| Property | LockedOnComputer | Gets the name of the computer to which the file is checked out. |
| Property | LockPath | Gets the full path to the checked-out file. |
| Property | Name | Gets the name of the file. |
| Property | ObjectType | Gets the type of object. |
| Property | Vault | Gets the file vault to which this file belongs. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ChangeState | Obsolete. Superseded by IEdmFile10::ChangeState2 . |
| Method | GetConfigurations | Gets a list of names of the configurations for the specified version of this file. |
| Method | GetEnumeratorVariable | Gets an interface to this file's data card variables. |
| Method | GetFileCopy | Gets a copy of the file with the specified version from the archive and deposits it in the specified location. |
| Method | GetFirstFolderPosition | Starts an enumeration of the parent folders of this file. |
| Method | GetLocalFileDate | Gets the date and timestamp of a local copy of this file. |
| Method | GetLocalFileSize | Obsolete. Superseded by IEdmFile9::GetLocalFileSize2 . |
| Method | GetLocalPath | Gets the full path to this file in the specified parent folder. |
| Method | GetLocalRevisionName | Gets the revision name of the local copy of this file. |
| Method | GetLocalVersionNo | Obsolete. Superseded by IEdmFile12::GetLocalVersionNo2 . |
| Method | GetNextFolder | Gets the next parent folder of this file. |
| Method | GetReferenceTree | Gets an interface to the files that reference or are referenced by this file. |
| Method | GetRevisionGeneratorInfo | Gets information about this file for the revision generator. |
| Method | IncrementRevision | Creates a new revision of this file. |
| Method | IsKindOf | Checks whether the object is of a certain type. |
| Method | LockFile | Checks out this file from the vault to which the user is currently logged in. |
| Method | Refresh | Refreshes the file. |
| Method | Rename | Obsolete. Superseded by IEdmFile6::RenameEx . |
| Method | UndoLockFile | Removes the check-out of a file without saving changes to the archive. |
| Method | UnlockFile | Checks in this file. |

[Top](#topBookmark)

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
