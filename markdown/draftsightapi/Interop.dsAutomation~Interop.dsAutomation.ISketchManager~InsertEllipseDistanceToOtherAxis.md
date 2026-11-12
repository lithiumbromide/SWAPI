---
title: "InsertEllipseDistanceToOtherAxis Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertEllipseDistanceToOtherAxis"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseDistanceToOtherAxis.html"
---

# InsertEllipseDistanceToOtherAxis Method (ISketchManager)

Constructs an Ellipse using the specified axes end points and the radius of the perpendicular axis.

## Syntax

### Visual Basic

```vb
Function InsertEllipseDistanceToOtherAxis( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal DistanceToOtherAxis As System.Double _
) As EllipseArc
```

### C#

```csharp
EllipseArc InsertEllipseDistanceToOtherAxis(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double DistanceToOtherAxis
)
```

### JScript

```
function InsertEllipseDistanceToOtherAxis(
   X1 : System.double,
   Y1 : System.double,
   X2 : System.double,
   Y2 : System.double,
   DistanceToOtherAxis : System.double
) : EllipseArc;
```

### Managed Extensions for C++

```
EllipseArc* InsertEllipseDistanceToOtherAxis(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double DistanceToOtherAxis
)
```

### C++/CLI

```cpp
EllipseArc^ InsertEllipseDistanceToOtherAxis(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double DistanceToOtherAxis
)
```

### Parameters

- `X1`: x coordinate of first axis end point
- `Y1`: y coordinate of first axis end point
- `X2`: x coordinate of second axis end point
- `Y2`: y coordinate of second axis end point
- `DistanceToOtherAxis`: Radius of the perpendicular axis

### Return Value

[Ellipse](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)

## Examples

[Construct Ellipses and Elliptical Arcs (C#)](Construct_Ellipses_and_Elliptical_Arcs_Example_CSharp.htm)
[Construct Ellipses and Elliptical Arcs (VB.NET)](Construct_Ellipses_and_Elliptical_Arcs_Example_VBNET.htm)
[Construct Ellipses and Elliptical Arcs (VBA)](Construct_Ellipses_and_Elliptical_Arcs_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertEllipseRotation Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseRotation.html)
[ISketchManager::InsertEllipseArcDistanceToOtherAxis Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEllipseArcDistanceToOtherAxis.html)

## Availability

DraftSight V1R1.1
