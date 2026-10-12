---
title: "TableType Property (IEdmSWBom)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSWBom"
member: "TableType"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom~TableType.html"
---

# TableType Property (IEdmSWBom)

Gets or sets the type of this BOM.

## Syntax

### Visual Basic

```vb
Property TableType As System.Integer
```

### C#

```csharp
System.int TableType {get; set;}
```

### C++/CLI

```cpp
property System.int TableType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

0 = Parts only

1 = Top-level only

2 = Indented

## Examples

See the [IEdmBomMgr3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3.html) examples.

## See Also

[IEdmSWBom Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom.html)
[IEdmSWBom Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom_members.html)

## Availability

SOLIDWORKS PDM Professional 2021 SP03
