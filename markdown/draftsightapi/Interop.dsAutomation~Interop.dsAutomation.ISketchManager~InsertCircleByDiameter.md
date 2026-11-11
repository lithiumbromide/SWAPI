---
title: "InsertCircleByDiameter Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertCircleByDiameter"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircleByDiameter.html"
---

# InsertCircleByDiameter Method (ISketchManager)

Constructs a Circle using the specified center point and diameter.

## Syntax

### Visual Basic

```vb
Function InsertCircleByDiameter( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal CenterZ As System.Double, _
   ByVal Diameter As System.Double _
) As Circle
```

### C#

```csharp
Circle InsertCircleByDiameter(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double Diameter
)
```

### JScript

```
function InsertCircleByDiameter(
   CenterX : System.double,
   CenterY : System.double,
   CenterZ : System.double,
   Diameter : System.double
) : Circle;
```

### Managed Extensions for C++

```
Circle* InsertCircleByDiameter(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double Diameter
)
```

### C++/CLI

```cpp
Circle^ InsertCircleByDiameter(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double Diameter
)
```

### Parameters

- `CenterX`: x coordinate of the center point
- `CenterY`: y coordinate of the center point
- `CenterZ`: z coordinate of the center point
- `Diameter`: Diameter of Circle

### Return Value

[Circle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertCircle Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircle.html)
[ISketchManager::InsertCircleBy3Points Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircleBy3Points.html)

## Availability

DraftSight V1R3.0
