---
title: "GetLoggedInWindowsUserID Method (IEdmVault11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault11"
member: "GetLoggedInWindowsUserID"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetLoggedInWindowsUserID.html"
---

# GetLoggedInWindowsUserID Method (IEdmVault11)

Gets the ID of the user who is currently logged in through the SOLIDWORKS PDM Professional client software on this machine.

## Syntax

### Visual Basic

```vb
Function GetLoggedInWindowsUserID( _
   ByVal bsVault As System.String _
) As System.Integer
```

### C#

```csharp
System.int GetLoggedInWindowsUserID(
   System.string bsVault
)
```

### C++/CLI

```cpp
System.int GetLoggedInWindowsUserID(
   System.String^ bsVault
)
```

### Parameters

- `bsVault`: Name of the vault for which to get the logged-in user

### Return Value

ID of the logged-in user; 0 if no one is logged in

## Remarks

Any number of users can be logged into a vault at the same time by calling [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html). However, only a single user can be logged into a machine either through the SOLIDWORKS PDM Professional client software or by calling [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html). This is the user for whom this method returns an ID.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11.html)
[IEdmVault11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
