---
title: "InsertEllipseArcRotation Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertEllipseArcRotation"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseArcRotation.html"
---

# InsertEllipseArcRotation Method (ISketchManager)

Constructs an elliptical Arc using the specified axes end points, angle of rotation, and start and end angles.

## Syntax

### Visual Basic

```vb
Function InsertEllipseArcRotation( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Rotation As System.Double, _
   ByVal StartAngle As System.Double, _
   ByVal EndAngle As System.Double _
) As EllipseArc
```

### C#

```csharp
EllipseArc InsertEllipseArcRotation(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double Rotation,
   System.double StartAngle,
   System.double EndAngle
)
```

### JScript

```
function InsertEllipseArcRotation(
   X1 : System.double,
   Y1 : System.double,
   X2 : System.double,
   Y2 : System.double,
   Rotation : System.double,
   StartAngle : System.double,
   EndAngle : System.double
) : EllipseArc;
```

### Managed Extensions for C++

```
EllipseArc* InsertEllipseArcRotation(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double Rotation,
   System.double StartAngle,
   System.double EndAngle
)
```

### C++/CLI

```cpp
EllipseArc^ InsertEllipseArcRotation(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double Rotation,
   System.double StartAngle,
   System.double EndAngle
)
```

### Parameters

- `X1`: x coordinate of first axis end point
- `Y1`: y coordinate of first axis end point
- `X2`: x coordinate of second axis end point
- `Y2`: y coordinate of second axis end point
- `Rotation`: Angle of rotation; a value between 0° and 89.9°
- `StartAngle`: Start angle of the arc
- `EndAngle`: End angle of the arc

### Return Value

[Ellipitcal Arc](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)

## Examples

[Construct Ellipses and Elliptical Arcs (C#)](Construct_Ellipses_and_Elliptical_Arcs_Example_CSharp.htm)
[Construct Ellipses and Elliptical Arcs (VB.NET)](Construct_Ellipses_and_Elliptical_Arcs_Example_VBNET.htm)
[Construct Ellipses and Elliptical Arcs (VBA)](Construct_Ellipses_and_Elliptical_Arcs_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertEllipseArcDistanceToOtherAxis Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseArcDistanceToOtherAxis.html)
[ISketchManager::InsertEllipseRotation Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseRotation.html)

## Availability

DraftSight V1R1.1
