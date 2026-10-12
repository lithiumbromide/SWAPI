---
title: "GetVaultNameFromPath Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "GetVaultNameFromPath"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetVaultNameFromPath.html"
---

# GetVaultNameFromPath Method (IEdmVault5)

Gets the name of the vault where the specified file or folder resides.

## Syntax

### Visual Basic

```vb
Function GetVaultNameFromPath( _
   ByVal bsPath As System.String _
) As System.String
```

### C#

```csharp
System.string GetVaultNameFromPath(
   System.string bsPath
)
```

### C++/CLI

```cpp
System.String^ GetVaultNameFromPath(
   System.String^ bsPath
)
```

### Parameters

- `bsPath`: Full system path to a file or folder

### Return Value

Vault name

## Examples

[Check Out and Copy File (VB.NET)](Check_Out_and_Copy_File_Example_VBNET.htm)
[Check Out and Copy File (C#)](Check_Out_and_Copy_File_Example_CSharp.htm)

## Remarks

You do not need to call [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) or [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html) before calling this method.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_KEY_NOT_FOUND: The specified path is not in any vault.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
