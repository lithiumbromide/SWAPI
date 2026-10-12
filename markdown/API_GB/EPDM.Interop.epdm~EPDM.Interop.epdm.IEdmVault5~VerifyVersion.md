---
title: "VerifyVersion Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "VerifyVersion"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~VerifyVersion.html"
---

# VerifyVersion Method (IEdmVault5)

Verifies that the installed SOLIDWORKS PDM Professional is at the specified version level or higher.

## Syntax

### Visual Basic

```vb
Sub VerifyVersion( _
   ByVal lMajor As System.Integer, _
   ByVal lMinor As System.Integer _
)
```

### C#

```csharp
void VerifyVersion(
   System.int lMajor,
   System.int lMinor
)
```

### C++/CLI

```cpp
void VerifyVersion(
   System.int lMajor,
   System.int lMinor
)
```

### Parameters

- `lMajor`: Minimum major version number
- `lMinor`: Minimum minor version number

## Examples

[Vault Utilities (VB.NET)](Vault_Utilities_Example_VBNET.htm)
[Vault Utilities (C#)](Vault_Utilities_Example_CSharp.htm)

## Remarks

Add-ins that depend on a specific SOLIDWORKS PDM Professional version should make themselves impossible to install on earlier versions of SOLIDWORKS PDM Professional. To do this, set the minimum version of SOLIDWORKS PDM Professional in mlRequiredVersionMajor and mlRequiredVersionMinor of the [EdmAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo.html) structure that is passed as a parameter in [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_UNSUPPORTED_PROGRAM_VERSION: The installed program is at a version level that is lower than the specified version.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
