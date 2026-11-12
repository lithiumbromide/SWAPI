---
title: "Position Property (IEdgePoint)"
project: "SOLIDWORKS API Help"
interface: "IEdgePoint"
member: "Position"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint~Position.html"
---

# Position Property (IEdgePoint)

Gets or sets the position of the midpoint on an [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) or an endpoint or midpoint on a [reference curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReferenceCurve.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Position As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgePoint
Dim value As System.Double

instance.Position = value

value = instance.Position
```

### C#

```csharp
System.double Position {get; set;}
```

### C++/CLI

```cpp
property System.double Position {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 (start) to 100 (end)

## VBA Syntax

See [EdgePoint::Position](ms-its:sldworksapivb6.chm::/sldworks~EdgePoint~Position.html).

## Examples

[Create Reference Curve (C#)](Create_Reference_Curve_Example_CSharp.htm)
[Create Reference Curve (VB.NET)](Create_Reference_Curve_Example_VBNET.htm)
[Create Reference Curve (VBA)](Create_Reference_Curve_Example_VB.htm)

## See Also

[IEdgePoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint.html)
[IEdgePoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
