---
title: "PatternCircular Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "PatternCircular"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternCircular.html"
---

# PatternCircular Method (ISketchManager)

Creates a circular pattern of the specified entities.

## Syntax

### Visual Basic

```vb
Sub PatternCircular( _
   ByVal BasePatternOn As dsBasePatternOn_e, _
   ByVal AngleBetween As System.Double, _
   ByVal FillAngle As System.Double, _
   ByVal TotalNumber As System.Integer, _
   ByVal ElementBasePointX As System.Double, _
   ByVal ElementBasePointY As System.Double, _
   ByVal AxisPointX As System.Double, _
   ByVal AxisPointY As System.Double, _
   ByVal OrientElementsAboutAxis As System.Boolean, _
   ByVal EntityTypeLongArray As System.Object, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void PatternCircular(
   dsBasePatternOn_e BasePatternOn,
   System.double AngleBetween,
   System.double FillAngle,
   System.int TotalNumber,
   System.double ElementBasePointX,
   System.double ElementBasePointY,
   System.double AxisPointX,
   System.double AxisPointY,
   System.bool OrientElementsAboutAxis,
   System.object EntityTypeLongArray,
   System.object EntitiesArray
)
```

### JScript

```
function PatternCircular(
   BasePatternOn : dsBasePatternOn_e,
   AngleBetween : System.double,
   FillAngle : System.double,
   TotalNumber : System.int,
   ElementBasePointX : System.double,
   ElementBasePointY : System.double,
   AxisPointX : System.double,
   AxisPointY : System.double,
   OrientElementsAboutAxis : System.boolean,
   EntityTypeLongArray : System.Object,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void PatternCircular(
   dsBasePatternOn_e BasePatternOn,
   System.double AngleBetween,
   System.double FillAngle,
   System.int TotalNumber,
   System.double ElementBasePointX,
   System.double ElementBasePointY,
   System.double AxisPointX,
   System.double AxisPointY,
   System.bool OrientElementsAboutAxis,
   System.Object* EntityTypeLongArray,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void PatternCircular(
   dsBasePatternOn_e BasePatternOn,
   System.double AngleBetween,
   System.double FillAngle,
   System.int TotalNumber,
   System.double ElementBasePointX,
   System.double ElementBasePointY,
   System.double AxisPointX,
   System.double AxisPointY,
   System.bool OrientElementsAboutAxis,
   System.Object^ EntityTypeLongArray,
   System.Object^ EntitiesArray
)
```

### Parameters

- `BasePatternOn`: Base pattern type as defined in [dsBasePatternOn_e](Interop.dsAutomation~Interop.dsAutomation.dsBasePatternOn_e.html)
- `AngleBetween`: Angle between the base points of the pattern entities and the center of the pattern; valid when dsBasePatternOn is dsBasePatternOn_e.AngleBetweenAndElementsNumbers or dsBasePatternOn_e.dsBasePatternOn_FillAngleAndAngleBetween; in radians
- `FillAngle`: Positive or negative value for the fill angle; valid when BasePatternOn is dsBasePatternOn_e.dsBasePatternOn_FillAngleAndAngleBetween or dsBasePatternOn_e.dsBasePatternOn_FillAngleAndElementsNumber; in radians
- `TotalNumber`: Total number of entities in the pattern, including the original entity
- `ElementBasePointX`: x coordinate of the base point of the pattern
- `ElementBasePointY`: y coordinate of the base point of the pattern
- `AxisPointX`: x coordinate for the center point of the pattern
- `AxisPointY`: y coordinate for the center point of the pattern
- `OrientElementsAboutAxis`: True to rotate the entities as they are patterned, false to align the entities to the source entity
- `EntityTypeLongArray`: Array of longs of the types of entities as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)
- `EntitiesArray`: Array of entities to pattern

## Examples

[Create Circular Pattern (C#)](Create_Circular_Pattern_Example_CSharp.htm)
[Create Circular Pattern (VB.NET)](Create_Circular_Pattern_Example_VBNET.htm)
[Create Circular Pattern (VBA)](Create_Circular_Pattern_Example_VBA.htm)
[Create Circular Pattern (JavaScript)](Create_Circular_Pattern_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::PatternLinear Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternLinear.html)
[ISketchManager::Pattern3DLinear Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Pattern3DLinear.html)
[ISketchManager::PatternCircular Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternCircular.html)
[ISketchManager::Pattern3DCircular Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Pattern3DCircular.html)

## Availability

DraftSight V1R1.3
