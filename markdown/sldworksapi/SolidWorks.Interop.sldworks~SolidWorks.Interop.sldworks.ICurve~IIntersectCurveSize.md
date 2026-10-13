---
title: "IIntersectCurveSize Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IIntersectCurveSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IIntersectCurveSize.html"
---

# IIntersectCurveSize Method (ICurve)

Gets the size of the array required by [ICurve::IIntersectCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IIntersectCurve.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IIntersectCurveSize( _
   ByVal OtherCurve As Curve, _
   ByRef ThisStartPoint As System.Double, _
   ByRef ThisEndPoint As System.Double, _
   ByRef OtherStartPoint As System.Double, _
   ByRef OtherEndPoint As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim OtherCurve As Curve
Dim ThisStartPoint As System.Double
Dim ThisEndPoint As System.Double
Dim OtherStartPoint As System.Double
Dim OtherEndPoint As System.Double
Dim value As System.Integer

value = instance.IIntersectCurveSize(OtherCurve, ThisStartPoint, ThisEndPoint, OtherStartPoint, OtherEndPoint)
```

### C#

```csharp
System.int IIntersectCurveSize(
   Curve OtherCurve,
   ref System.double ThisStartPoint,
   ref System.double ThisEndPoint,
   ref System.double OtherStartPoint,
   ref System.double OtherEndPoint
)
```

### C++/CLI

```cpp
System.int IIntersectCurveSize(
   Curve^ OtherCurve,
   System.double% ThisStartPoint,
   System.double% ThisEndPoint,
   System.double% OtherStartPoint,
   System.double% OtherEndPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OtherCurve`: Curve to intersect with this curve
- `ThisStartPoint`: Start point of this curve
- `ThisEndPoint`: End point of this curve
- `OtherStartPoint`: Start point of otherCurve
- `OtherEndPoint`: End point of otherCurve

### Return Value

Size of the array needed to contain the return values of [ICurve::IIntersectCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IIntersectCurve.html)

## VBA Syntax

See [Curve::IIntersectCurveSize](ms-its:sldworksapivb6.chm::/sldworks~Curve~IIntersectCurveSize.html).

## Remarks

To get the actual intersection points, call [ICurve::IIntersectCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IIntersectCurve.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::IntersectCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IntersectCurve.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
