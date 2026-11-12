---
title: "PatternLinear Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "PatternLinear"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternLinear.html"
---

# PatternLinear Method (ISketchManager)

Creates a linear pattern of the specified entities

## Syntax

### Visual Basic

```vb
Sub PatternLinear( _
   ByVal NumberElementsOnVerticalAxis As System.Integer, _
   ByVal NumberElementsOnHorizontalAxis As System.Integer, _
   ByVal SpacingOnVerticalAxis As System.Double, _
   ByVal SpacingOnHorizontalAxis As System.Double, _
   ByVal PatternAngle As System.Double, _
   ByVal EntityTypeLongArray As System.Object, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void PatternLinear(
   System.int NumberElementsOnVerticalAxis,
   System.int NumberElementsOnHorizontalAxis,
   System.double SpacingOnVerticalAxis,
   System.double SpacingOnHorizontalAxis,
   System.double PatternAngle,
   System.object EntityTypeLongArray,
   System.object EntitiesArray
)
```

### JScript

```
function PatternLinear(
   NumberElementsOnVerticalAxis : System.int,
   NumberElementsOnHorizontalAxis : System.int,
   SpacingOnVerticalAxis : System.double,
   SpacingOnHorizontalAxis : System.double,
   PatternAngle : System.double,
   EntityTypeLongArray : System.Object,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void PatternLinear(
   System.int NumberElementsOnVerticalAxis,
   System.int NumberElementsOnHorizontalAxis,
   System.double SpacingOnVerticalAxis,
   System.double SpacingOnHorizontalAxis,
   System.double PatternAngle,
   System.Object* EntityTypeLongArray,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void PatternLinear(
   System.int NumberElementsOnVerticalAxis,
   System.int NumberElementsOnHorizontalAxis,
   System.double SpacingOnVerticalAxis,
   System.double SpacingOnHorizontalAxis,
   System.double PatternAngle,
   System.Object^ EntityTypeLongArray,
   System.Object^ EntitiesArray
)
```

### Parameters

- `NumberElementsOnVerticalAxis`: Number of elements for the vertical axis
- `NumberElementsOnHorizontalAxis`: Number of elements for the horizontal axis
- `SpacingOnVerticalAxis`: Distance between rows
- `SpacingOnHorizontalAxis`: Distance between columns
- `PatternAngle`: Angle to control how the copies are arranged in radians
- `EntityTypeLongArray`: Array of longs of the types of entities to pattern as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)
- `EntitiesArray`: Array of objects of the entities to pattern

## Examples

[Create Linear Pattern (C#)](Create_Linear_Pattern_Example_CSharp.htm)
[Create Linear Pattern (VB.NET)](Create_Linear_Pattern_Example_VBNET.htm)
[Create Linear Pattern (VBA)](Create_Linear_Pattern_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::Pattern3DLinear Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Pattern3DLinear.html)
[ISketchManager::PatternCircular Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternCircular.html)
[ISketchManager::Pattern3DCircular Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Pattern3DCircular.html)

## Availability

DraftSight V1R1.3
