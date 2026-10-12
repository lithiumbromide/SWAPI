---
title: "LoginAuto Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "LoginAuto"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html"
---

# LoginAuto Method (IEdmVault5)

Logs in to the specified vault.

## Syntax

### Visual Basic

```vb
Sub LoginAuto( _
   ByVal bsVaultName As System.String, _
   ByVal hParentWnd As System.Integer _
)
```

### C#

```csharp
void LoginAuto(
   System.string bsVaultName,
   System.int hParentWnd
)
```

### C++/CLI

```cpp
void LoginAuto(
   System.String^ bsVaultName,
   System.int hParentWnd
)
```

### Parameters

- `bsVaultName`: Vault name
- `hParentWnd`: Parent window handle; used when the login dialog box displays to ensure it remains visible

## Examples

See the [IEdmVault5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html) examples.

## Remarks

This method differs from [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) in that this method does not require the username and password. This method logs into the vault as the same user that is already logged into either the vault view through File Explorer or the vault through the SOLIDWORKS PDM Professional client software. This method allows you to share the license of the already logged-in user. If no user is already logged into the specified file vault, a login dialog box displays. Also unlike IEdmVault5::Login, this method properly consumes a license without first calling [IEdmVault13::LoginEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault13~LoginEx.html) to comply with the [SOLIDWORKS End User License Agreement (EULA)](http://www.solidworks.com/sw/eula.htm).

You can retrieve the ID of the SOLIDWORKS PDM Professional client user by calling [IEdmVault11::GetLoggedInWindowsUserID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetLoggedInWindowsUserID.html). You can also log in silently as the SOLIDWORKS PDM Professional client by calling [IEdmVault11::LogInWindowsUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~LogInWindowsUser.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_ALREADY_LOGGED_IN: You are already logged in to this vault.
- E_EDM_CANT_OPEN_DATABASE: The database could not be opened (Maybe the vault name was incorrect?).
- E_EDM_CANCELLED_BY_USER: The log-in dialog box displays, but the user clicked **Cancel** instead of logging in.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
