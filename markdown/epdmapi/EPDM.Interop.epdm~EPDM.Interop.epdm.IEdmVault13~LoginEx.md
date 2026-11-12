---
title: "LoginEx Method (IEdmVault13)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault13"
member: "LoginEx"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault13~LoginEx.html"
---

# LoginEx Method (IEdmVault13)

Allows an application that is not supplied and supported by SOLIDWORKS Corporation to:

- log into SOLIDWORKS PDM Professional
  - or -
- log into a vault view
  - or -
- directly access the vault database

when the same user is not already logged into a local view.

## Syntax

### Visual Basic

```vb
Sub LoginEx( _
   ByVal bsUserName As System.String, _
   ByVal bsPasswd As System.String, _
   ByVal bsVaultName As System.String, _
   Optional ByVal lEdmLoginFlags As System.Integer _
)
```

### C#

```csharp
void LoginEx(
   System.string bsUserName,
   System.string bsPasswd,
   System.string bsVaultName,
   System.int lEdmLoginFlags
)
```

### C++/CLI

```cpp
void LoginEx(
   System.String^ bsUserName,
   System.String^ bsPasswd,
   System.String^ bsVaultName,
   System.int lEdmLoginFlags
)
```

### Parameters

- `bsUserName`: User name of user created in the SOLIDWORKS PDM Professional User Manager
- `bsPasswd`: User password for bsUserName
- `bsVaultName`: Name of vault
- `lEdmLoginFlags`: Login flags:

  - 0 = Nothing
  - 1 = Web client

## Remarks

To make it easier to program and to comply with the [SOLIDWORKS End User License Agreement (EULA)](http://www.solidworks.com/sw/eula.htm), this method ensures that licenses are properly consumed by your application.

## See Also

[IEdmVault13 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault13.html)
[IEdmVault13 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault13_members.html)
[IEdmVault5::Login Method()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html)
[IEdmVault5::LoginAuto Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html)

## Availability

SOLIDWORKS PDM Professional 2014
