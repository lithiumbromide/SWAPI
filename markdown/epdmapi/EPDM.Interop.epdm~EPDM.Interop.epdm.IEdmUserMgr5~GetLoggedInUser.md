---
title: "GetLoggedInUser Method (IEdmUserMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr5"
member: "GetLoggedInUser"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetLoggedInUser.html"
---

# GetLoggedInUser Method (IEdmUserMgr5)

Gets the user currently running this program in the vault.

## Syntax

### Visual Basic

```vb
Function GetLoggedInUser() As IEdmUser5
```

### C#

```csharp
IEdmUser5 GetLoggedInUser()
```

### C++/CLI

```cpp
IEdmUser5^ GetLoggedInUser();
```

### Return Value

[IEdmUser5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5.html); current user

## Examples

[Get Messages (C#)](Get_Messages_Example_CSharp.htm)
[Get Messages (VB.NET)](Get_Messages_Example_VBNET.htm)

## Remarks

This method returns the IEdmUser5 interface of the user currently logged in on the [IEdmVault5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html) object from which this IEdmUserMgr5 interface is retrieved. [IEdmUserMgr5::GetFirstLoggedInUserPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetFirstLoggedInUserPosition.html) and [IEdmUserMgr5::GetNextLoggedInUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetNextLoggedInUser.html) return information about all users currently logged in to the vault.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_NOT_LOGGED_IN: Neither [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) nor [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html) has been called.

## See Also

[IEdmUserMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5.html)
[IEdmUserMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
