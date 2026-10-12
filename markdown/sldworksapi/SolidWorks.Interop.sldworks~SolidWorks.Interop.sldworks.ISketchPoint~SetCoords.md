---
title: "SetCoords Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "SetCoords"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~SetCoords.html"
---

# SetCoords Method (ISketchPoint)

Sets the location of this sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCoords( _
   ByVal Xx As System.Double, _
   ByVal Yy As System.Double, _
   ByVal Zz As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim Xx As System.Double
Dim Yy As System.Double
Dim Zz As System.Double
Dim value As System.Boolean

value = instance.SetCoords(Xx, Yy, Zz)
```

### C#

```csharp
System.bool SetCoords(
   System.double Xx,
   System.double Yy,
   System.double Zz
)
```

### C++/CLI

```cpp
System.bool SetCoords(
   System.double Xx,
   System.double Yy,
   System.double Zz
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Xx`: X component of the direction vector
- `Yy`: Y component of the direction vector
- `Zz`: Z component of the direction vector

### Return Value

True if the coordinates are successfully set, false if not

## VBA Syntax

See [SketchPoint::SetCoords](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~SetCoords.html).

## Remarks

When setting new coordinate values to a sketch point, this method adheres to any constraints that are active in the sketch. If the sketch point is an end point of a sketch line that is constrained to be horizontal, then the values are adjusted according to that constraint.

To set the coordinates of a sketch point on a spline, the location of the sketch point must already exist on the spline. You cannot use this method to create a new sketch point that is not on the spline.

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
[ISketchPoint::GetCoords Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetCoords.html)
[ISketchPoint::X Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~X.html)
[ISketchPoint::Y Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Y.html)
[ISketchPoint::Z Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Z.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
