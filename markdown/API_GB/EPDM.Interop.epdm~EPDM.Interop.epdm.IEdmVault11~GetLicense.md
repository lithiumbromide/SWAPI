---
title: "GetLicense Method (IEdmVault11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault11"
member: "GetLicense"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetLicense.html"
---

# GetLicense Method (IEdmVault11)

Gets all of the SOLIDWORKS PDM Professional licenses installed in this vault.

## Syntax

### Visual Basic

```vb
Sub GetLicense( _
   ByRef ppoRetLicense As EdmLicense() _
)
```

### C#

```csharp
void GetLicense(
   out EdmLicense[] ppoRetLicense
)
```

### C++/CLI

```cpp
void GetLicense(
   [Out] array<EdmLicense> ppoRetLicense
)
```

### Parameters

- `ppoRetLicense`: Array of [EdmLicense](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLicense.html) structures; one structure for each license that has one or more users (see **Remarks**)

## Examples

[Vault Utilities (VB.NET)](Vault_Utilities_Example_VBNET.htm)
[Vault Utilities (C#)](Vault_Utilities_Example_CSharp.htm)

## Remarks

In SOLIDWORKS PDM Professional:

- 2015 SP0 and later, licenses are shared among all vaults that use the same SolidNetwork License Server (SNL). See [IEdmVault14::InstallLicense2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault14~InstallLicense2.html).
- 2014 and earlier, licenses were shared among all vaults that were in the same SQL Server instance.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11.html)
[IEdmVault11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
