---
title: "GetVersion Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "GetVersion"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetVersion.html"
---

# GetVersion Method (IEdmVault5)

Gets the version of SOLIDWORKS PDM Professional that is installed on this machine.

## Syntax

### Visual Basic

```vb
Sub GetVersion( _
   ByRef plMajor As System.Integer, _
   ByRef plMinor As System.Integer _
)
```

### C#

```csharp
void GetVersion(
   out System.int plMajor,
   out System.int plMinor
)
```

### C++/CLI

```cpp
void GetVersion(
   [Out] System.int plMajor,
   [Out] System.int plMinor
)
```

### Parameters

- `plMajor`: Major version number
- `plMinor`: Minor version number

## Examples

[Log Into Vault and Display Information (C#)](Log_Into_Vault_and_Display_Information_Example_CSharp.htm)
[Log Into Vault and Display Information (VB.NET)](Log_Into_Vault_and_Display_Information_Example_VBNET.htm)

## Remarks

You do not need to call [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) or [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html) before calling this method.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
