---
title: "GetUserGroup Method (IEdmUserMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr5"
member: "GetUserGroup"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetUserGroup.html"
---

# GetUserGroup Method (IEdmUserMgr5)

Gets a user group with the specified name or ID.

## Syntax

### Visual Basic

```vb
Function GetUserGroup( _
   ByRef poIdOrName As System.Object _
) As IEdmUserGroup5
```

### C#

```csharp
IEdmUserGroup5 GetUserGroup(
   ref System.object poIdOrName
)
```

### C++/CLI

```cpp
IEdmUserGroup5^ GetUserGroup(
   System.Object^% poIdOrName
)
```

### Parameters

- `poIdOrName`: ID or name of the user group to get

### Return Value

[IEdmUserGroup5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5.html)

## Examples

[Traverse Users and Groups in Vault (C#)](Traverse_Users_and_Groups_in_Vault_Example_CSharp.htm)
[Traverse Users and Groups in Vault (VB.NET)](Traverse_Users_and_Groups_in_Vault_Example_VBNET.htm)
[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)
[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm)

## Remarks

C++ users must release the returned interface, IEdmUserGroup5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The poIdOrName argument contains an unknown user group name. The return value contains null when this happens in C++.
- E_EDM_INVALID_ID: The poIdOrName argument contains an invalid ID.
- E_EDM_DATABASE_ACCESS: Returned only for invalid IDs in SOLIDWORKS PDM Professional 5.2.

## See Also

[IEdmUserMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5.html)
[IEdmUserMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
