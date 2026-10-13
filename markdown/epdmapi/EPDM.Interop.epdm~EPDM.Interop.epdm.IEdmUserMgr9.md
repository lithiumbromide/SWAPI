---
title: "IEdmUserMgr9 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr9"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9.html"
---

# IEdmUserMgr9 Interface

Allows you to access the users and user groups in the vault.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmUserMgr9
   Inherits IEdmUserMgr5, IEdmUserMgr6, IEdmUserMgr7, IEdmUserMgr8
```

### C#

```csharp
public interface IEdmUserMgr9 : IEdmUserMgr5, IEdmUserMgr6, IEdmUserMgr7, IEdmUserMgr8
```

### C++/CLI

```cpp
public interface class IEdmUserMgr9 : public IEdmUserMgr5, IEdmUserMgr6, IEdmUserMgr7, IEdmUserMgr8
```

## Examples

[Traverse Users and Groups in Vault (VB.NET)](Traverse_Users_and_Groups_in_Vault_Example_VBNET.htm)
[Traverse Users and Groups in Vault (C#)](Traverse_Users_and_Groups_in_Vault_Example_CSharp.htm)

## Remarks

This interface:

- extends [IEdmUserMgr8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8.html) by providing the ability to get and set the state and transition permissions for users and groups.
- is extended by [IEdmUserMgr10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr10.html).

## See Also

[IEdmUserMgr9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
