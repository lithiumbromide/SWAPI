---
title: "IEdmUserGroup5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserGroup5"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5.html"
---

# IEdmUserGroup5 Interface

Allows you to access a user group in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmUserGroup5
   Inherits IEdmObject5
```

### C#

```csharp
public interface IEdmUserGroup5 : IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmUserGroup5 : public IEdmObject5
```

## Examples

[Get and Set Folder Permissions (VB.NET)](Get_and_Set_Folder_Permissions_Example_VBNET.htm)
[Get and Set Folder Permissions (C#)](Get_and_Set_Folder_Permissions_Example_CSharp.htm)
[Traverse Users and Groups in Vault (C#)](Traverse_Users_and_Groups_in_Vault_Example_CSharp.htm)
[Traverse Users and Groups in Vault (VB.NET)](Traverse_Users_and_Groups_in_Vault_Example_VBNET.htm)

## Remarks

This interface:

- inherits from [IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html).
- is extended by [IEdmUserGroup6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup6.html).

User groups are set up using SOLIDWORKS PDM Professional's User Manager.

Use [IEdmUserMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5.html) to enumerate the user groups in the vault.

## Accessors

[IEdmUserMgr5::GetNextUserGroup](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetNextUserGroup.html)

[IEdmUserMgr5::GetUserGroup](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetUserGroup.html)

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)

## See Also

[IEdmUserGroup5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmUser5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5.html)
