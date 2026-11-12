---
title: "AddSWBom Method (IEdmBomMgr3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomMgr3"
member: "AddSWBom"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3~AddSWBom.html"
---

# AddSWBom Method (IEdmBomMgr3)

Adds the specified SOLIDWORKS BOM to the specified document.

## Syntax

### Visual Basic

```vb
Sub AddSWBom( _
   ByVal lDocumentID As System.Integer, _
   ByVal lProjectID As System.Integer, _
   ByVal lDocRevNr As System.Integer, _
   ByVal poSWBom As EdmSWBom _
)
```

### C#

```csharp
void AddSWBom(
   System.int lDocumentID,
   System.int lProjectID,
   System.int lDocRevNr,
   EdmSWBom poSWBom
)
```

### C++/CLI

```cpp
void AddSWBom(
   System.int lDocumentID,
   System.int lProjectID,
   System.int lDocRevNr,
   EdmSWBom^ poSWBom
)
```

### Parameters

- `lDocumentID`: ID of document
- `lProjectID`: ID of project where document resides
- `lDocRevNr`: Version number of document
- `poSWBom`: [IEdmSWBom](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom.html)

## Examples

See the [IEdmBomMgr3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3.html) examples.

## See Also

[IEdmBomMgr3 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3.html)
[IEdmBomMgr3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3_members.html)

## Availability

SOLIDWORKS PDM Professional 2021 SP03
