---
title: "InsertEllipseRotation Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertEllipseRotation"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseRotation.html"
---

# InsertEllipseRotation Method (ISketchManager)

Constructs an Ellipse using the specified axes end points and the angle of rotation.

## Syntax

### Visual Basic

```vb
Function InsertEllipseRotation( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Rotation As System.Double _
) As EllipseArc
```

### C#

```csharp
EllipseArc InsertEllipseRotation(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double Rotation
)
```

### JScript

```
function InsertEllipseRotation(
   X1 : System.double,
   Y1 : System.double,
   X2 : System.double,
   Y2 : System.double,
   Rotation : System.double
) : EllipseArc;
```

### Managed Extensions for C++

```
EllipseArc* InsertEllipseRotation(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double Rotation
)
```

### C++/CLI

```cpp
EllipseArc^ InsertEllipseRotation(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double Rotation
)
```

### Parameters

- `X1`: x coordinate of first axis end point
- `Y1`: y coordinate of first axis end point
- `X2`: x coordinate of second axis end point
- `Y2`: y coordinate of second axis end point
- `Rotation`: Angle of rotation; a value between 0° and 89.9° in radians

### Return Value

[Ellipse](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)

## Examples

[Construct Ellipses and Elliptical Arcs (C#)](Construct_Ellipses_and_Elliptical_Arcs_Example_CSharp.htm)
[Construct Ellipses and Elliptical Arcs (VB.NET)](Construct_Ellipses_and_Elliptical_Arcs_Example_VBNET.htm)
[Construct Ellipses and Elliptical Arcs (VBA)](Construct_Ellipses_and_Elliptical_Arcs_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertEllipseDistanceToOtherAxis Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseDistanceToOtherAxis.html)
[ISketchManager::InsertEllipseArcRotation Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseArcRotation.html)

## Availability

DraftSight V1R1.1
