---
title: "PartConfigurationGrouping Property (ISwDMTable4)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable4"
member: "PartConfigurationGrouping"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4~PartConfigurationGrouping.html"
---

# PartConfigurationGrouping Property (ISwDMTable4)

Gets the part configuration grouping for the bill of materials (BOM) table.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PartConfigurationGrouping As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable4
Dim value As System.Integer

value = instance.PartConfigurationGrouping
```

### C#

```csharp
System.int PartConfigurationGrouping {get;}
```

### C++/CLI

```cpp
property System.int PartConfigurationGrouping {
   System.int get();
}
```

### Property Value

Part configuration grouping as defined in [swDMPartConfigurationGrouping](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDMPartConfigurationGrouping.html)

## VBA Syntax

See [SwDMTable4::PartConfigurationGrouping](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable4~PartConfigurationGrouping.html).

## Examples

[Get BOM Tables (C#)](Get_BOM_Tables_Example_CSharp.htm)
[Get BOM Tables (VB.NET)](Get_BOM_Tables_Example_VBNET.htm)

## Requirements

This property only supports model documents saved in SOLIDWORKS 2012 and later.

## See Also

[ISwDMTable4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4.html)
[ISwDMTable4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4_members.html)

## Availability

SOLIDWORKS Document Manager API 2012 SP0
