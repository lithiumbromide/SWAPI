---
title: "IEdmUser5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUser5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5.html"
---

# IEdmUser5 Interface

Allows you to access a user in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmUser5
   Inherits IEdmObject5
```

### C#

```csharp
public interface IEdmUser5 : IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmUser5 : public IEdmObject5
```

## Examples

[Get and Set Folder Permissions (VB.NET)](Get_and_Set_Folder_Permissions_Example_VBNET.htm)
[Get and Set Folder Permissions (C#)](Get_and_Set_Folder_Permissions_Example_CSharp.htm)
[Traverse Users and Groups in Vault (C#)](Traverse_Users_and_Groups_in_Vault_Example_CSharp.htm)
[Traverse Users and Groups in Vault (VB.NET)](Traverse_Users_and_Groups_in_Vault_Example_VBNET.htm)

## Remarks

This interface:

- inherits from [IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html).
- is extended by [IEdmUser6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser6.html).

To enumerate:

- the users in a file vault, use [IEdmUserMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5.html).
- the messages sent to a user, cast this interface to an [IEdmInbox5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmInbox5.html) pointer.

## Accessors

[IEdmFile5::LockedByUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~LockedByUser.html)

[IEdmLabel5::User](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~User.html)

[IEdmReference5::LockedByUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~LockedByUser.html)

[IEdmRevision5::User](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5~User.html)

[IEdmUserGroup5::GetNextUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~GetNextUser.html)

[IEdmUserMgr5::GetLoggedInUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetLoggedInUser.html)

[IEdmUserMgr5::GetNextUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetNextUser.html)

[IEdmUserMgr5::GetUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetUser.html)

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)

## See Also

[IEdmUser5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
