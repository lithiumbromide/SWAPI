---
title: "ConvertLineToBcurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "ConvertLineToBcurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.html"
---

# ConvertLineToBcurve Method (ICurve)

Converts the specified line into a b-spline curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvertLineToBcurve( _
   ByVal StartPoint As System.Object, _
   ByVal EndPoint As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim StartPoint As System.Object
Dim EndPoint As System.Object
Dim value As System.Object

value = instance.ConvertLineToBcurve(StartPoint, EndPoint)
```

### C#

```csharp
System.object ConvertLineToBcurve(
   System.object StartPoint,
   System.object EndPoint
)
```

### C++/CLI

```cpp
System.Object^ ConvertLineToBcurve(
   System.Object^ StartPoint,
   System.Object^ EndPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartPoint`: Array values for the coordinates of the start point of the line
- `EndPoint`: Array values for the coordinates of the end point of the line

### Return Value

Array values giving the b-spline representation of the line

## VBA Syntax

See [Curve::ConvertLineToBcurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~ConvertLineToBcurve.html).

## Remarks

Given coordinates of two end points of a line, this method returns the b-spline representation of the line. The returned data are doubles arranged in the following order:

| dim, order |  |  |
| --- | --- | --- |
|  | dim | Dimension of the control point data. If dim=3 (non-rational), control point coordinates are returned as [x0,y0,z0,x1,y1,z1,.....]. If dim=4 (rational), control point coordinates are returned as [x0,y0,z0,w0,x1,y1,z1,w1,.....], where w is the weight for the point. |
|  | order | Order of the b-spline returned. |
| NumControlPoints, Periodic |  |  |
|  | NumControlPoints | Number of control points for the b-spline. |
|  | Periodic | True if the b-spline is periodic. |
| Knots |  |  |
| ControlPoints |  |  |

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.html)
[ICurve::GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.html)
[ICurve::IGetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.html)
[ICurve::IsLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.html)
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.html)
