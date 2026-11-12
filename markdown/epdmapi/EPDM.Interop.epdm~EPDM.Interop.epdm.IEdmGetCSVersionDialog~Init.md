---
title: "Init Method (IEdmGetCSVersionDialog)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmGetCSVersionDialog"
member: "Init"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetCSVersionDialog~Init.html"
---

# Init Method (IEdmGetCSVersionDialog)

Populates the Restore coldstored file version dialog with data.

## Syntax

### Visual Basic

```vb
Sub Init( _
   ByVal poVault As IEdmVault5, _
   ByVal lArcSrvID As System.Integer, _
   ByVal eError As EdmGetOpError, _
   ByVal bsFileName As System.String, _
   ByVal lDocID As System.Integer, _
   ByVal lVersionNo As System.Integer, _
   ByVal lDateFmt As System.Integer, _
   ByVal lDisplayErrCode As System.Integer _
)
```

### C#

```csharp
void Init(
   IEdmVault5 poVault,
   System.int lArcSrvID,
   EdmGetOpError eError,
   System.string bsFileName,
   System.int lDocID,
   System.int lVersionNo,
   System.int lDateFmt,
   System.int lDisplayErrCode
)
```

### C++/CLI

```cpp
void Init(
   IEdmVault5^ poVault,
   System.int lArcSrvID,
   EdmGetOpError eError,
   System.String^ bsFileName,
   System.int lDocID,
   System.int lVersionNo,
   System.int lDateFmt,
   System.int lDisplayErrCode
)
```

### Parameters

- `poVault`: [IEdmVault5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html); pointer to the vault
- `lArcSrvID`: Archive server ID
- `eError`: [EdmGetOpError](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetOpError.html); error code returned after getting coldstored version
- `bsFileName`: Name of the file being restored from cold storage
- `lDocID`: ID of the document being restored from cold storage
- `lVersionNo`: Version number of the file being restored from cold storage
- `lDateFmt`: SQL Server date format code (see Remarks in [IEdmVault11::CreateNewVault](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~CreateNewVault.html))
- `lDisplayErrCode`: Not implemented

## See Also

[IEdmGetCSVersionDialog Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetCSVersionDialog.html)
[IEdmGetCSVersionDialog Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetCSVersionDialog_members.html)
