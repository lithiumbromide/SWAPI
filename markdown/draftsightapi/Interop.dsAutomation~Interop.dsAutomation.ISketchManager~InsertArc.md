---
title: "InsertArc Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArc.html"
---

# InsertArc Method (ISketchManager)

Constructs an Arc.

## Syntax

### Visual Basic

```vb
Function InsertArc( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal CenterZ As System.Double, _
   ByVal Radius As System.Double, _
   ByVal StartAngle As System.Double, _
   ByVal EndAngle As System.Double _
) As CircleArc
```

### C#

```csharp
CircleArc InsertArc(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double Radius,
   System.double StartAngle,
   System.double EndAngle
)
```

### JScript

```
function InsertArc(
   CenterX : System.double,
   CenterY : System.double,
   CenterZ : System.double,
   Radius : System.double,
   StartAngle : System.double,
   EndAngle : System.double
) : CircleArc;
```

### Managed Extensions for C++

```
CircleArc* InsertArc(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double Radius,
   System.double StartAngle,
   System.double EndAngle
)
```

### C++/CLI

```cpp
CircleArc^ InsertArc(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double Radius,
   System.double StartAngle,
   System.double EndAngle
)
```

### Parameters

- `CenterX`: x coordinate for the center point of the Arc
- `CenterY`: y coordinate for the center point of the Arc
- `CenterZ`: z coordinate for the center point of the Arc
- `Radius`: Radius of Arc
- `StartAngle`: Positive or negative value of the angle from the chord tangent to the start point in radians
- `EndAngle`: Positive or negative value of the angle from the chord tangent to the end point in radians

### Return Value

[Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)

## Examples

[Construct Arc (C#)](Construct_Arc_Example_CSharp.htm)
[Construct Arc (VB.NET)](Construct_Arc_Example_VBNET.htm)
[Construct Arc (VBA)](Construct_Arc_Example_VBA.htm)
[Insert and Dimension Sketch (JavaScript)](Insert_and_Dimension_Sketch_Example_JS.htm)
[Mirror Entities (JavaScript)](Mirror_Entities_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertArcByCenter2Points2 Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcByCenter2Points2.html)
[ISketchManager::InsertArcBy3Points Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcBy3Points.html)

## Availability

DraftSight V1R1.1
