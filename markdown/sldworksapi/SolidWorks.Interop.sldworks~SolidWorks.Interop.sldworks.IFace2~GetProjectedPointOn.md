---
title: "GetProjectedPointOn Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetProjectedPointOn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetProjectedPointOn.html"
---

# GetProjectedPointOn Method (IFace2)

Gets the point where the input point is projected on to this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProjectedPointOn( _
   ByVal Point As MathPoint, _
   ByVal Direction As MathVector _
) As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim Point As MathPoint
Dim Direction As MathVector
Dim value As MathPoint

value = instance.GetProjectedPointOn(Point, Direction)
```

### C#

```csharp
MathPoint GetProjectedPointOn(
   MathPoint Point,
   MathVector Direction
)
```

### C++/CLI

```cpp
MathPoint^ GetProjectedPointOn(
   MathPoint^ Point,
   MathVector^ Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: [Point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) to project
- `Direction`: [Direction](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) to project the point

### Return Value

[Point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) where the input point is projected on to the face

## VBA Syntax

See [Face2::GetProjectedPointOn](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetProjectedPointOn.html).

## Examples

[Get Projected Point (VBA)](Get_Projected_Point_Example_VB.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetClosestPointOn.html)
[IFace2::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetClosestPointOn.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
