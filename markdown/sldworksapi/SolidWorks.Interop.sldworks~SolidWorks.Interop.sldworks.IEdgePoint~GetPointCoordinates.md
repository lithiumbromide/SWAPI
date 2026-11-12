---
title: "GetPointCoordinates Method (IEdgePoint)"
project: "SOLIDWORKS API Help"
interface: "IEdgePoint"
member: "GetPointCoordinates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint~GetPointCoordinates.html"
---

# GetPointCoordinates Method (IEdgePoint)

Gets the coordinates for this midpoint on an [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) or an endpoint or midpoint on a [reference curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReferenceCurve.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetPointCoordinates( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgePoint
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.GetPointCoordinates(X, Y, Z)
```

### C#

```csharp
void GetPointCoordinates(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### C++/CLI

```cpp
void GetPointCoordinates(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate for this midpoint or endpoint
- `Y`: y coordinate for this midpoint or endpoint
- `Z`: z coordinate for this midpoint or endpoint

## VBA Syntax

See [EdgePoint::GetPointCoordinates](ms-its:sldworksapivb6.chm::/sldworks~EdgePoint~GetPointCoordinates.html).

## Examples

[Create Reference Curve (C#)](Create_Reference_Curve_Example_CSharp.htm)
[Create Reference Curve (VB.NET)](Create_Reference_Curve_Example_VBNET.htm)
[Create Reference Curve (VBA)](Create_Reference_Curve_Example_VB.htm)

## See Also

[IEdgePoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint.html)
[IEdgePoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
