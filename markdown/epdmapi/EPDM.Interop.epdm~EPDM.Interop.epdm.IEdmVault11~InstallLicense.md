---
title: "InstallLicense Method (IEdmVault11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault11"
member: "InstallLicense"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~InstallLicense.html"
---

# InstallLicense Method (IEdmVault11)

Obsolete. Replaced by [IEdmVault14::InstallLicense2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault14~InstallLicense2.html).

## Syntax

### Visual Basic

```vb
Sub InstallLicense( _
   ByVal bsUserName As System.String, _
   ByVal bsPasswd As System.String, _
   ByVal bsVaultName As System.String, _
   ByVal bsLicenseFilePath As System.String _
)
```

### C#

```csharp
void InstallLicense(
   System.string bsUserName,
   System.string bsPasswd,
   System.string bsVaultName,
   System.string bsLicenseFilePath
)
```

### C++/CLI

```cpp
void InstallLicense(
   System.String^ bsUserName,
   System.String^ bsPasswd,
   System.String^ bsVaultName,
   System.String^ bsLicenseFilePath
)
```

### Parameters

- `bsUserName`: Name of a SOLIDWORKS PDM Professional user
- `bsPasswd`: Password for bsUserName
- `bsVaultName`: Name of vault for which to install a license
- `bsLicenseFilePath`: Path to the license file

## Remarks

In SOLIDWORKS PDM Professional 2014 and earlier, licenses were shared among all vaults that were in the same SQL Server instance. Because licenses are shared among all vaults that use the same SolidNetwork License Server (SNL) in SOLIDWORKS PDM Professional 2015 SP0 and later, this method is obsolete and replaced by [IEdmVault14::InstallLicense2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault14~InstallLicense2.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11.html)
[IEdmVault11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
