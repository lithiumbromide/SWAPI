---
title: "Pattern3DCircular Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "Pattern3DCircular"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Pattern3DCircular.html"
---

# Pattern3DCircular Method (ISketchManager)

Creates a pattern of the specified entities in 3D space in a circular alignment about a rotation axis.

## Syntax

### Visual Basic

```vb
Sub Pattern3DCircular( _
   ByVal NumberItemsInPattern As System.Integer, _
   ByVal AngleToFill As System.Double, _
   ByVal RotatePatternElements As System.Boolean, _
   ByVal CenterPoint As MathPoint, _
   ByVal SecondPointOnAxis As MathPoint, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void Pattern3DCircular(
   System.int NumberItemsInPattern,
   System.double AngleToFill,
   System.bool RotatePatternElements,
   MathPoint CenterPoint,
   MathPoint SecondPointOnAxis,
   System.object EntitiesArray
)
```

### JScript

```
function Pattern3DCircular(
   NumberItemsInPattern : System.int,
   AngleToFill : System.double,
   RotatePatternElements : System.boolean,
   CenterPoint : MathPoint,
   SecondPointOnAxis : MathPoint,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void Pattern3DCircular(
   System.int NumberItemsInPattern,
   System.double AngleToFill,
   System.bool RotatePatternElements,
   MathPoint* CenterPoint,
   MathPoint* SecondPointOnAxis,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void Pattern3DCircular(
   System.int NumberItemsInPattern,
   System.double AngleToFill,
   System.bool RotatePatternElements,
   MathPoint^ CenterPoint,
   MathPoint^ SecondPointOnAxis,
   System.Object^ EntitiesArray
)
```

### Parameters

- `NumberItemsInPattern`: Number of items to pattern
- `AngleToFill`: Angle to fill (see **Remarks**)
- `RotatePatternElements`: True to rotate the entities when copied, false to not
- `CenterPoint`: [Center point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) of the rotation axis
- `SecondPointOnAxis`: [Second point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on the rotation axis
- `EntitiesArray`: Array of entities from which to create the circular pattern in 3D space

## Remarks

Type a positive number for a counterclockwise fill angle, or type a negative number for a clockwise fill angle.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::PatternCircular Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternCircular.html)
[ISketchManager::Pattern3DLinear Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Pattern3DLinear.html)
[ISketchManager::PatternLinear Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternLinear.html)

## Availability

DraftSight V1R4.0
