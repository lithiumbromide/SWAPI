---
title: "Infinite Property (ISketchLine)"
project: "SOLIDWORKS API Help"
interface: "ISketchLine"
member: "Infinite"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~Infinite.html"
---

# Infinite Property (ISketchLine)

Gets whether the line is infinite or finite.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Infinite As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchLine
Dim value As System.Boolean

value = instance.Infinite
```

### C#

```csharp
System.bool Infinite {get;}
```

### C++/CLI

```cpp
property System.bool Infinite {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the line is infinite, false (finite) if not

## VBA Syntax

See [SketchLine::Infinite](ms-its:sldworksapivb6.chm::/sldworks~SketchLine~Infinite.html).

## Examples

[Make Line Infinite (VBA)](Make_Line_Infinite_Example_VB.htm)

## See Also

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)
[ISketchLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.html)
[ISketchLine::MakeInfinite Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~MakeInfinite.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
