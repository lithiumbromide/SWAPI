---
title: "CircleParams Property (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "CircleParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CircleParams.html"
---

# CircleParams Property (ICurve)

Gets the parameters of a curve that is a circle.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CircleParams As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Object

value = instance.CircleParams
```

### C#

```csharp
System.object CircleParams {get;}
```

### C++/CLI

```cpp
property System.Object^ CircleParams {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Curve::CircleParams](ms-its:sldworksapivb6.chm::/sldworks~Curve~CircleParams.html).

## Examples

[Get Entities Attached to Cosmetic Thread (VBA)](Get_Entities_Attached_To_Cosmetic_Thread_Example_VB.htm)

## Remarks

To determine if a circular edge is a complete circle or an arc, use [IEdge::GetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetCurveParams2.html).

The return value is the following array of 7 double values:

[ center.x, center.y, center.z, axis.x, axis.y, axis.z, radius ]

Center and radius values are in meters.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::IsCircle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsCircle.html)
[ICurve::ICircleParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ICircleParams.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)
