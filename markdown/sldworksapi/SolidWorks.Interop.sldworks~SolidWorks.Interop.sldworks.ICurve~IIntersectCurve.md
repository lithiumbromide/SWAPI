---
title: "IIntersectCurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IIntersectCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurve.html"
---

# IIntersectCurve Method (ICurve)

Gets a set of points that represent the intersection of two trimmed curves.

## Syntax

### Visual Basic (Declaration)

```vb
Function IIntersectCurve( _
   ByVal OtherCurve As Curve, _
   ByRef ThisStartPoint As System.Double, _
   ByRef ThisEndPoint As System.Double, _
   ByRef OtherStartPoint As System.Double, _
   ByRef OtherEndPoint As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim OtherCurve As Curve
Dim ThisStartPoint As System.Double
Dim ThisEndPoint As System.Double
Dim OtherStartPoint As System.Double
Dim OtherEndPoint As System.Double
Dim value As System.Double

value = instance.IIntersectCurve(OtherCurve, ThisStartPoint, ThisEndPoint, OtherStartPoint, OtherEndPoint)
```

### C#

```csharp
System.double IIntersectCurve(
   Curve OtherCurve,
   ref System.double ThisStartPoint,
   ref System.double ThisEndPoint,
   ref System.double OtherStartPoint,
   ref System.double OtherEndPoint
)
```

### C++/CLI

```cpp
System.double IIntersectCurve(
   Curve^ OtherCurve,
   System.double% ThisStartPoint,
   System.double% ThisEndPoint,
   System.double% OtherStartPoint,
   System.double% OtherEndPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OtherCurve`: Curve to intersect with this [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `ThisStartPoint`: Start point of this curve
- `ThisEndPoint`: End point of this curve
- `OtherStartPoint`: Start point of otherCurve
- `OtherEndPoint`: End point of otherCurve

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles of the intersection points (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [Curve::IIntersectCurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~IIntersectCurve.html).

## Remarks

The array of doubles returned contains the x, y, z location of the tessellation points and a code for each point that indicates the intersection class:

[ x1, y1, z1, k1, x2, y2, z2, k2.... ]

Return codes are defined in [swIntersectionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swIntersectionType_e.html).

Before calling this method, call [ICurve::IIntersectCurveSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IIntersectCurveSize.html) to determine the size of the array needed for the return values from this method.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::IntersectCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IntersectCurve.html)

## Availability

SOLIDWORKS 98Plus, datecode 1988319
