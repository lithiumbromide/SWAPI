---
title: "Pattern3DLinear Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "Pattern3DLinear"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Pattern3DLinear.html"
---

# Pattern3DLinear Method (ISketchManager)

Creates a pattern of the specified entities in 3D space in a matrix of rows, columns, and levels.

## Syntax

### Visual Basic

```vb
Sub Pattern3DLinear( _
   ByVal NumberElementsOnVerticalAxis As System.Integer, _
   ByVal NumberElementsOnHorizontalAxis As System.Integer, _
   ByVal NumberLevels As System.Integer, _
   ByVal VerticalSpacing As System.Double, _
   ByVal HorizontalSpacing As System.Double, _
   ByVal SpacingBetweenLevels As System.Double, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void Pattern3DLinear(
   System.int NumberElementsOnVerticalAxis,
   System.int NumberElementsOnHorizontalAxis,
   System.int NumberLevels,
   System.double VerticalSpacing,
   System.double HorizontalSpacing,
   System.double SpacingBetweenLevels,
   System.object EntitiesArray
)
```

### JScript

```
function Pattern3DLinear(
   NumberElementsOnVerticalAxis : System.int,
   NumberElementsOnHorizontalAxis : System.int,
   NumberLevels : System.int,
   VerticalSpacing : System.double,
   HorizontalSpacing : System.double,
   SpacingBetweenLevels : System.double,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void Pattern3DLinear(
   System.int NumberElementsOnVerticalAxis,
   System.int NumberElementsOnHorizontalAxis,
   System.int NumberLevels,
   System.double VerticalSpacing,
   System.double HorizontalSpacing,
   System.double SpacingBetweenLevels,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void Pattern3DLinear(
   System.int NumberElementsOnVerticalAxis,
   System.int NumberElementsOnHorizontalAxis,
   System.int NumberLevels,
   System.double VerticalSpacing,
   System.double HorizontalSpacing,
   System.double SpacingBetweenLevels,
   System.Object^ EntitiesArray
)
```

### Parameters

- `NumberElementsOnVerticalAxis`: Number of rows (x axis)
- `NumberElementsOnHorizontalAxis`: Number of columns (y axis)
- `NumberLevels`: Number of levels (z axis)
- `VerticalSpacing`: Spacing between rows
- `HorizontalSpacing`: Spacing between columns
- `SpacingBetweenLevels`: Spacing between levels
- `EntitiesArray`: Array of entities from which to create the linear pattern in 3D space

## Remarks

| VerticalSpacing, HorizontalSpacing, and SpacingBetweenLevels... | Generate the pattern along... |
| --- | --- |
| Positive values | Positive x, y, and z axes |
| Negative values | Negative x, y, and z axes |

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::PatternLinear Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternLinear.html)
[ISketchManager::Pattern3DCircular Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Pattern3DCircular.html)
[ISketchManager::PatternCircular Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternCircular.html)

## Availability

DraftSight V1R4.0
