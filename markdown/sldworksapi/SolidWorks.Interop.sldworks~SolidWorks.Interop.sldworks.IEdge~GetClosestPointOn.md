---
title: "GetClosestPointOn Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "GetClosestPointOn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetClosestPointOn.html"
---

# GetClosestPointOn Method (IEdge)

Uses the X,Y,Z input point and returns the closest point on the edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object

value = instance.GetClosestPointOn(X, Y, Z)
```

### C#

```csharp
System.object GetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.Object^ GetClosestPointOn(
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

Array of five doubles (see **Remarks**)

## VBA Syntax

See [Edge::GetClosestPointOn](ms-its:sldworksapivb6.chm::/sldworks~Edge~GetClosestPointOn.html).

## Remarks

This method returns only one point, regardless of how many points achieve the minimum distance.

This method returns an array that contains the following values:

**[** `PointX, PointY, PointZ, UParameter, NotUsed` **]**

where the point values represent the point on the edge, and `UParameter` is the parameter on the edge that is closest to the input point. Ignore the fifth array element.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetClosestPointOn.html)
[ICurve::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetClosestPointOn.html)
[ICurve::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetClosestPointOn.html)
[IFace2::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetClosestPointOn.html)
[IFace2::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetClosestPointOn.html)
[ISurface::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetClosestPointOn.html)
[ISurface::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetClosestPointOn.html)
[IVertex::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetClosestPointOn.html)
[IVertex::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetClosestPointOn.html)
