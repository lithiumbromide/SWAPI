---
title: "GetErrorString Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "GetErrorString"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetErrorString.html"
---

# GetErrorString Method (IEdmVault5)

Gets the name and description for the specified error code returned by one of SOLIDWORKS PDM Professional's API methods.

## Syntax

### Visual Basic

```vb
Sub GetErrorString( _
   ByVal lError As System.Integer, _
   Optional ByRef pbsErrorName As System.String, _
   Optional ByRef pbsDescription As System.String _
)
```

### C#

```csharp
void GetErrorString(
   System.int lError,
   out System.string pbsErrorName,
   out System.string pbsDescription
)
```

### C++/CLI

```cpp
void GetErrorString(
   System.int lError,
   [Out] System.String^ pbsErrorName,
   [Out] System.String^ pbsDescription
)
```

### Parameters

- `lError`: Error code for which to get a description
- `pbsErrorName`: Error name as defined in [Return codes](ReturnCodes.htm); hexadecimal number if the error is unknown
- `pbsDescription`: Description of the error

## Examples

[Batch Add Files and Folders to Vault (VB.NET)](Batch_Add_Files_and_Folders_Example_VBNET.htm)
[Batch Add Files and Folders to Vault (C#)](Batch_Add_Files_and_Folders_Example_CSharp.htm)

## Remarks

You do not have to be logged in to the vault to call this method.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)
[IEdmVault11::GetErrorMessage Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetErrorMessage.html)
[IEdmVault11::GetErrorName Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetErrorName.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
