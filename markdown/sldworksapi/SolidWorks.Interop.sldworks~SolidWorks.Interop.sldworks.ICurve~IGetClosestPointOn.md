---
title: "IGetClosestPointOn Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IGetClosestPointOn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetClosestPointOn.html"
---

# IGetClosestPointOn Method (ICurve)

Determines the closest point on the curve using the x,y,z input point.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Double

value = instance.IGetClosestPointOn(X, Y, Z)
```

### C#

```csharp
System.double IGetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.double IGetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X value of the input point
- `Y`: Y value of the input point
- `Z`: Z value of the input point

### Return Value

Array of 5 doubles (see **Remarks**)

## VBA Syntax

See [Curve::IGetClosestPointOn](ms-its:sldworksapivb6.chm::/sldworks~Curve~IGetClosestPointOn.html).

## Remarks

This method returns only one point, regardless of the number of valid minimum distance points.

The array return contains the following values:

[ PointX, PointY, PointZ, ParamU, NotUsed ]

where:

- PointX, PointY,and PointZ represent the point on the curve
- ParamU is the parameter on the curve that is closest to the input point
- NotUsed is unused

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetClosestPointOn.html)
[IEdge::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetClosestPointOn.html)
[IEdge::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetClosestPointOn.html)
[IFace2::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetClosestPointOn.html)
[IFace2::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetClosestPointOn.html)
[ISelectionMgr::GetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.html)
[ISelectionMgr::IGetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.html)
[ISelectionMgr::IGetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.html)
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.html)
[ISurface::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetClosestPointOn.html)
[ISurface::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetClosestPointOn.html)
[IVertex::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetClosestPointOn.html)
[IVertex::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetClosestPointOn.html)
[IVertex::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetClosestPointOn.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
