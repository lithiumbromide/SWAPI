---
title: "InsertEllipseArcDistanceToOtherAxis Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertEllipseArcDistanceToOtherAxis"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseArcDistanceToOtherAxis.html"
---

# InsertEllipseArcDistanceToOtherAxis Method (ISketchManager)

Constructs an elliptical Arc using the specified axes end points, radius of the perpendicular axis, and start and end angles.

## Syntax

### Visual Basic

```vb
Function InsertEllipseArcDistanceToOtherAxis( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal DistanceToOtherAxis As System.Double, _
   ByVal StartAngle As System.Double, _
   ByVal EndAngle As System.Double _
) As EllipseArc
```

### C#

```csharp
EllipseArc InsertEllipseArcDistanceToOtherAxis(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double DistanceToOtherAxis,
   System.double StartAngle,
   System.double EndAngle
)
```

### JScript

```
function InsertEllipseArcDistanceToOtherAxis(
   X1 : System.double,
   Y1 : System.double,
   X2 : System.double,
   Y2 : System.double,
   DistanceToOtherAxis : System.double,
   StartAngle : System.double,
   EndAngle : System.double
) : EllipseArc;
```

### Managed Extensions for C++

```
EllipseArc* InsertEllipseArcDistanceToOtherAxis(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double DistanceToOtherAxis,
   System.double StartAngle,
   System.double EndAngle
)
```

### C++/CLI

```cpp
EllipseArc^ InsertEllipseArcDistanceToOtherAxis(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double DistanceToOtherAxis,
   System.double StartAngle,
   System.double EndAngle
)
```

### Parameters

- `X1`: x coordinate of first axis end point
- `Y1`: y coordinate of first axis end point
- `X2`: x coordinate of second axis end point
- `Y2`: y coordinate of second axis end point
- `DistanceToOtherAxis`: Radius of the perpendicular axis
- `StartAngle`: Start angle of the arc
- `EndAngle`: End angle of the arc

### Return Value

[Elliptical Arc](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)

## Examples

[Construct Ellipses and Elliptical Arcs (C#)](Construct_Ellipses_and_Elliptical_Arcs_Example_CSharp.htm)
[Construct Ellipses and Elliptical Arcs (VB.NET)](Construct_Ellipses_and_Elliptical_Arcs_Example_VBNET.htm)
[Construct Ellipses and Elliptical Arcs (VBA)](Construct_Ellipses_and_Elliptical_Arcs_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertEllipseArcRotation Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseArcRotation.html)
[ISketchManager::InsertEllipseDistanceToOtherAxis Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseDistanceToOtherAxis.html)

## Availability

DraftSight V1R1.1
