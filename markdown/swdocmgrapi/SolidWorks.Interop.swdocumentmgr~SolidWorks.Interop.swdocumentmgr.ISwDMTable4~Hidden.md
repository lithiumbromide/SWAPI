---
title: "Hidden Property (ISwDMTable4)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable4"
member: "Hidden"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4~Hidden.html"
---

# Hidden Property (ISwDMTable4)

Gets whether the bill of materials (BOM) table is hidden.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Hidden As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable4
Dim value As System.Boolean

value = instance.Hidden
```

### C#

```csharp
System.bool Hidden {get;}
```

### C++/CLI

```cpp
property System.bool Hidden {
   System.bool get();
}
```

### Property Value

True if the BOM table is hidden, false if the BOM table is shown

## VBA Syntax

See [SwDMTable4::Hidden](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable4~Hidden.html).

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
