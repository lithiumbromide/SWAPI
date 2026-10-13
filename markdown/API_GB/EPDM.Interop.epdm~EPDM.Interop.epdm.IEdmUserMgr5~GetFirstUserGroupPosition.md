---
title: "GetFirstUserGroupPosition Method (IEdmUserMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr5"
member: "GetFirstUserGroupPosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetFirstUserGroupPosition.html"
---

# GetFirstUserGroupPosition Method (IEdmUserMgr5)

Starts an enumeration of the user groups in the vault.

## Syntax

### Visual Basic

```vb
Function GetFirstUserGroupPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstUserGroupPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstUserGroupPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first user group in the enumeration

## Examples

[Get and Set Folder Permissions (VB.NET)](Get_and_Set_Folder_Permissions_Example_VBNET.htm)
[Get and Set Folder Permissions (C#)](Get_and_Set_Folder_Permissions_Example_CSharp.htm)
[Traverse Users and Groups in Vault (C#)](Traverse_Users_and_Groups_in_Vault_Example_CSharp.htm)
[Traverse Users and Groups in Vault (VB.NET)](Traverse_Users_and_Groups_in_Vault_Example_VBNET.htm)

## Remarks

After calling this method, pass the returned position of the first user group to [IEdmUserMgr5::GetNextUserGroup](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetNextUserGroup.html) to get the first user group in this list. Then call IEdmUserMgr5::GetNextUserGroup repeatedly to get the rest of the user groups.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5.html)
[IEdmUserMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
