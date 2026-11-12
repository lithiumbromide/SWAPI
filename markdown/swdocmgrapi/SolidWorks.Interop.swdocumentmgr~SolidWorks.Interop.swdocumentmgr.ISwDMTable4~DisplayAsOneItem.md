---
title: "DisplayAsOneItem Property (ISwDMTable4)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable4"
member: "DisplayAsOneItem"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4~DisplayAsOneItem.html"
---

# DisplayAsOneItem Property (ISwDMTable4)

Gets whether different configurations have the same item number when the bill of materials (BOM) table contains components with multiple configurations.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DisplayAsOneItem As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable4
Dim value As System.Boolean

value = instance.DisplayAsOneItem
```

### C#

```csharp
System.bool DisplayAsOneItem {get;}
```

### C++/CLI

```cpp
property System.bool DisplayAsOneItem {
   System.bool get();
}
```

### Property Value

True if different configurations have the same item number when the BOM table contains components with multiple configurations, false if different configurations have different item numbers when the BOM table contains components with multiple configurations

## VBA Syntax

See [SwDMTable4::DisplayAsOneItem](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable4~DisplayAsOneItem.html).

## Examples

[Get BOM Tables (C#)](Get_BOM_Tables_Example_CSharp.htm)
[Get BOM Tables (VB.NET)](Get_BOM_Tables_Example_VBNET.htm)

## Remarks

This property only supports model documents saved in SOLIDWORKS 2012 and later.

## See Also

[ISwDMTable4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4.html)
[ISwDMTable4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4_members.html)

## Availability

SOLIDWORKS Document Manager API 2012 SP0
