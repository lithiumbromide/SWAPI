---
title: "EdmRefItemProperty Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRefItemProperty"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefItemProperty.html"
---

# EdmRefItemProperty Enumeration

Types of property that can be accessed in

[IEdmRefItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem.html)

objects via

[IEdmRefItem::GetProperty](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem~GetProperty.html)

and

[IEdmRefItem::SetProperty](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem~SetProperty.html)

.

## Syntax

### Visual Basic

```vb
Public Enum EdmRefItemProperty
   Inherits System.Enum
```

### C#

```csharp
public enum EdmRefItemProperty : System.Enum
```

### C++/CLI

```cpp
public enum class EdmRefItemProperty : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmrip_CheckAdd | 27 = R+W; Boolean; add file? |
| Edmrip_CheckChangeState | 28 = R+W; Boolean; change the state of the file? |
| Edmrip_CheckCopy | 24 = R+W; Boolean; copy file? |
| Edmrip_CheckGet | 20 = R+W; Boolean; retrieve file? |
| Edmrip_CheckHasBlockingWarning | 30 = R+W; Boolean; file has blocking warning? |
| Edmrip_CheckIncRev | 21 = R+W; Boolean; increment revision? |
| Edmrip_CheckKeepLocked | 19 = R+W; Boolean; keep check-out state after check in? |
| Edmrip_CheckLock | 17 = R+W; Boolean; check out file? |
| Edmrip_CheckOverwriteLatestVersion | 29 = R+W; Boolean; overwrite the latest version of the file with the new changes instead of creating a new version? |
| Edmrip_CheckRemoveLocal | 23 = R+W; Boolean; Check In container; remove local file copy after check in? |
| Edmrip_CheckUndoLock | 22 = R+W; Boolean; Check In container; remove check-out state without producing a new version? |
| Edmrip_CheckUnlock | 18 = R+W; Boolean; Check In container; check in file? |
| Edmrip_FileName | 2 = R; string; All container; filename |
| Edmrip_FoundPath | 7 = R; string; Check In container; file system path to folder where file is found |
| Edmrip_HasReadPermission | 35 = Boolean; Has read permission? |
| Edmrip_ID | 0 = R; string; All container; unique ID of the item in the container |
| Edmrip_IncludedAs | 6 = R; string; Check In container; include path used to reference this file |
| Edmrip_LockComputer | 4 = R; string; Check In container; name of computer where file is checked out |
| Edmrip_LockPath | 3 = R; string; Check In container; file system path to folder where file is checked out |
| Edmrip_LockUser | 5 = R; string; Check In container; name of user who checked out file |
| Edmrip_RefName | 1 = R; string; All container; name of file reference; does not have to be the filename |
| Edmrip_RevisionLatest | 15 = R; string; current revision number of file |
| Edmrip_RevisionNew | 16 = R; string; next revision number of file |
| Edmrip_ShowMultipleWarnings | 31 = R+W; Boolean; display the Multiple Warnings link in the command dialog box's warning column? |
| Edmrip_Size | 33 = R; integer; file size |
| Edmrip_StatusHresult | 25 = R; HRESULT; All container; binary error code for this item |
| Edmrip_StatusText | 26 = R; string; All container; error code |
| Edmrip_TransitionID | 34 = R; integer; Transition ID returned with change state operation |
| Edmrip_Type | 32 = R; integer; Check In container; type of file: 1=normal, 2=virtual, 3=BOM, 4=item, 5=cutlist, 6=toolbox part |
| Edmrip_VersionAttached | 11 = R; integer; Check In container; version that was referenced before check in |
| Edmrip_VersionLatest | 9 = R; integer; Check In container; latest version of the file |
| Edmrip_VersionLocal | 8 = R; integer; Check In container; version of file copy on the local disk |
| Edmrip_VersionNew | 10 = R; integer; Check In container; next version of the file |
| Edmrip_VersionNewAttached | 12 = R; integer; Check In container; version that will be referenced after check in |
| Edmrip_WorkflowStateIcon | 14 = R; string; Check In container; name of the file's current workflow state icon |
| Edmrip_WorkflowStateName | 13 = R; string; Check In container; name of the file's current workflow state |

## Remarks

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
