---
title: "InstallLicense2 Method (IEdmVault14)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault14"
member: "InstallLicense2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault14~InstallLicense2.html"
---

# InstallLicense2 Method (IEdmVault14)

Installs a SOLIDWORKS PDM Professional license for this vault.

## Syntax

### Visual Basic

```vb
Sub InstallLicense2( _
   ByVal brUserName As System.String, _
   ByVal bsPasswd As System.String, _
   ByVal bsVaultName As System.String, _
   ByVal bsSNLServers As System.String _
)
```

### C#

```csharp
void InstallLicense2(
   System.string brUserName,
   System.string bsPasswd,
   System.string bsVaultName,
   System.string bsSNLServers
)
```

### C++/CLI

```cpp
void InstallLicense2(
   System.String^ brUserName,
   System.String^ bsPasswd,
   System.String^ bsVaultName,
   System.String^ bsSNLServers
)
```

### Parameters

- `brUserName`: Name of a SOLIDWORKS PDM Professional user
- `bsPasswd`: Password for bsUserName
- `bsVaultName`: Name of vault for which to install a license
- `bsSNLServers`: Names of the port and server of the SolidNetwork License (SNL) server; for example, 25734@myserver

## Remarks

In SOLIDWORKS PDM Professional:

- 2015 SP0 and later, licenses are shared among all vaults that use the same SolidNetwork License Server (SNL).
- 2014 and earlier, licenses were shared among all vaults that were in the same SQL Server instance.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault14 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault14.html)
[IEdmVault14 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault14_members.html)
[IEdmVault11::GetLicense Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetLicense.html)

## Availability

SOLIDWORKS PDM Professional 2015
