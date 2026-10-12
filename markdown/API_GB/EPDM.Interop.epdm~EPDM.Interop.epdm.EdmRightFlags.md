---
title: "EdmRightFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRightFlags"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRightFlags.html"
---

# EdmRightFlags Enumeration

Flags used in calls to [IEdmFolder5::HasRights](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~HasRights.html) and [IEdmFolder5::HasRightsEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~HasRightsEx.html) to check user rights. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmRightFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmRightFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmRightFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmRight_Add | 8 = Permission to add files |
| EdmRight_AddFolder | 64 = Permission to create subfolders |
| EdmRight_All | -1 or 0xffffffff = Complete set of rights NOTE : Do not use this constant in rights checking, because more flags might be added in the future. Instead, explicitly specify the rights bits. |
| EdmRight_BomActivate | 1024 = Activate computed BOM |
| EdmRight_ChangeCard | 65536 = Permission to change the contents of a file/folder data card |
| EdmRight_ColdStoreRestore | 524288 = Restore file from cold storage |
| EdmRight_Delete | 4 = Permission to delete files |
| EdmRight_DeleteFolder | 64 = Permission to delete subfolders |
| EdmRight_DestroyTrash | 256 = Destroy |
| EdmRight_EditFolderCard | 512 = Edit folder card data |
| EdmRight_EditVerFreeVarData | 1048576 = Edit version free variable data |
| EdmRight_IncrementRevision | 32 = Permission to increment revision on files |
| EdmRight_Lock | 2 = Permission to check out files |
| EdmRight_MandatoryVersionComments | 67108864 |
| EdmRight_MaySeeComputedBOM | 2048 = See computed BOM |
| EdmRight_MoveFile | 2097152 = Permission to move files |
| EdmRight_MoveFolder | 8388608 = Permission to move folders |
| EdmRight_None | 0 = No rights at all; used internally |
| EdmRight_OverwriteLatestVersion | 33554432 = Overwrite latest version |
| EdmRight_PrivateState | 4194304 = Permission to make state private |
| EdmRight_Read | 1 = Permission to read files |
| EdmRight_RecoverTrash | 128 = Recover files from the recycle bin |
| EdmRight_Rename | 8 = Permission to rename files |
| EdmRight_RenameFolder | 16777216 = Permission to rename folders |
| EdmRight_Rollback | 262144 = Can run the rollback command in the history dialog box |
| EdmRight_Share | 16 = Permission to share files |
| EdmRight_ShowWorkingVersion | 131072 = Permission to see working versions, not just revisions |

## Examples

[Get and Set Folder Permissions (VB.NET)](Get_and_Set_Folder_Permissions_Example_VBNET.htm)
[Get and Set Folder Permissions (C#)](Get_and_Set_Folder_Permissions_Example_CSharp.htm)

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
