---
title: "ICircleParams Property (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "ICircleParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ICircleParams.html"
---

# ICircleParams Property (ICurve)

Gets the parameters of a curve that is a circle.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ICircleParams As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Double

value = instance.ICircleParams
```

### C#

```csharp
System.double ICircleParams {get;}
```

### C++/CLI

```cpp
property System.double ICircleParams {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to an array of doubles (see **Remarks**)

## VBA Syntax

See [Curve::ICircleParams](ms-its:sldworksapivb6.chm::/sldworks~Curve~ICircleParams.html).

## Remarks

To determine if a circular edge is a complete circle or an arc, use [IEdge::IGetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetCurveParams2.html).

The return value is the following array of 7 double values:

[ center.x, center.y, center.z, axis.x, axis.y, axis.z, radius ]

Center and radius values are in meters.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::CircleParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CircleParams.html)
[ICurve::IsCircle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsCircle.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)
