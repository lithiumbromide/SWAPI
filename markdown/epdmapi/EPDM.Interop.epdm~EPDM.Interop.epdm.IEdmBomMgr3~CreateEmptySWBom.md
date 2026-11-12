---
title: "CreateEmptySWBom Method (IEdmBomMgr3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomMgr3"
member: "CreateEmptySWBom"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3~CreateEmptySWBom.html"
---

# CreateEmptySWBom Method (IEdmBomMgr3)

Creates an empty SOLIDWORKS BOM.

## Syntax

### Visual Basic

```vb
Function CreateEmptySWBom() As EdmSWBom
```

### C#

```csharp
EdmSWBom CreateEmptySWBom()
```

### C++/CLI

```cpp
EdmSWBom^ CreateEmptySWBom();
```

### Return Value

[IEdmSWBom](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom.html)

## Examples

See the [IEdmBomMgr3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3.html) examples.

## Remarks

After calling this method, call [IEdmBomMgr3::AddSWBom](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3~AddSWBom.html) to add a new SOLIDWORKS BOM to an existing document.

## See Also

[IEdmBomMgr3 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3.html)
[IEdmBomMgr3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3_members.html)

## Availability

SOLIDWORKS PDM Professional 2021 SP03
