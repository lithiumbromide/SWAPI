---
title: "Login Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "Login"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html"
---

# Login Method (IEdmVault5)

Logs in to the specified vault using the specified user name and password.

## Syntax

### Visual Basic

```vb
Sub Login( _
   ByVal bsUserName As System.String, _
   ByVal bsPasswd As System.String, _
   ByVal bsVaultName As System.String _
)
```

### C#

```csharp
void Login(
   System.string bsUserName,
   System.string bsPasswd,
   System.string bsVaultName
)
```

### C++/CLI

```cpp
void Login(
   System.String^ bsUserName,
   System.String^ bsPasswd,
   System.String^ bsVaultName
)
```

### Parameters

- `bsUserName`: User name of user created in the SOLIDWORKS PDM Professional User Manager
- `bsPasswd`: Password for bsUserName
- `bsVaultName`: Vault name

## Remarks

If your application is custom (i.e., it is not supplied or supported by SOLIDWORKS PDM Professional) and your application:

- logs into SOLIDWORKS PDM Professional
  - or -
- logs into a vault view
  - or -
- directly accesses a vault database

when the same user is not already logged into a local view, you must first call [IEdmVault13::LoginEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault13~LoginEx.html) or [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html) to comply with the [SOLIDWORKS End User License Agreement (EULA)](http://www.solidworks.com/sw/eula.htm). Call IEdmVault13::LoginEx or IEdmVault5::LoginAuto before calling this method to ensure that licenses are properly consumed by your application.

Call IEdmVault5::LoginAuto to log in as a user already logged into a vault view through File Explorer or into a vault through the SOLIDWORKS PDM Professional client software. You do not need to specify a username and password when you call IEdmVault5::LoginAuto to share a license with the already logged-in user.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_ALREADY_LOGGED_IN: You are already logged into this vault.
- E_EDM_LOGIN_FAILED: You entered an invalid user name or password.
- E_EDM_CANT_OPEN_DATABASE: The database could not be opened.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
