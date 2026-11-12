---
title: "LogInWindowsUser Method (IEdmVault11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault11"
member: "LogInWindowsUser"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~LogInWindowsUser.html"
---

# LogInWindowsUser Method (IEdmVault11)

Logs into SOLIDWORKS PDM Professional as the specified user.

## Syntax

### Visual Basic

```vb
Sub LogInWindowsUser( _
   ByVal bsUserName As System.String, _
   ByVal bsPasswd As System.String, _
   ByVal bsVaultName As System.String _
)
```

### C#

```csharp
void LogInWindowsUser(
   System.string bsUserName,
   System.string bsPasswd,
   System.string bsVaultName
)
```

### C++/CLI

```cpp
void LogInWindowsUser(
   System.String^ bsUserName,
   System.String^ bsPasswd,
   System.String^ bsVaultName
)
```

### Parameters

- `bsUserName`: User name
- `bsPasswd`: Password for bsUserName
- `bsVaultName`: Name of vault to which to log in

## Remarks

This method works like [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html), except this method does not display a login dialog box.

Any number of users can log in through the API, as long as they use the [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) method. However, only one user at a time can log in through the SOLIDWORKS PDM Professional client user interface. Both [IEdmVault11::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~LogInWindowsUser.html) and IEdmVault11::LogInWindowsUser log in the single user of the client user interface.

Call [IEdmVault11::GetLoggedInWindowsUserID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetLoggedInWindowsUserID.html) to obtain the ID of the user who is currently logged in through the client user interface.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_LOGIN_FAILED: The specified user name or password is incorrect.
- E_EDM_ALREADY_LOGGED_IN: Someone is already logged in from this client machine's user interface, or the IEdmVault object is already connected.

## See Also

[IEdmVault11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11.html)
[IEdmVault11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
