---
title: "IEdmFindUser Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFindUser"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser.html"
---

# IEdmFindUser Interface

Allows you to search for users in the vault.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFindUser
```

### C#

```csharp
public interface IEdmFindUser
```

### C++/CLI

```cpp
public interface class IEdmFindUser
```

## Examples

[Find Users (VB.NET)](Find_Users_Example_VBNET.htm)
[Find Users (C#)](Find_Users_Example_CSharp.htm)

## Remarks

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

To access this interface, call [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html) with eType set to [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_FindUser.

SOLIDWORKS PDM Professional uses this interface internally when you have linked a card button to the **Find User** command.

This interface provides for both silent and interactive searches of users. Interactive searches display the same user interface that SOLIDWORKS PDM Professional displays when searching the vault for users.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmFindUser Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
