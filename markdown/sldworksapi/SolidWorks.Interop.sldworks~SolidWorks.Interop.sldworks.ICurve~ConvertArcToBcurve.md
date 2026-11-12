---
title: "ConvertArcToBcurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "ConvertArcToBcurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.html"
---

# ConvertArcToBcurve Method (ICurve)

Gets the b-spline value representation of the arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvertArcToBcurve( _
   ByVal Center As System.Object, _
   ByVal Axis As System.Object, _
   ByVal Start As System.Object, _
   ByVal End As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim Center As System.Object
Dim Axis As System.Object
Dim Start As System.Object
Dim End As System.Object
Dim value As System.Object

value = instance.ConvertArcToBcurve(Center, Axis, Start, End)
```

### C#

```csharp
System.object ConvertArcToBcurve(
   System.object Center,
   System.object Axis,
   System.object Start,
   System.object End
)
```

### C++/CLI

```cpp
System.Object^ ConvertArcToBcurve(
   System.Object^ Center,
   System.Object^ Axis,
   System.Object^ Start,
   System.Object^ End
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`: Array for the x, y, z coordinates of the center point of the
  arc
- `Axis`: Array for the normal vector of the arc
- `Start`: Array for the x, y, z coordinates of the start point of the arc
- `End`: Array for the x, y, z coordinates of the end point of the arc

### Return Value

Array for the b-spline representation of the arc

## VBA Syntax

See [Curve::ConvertArcToBcurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~ConvertArcToBcurve.html).

## Remarks

Given coordinates of the center, start, end points and the normal vector of an arc, this method returns the b-spline representation of the arc.

The returned data are doubles arranged in the following order:

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
[ICurve::ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.html)
[ICurve::GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.html)
[ICurve::IGetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.html)
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.html)
