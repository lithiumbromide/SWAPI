---
title: "GetClosestPointOn Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetClosestPointOn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetClosestPointOn.html"
---

# GetClosestPointOn Method (IFace2)

Uses the X,Y,Z input point to determine the closest point on the face.

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
Dim instance As IFace2
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

Array of five doubles representing the X,Y,Z point on the face followed by the U, V parameter on the face that is closest to the input point

## VBA Syntax

See [Face2::GetClosestPointOn](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetClosestPointOn.html).

## Examples

[Calculate Closest Distance Between Faces (VBA)](Calculate_Closest_Distance_Between_Faces_Example_VB.htm)

## Remarks

This method returns only one point, regardless of how many points achieve the minimum distance.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetClosestPointOn.html)
[ICurve::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetClosestPointOn.html)
[ICurve::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetClosestPointOn.html)
[IEdge::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetClosestPointOn.html)
[IEdge::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetClosestPointOn.html)
[IFace2::GetProjectedPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetProjectedPointOn.html)
[ISurface::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetClosestPointOn.html)
[ISurface::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetClosestPointOn.html)
[IVertex::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetClosestPointOn.html)
[IVertex::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetClosestPointOn.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
