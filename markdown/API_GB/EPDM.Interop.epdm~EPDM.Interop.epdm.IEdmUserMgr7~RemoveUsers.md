---
title: "RemoveUsers Method (IEdmUserMgr7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr7"
member: "RemoveUsers"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~RemoveUsers.html"
---

# RemoveUsers Method (IEdmUserMgr7)

Removes the specified users from the vault.

## Syntax

### Visual Basic

```vb
Sub RemoveUsers( _
   ByVal poUserIDs() As System.Integer _
)
```

### C#

```csharp
void RemoveUsers(
   System.int[] poUserIDs
)
```

### C++/CLI

```cpp
void RemoveUsers(
   System.array<int>^ poUserIDs
)
```

### Parameters

- `poUserIDs`: Array of IDs of the users to remove (see **Remarks**)

## Examples

[Vault Utilities (VB.NET)](Vault_Utilities_Example_VBNET.htm)
[Vault Utilities (C#)](Vault_Utilities_Example_CSharp.htm)
[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)
[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm)

## Remarks

If you specify an ID in poUserIDs that does not exist, it is ignored.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The logged-in user lacks the [EdmSysPerm](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysPerm.html).EdmSysPerm_EditUserMgr permission.

## See Also

[IEdmUserMgr7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7.html)
[IEdmUserMgr7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
