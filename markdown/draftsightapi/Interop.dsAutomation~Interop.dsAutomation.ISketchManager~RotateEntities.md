---
title: "RotateEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "RotateEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RotateEntities.html"
---

# RotateEntities Method (ISketchManager)

Rotates the specified entities.

## Syntax

### Visual Basic

```vb
Sub RotateEntities( _
   ByVal PivotPointX As System.Double, _
   ByVal PivotPointY As System.Double, _
   ByVal RotateAngle As System.Double, _
   ByVal EntityTypeLongArray As System.Object, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void RotateEntities(
   System.double PivotPointX,
   System.double PivotPointY,
   System.double RotateAngle,
   System.object EntityTypeLongArray,
   System.object EntitiesArray
)
```

### JScript

```
function RotateEntities(
   PivotPointX : System.double,
   PivotPointY : System.double,
   RotateAngle : System.double,
   EntityTypeLongArray : System.Object,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void RotateEntities(
   System.double PivotPointX,
   System.double PivotPointY,
   System.double RotateAngle,
   System.Object* EntityTypeLongArray,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void RotateEntities(
   System.double PivotPointX,
   System.double PivotPointY,
   System.double RotateAngle,
   System.Object^ EntityTypeLongArray,
   System.Object^ EntitiesArray
)
```

### Parameters

- `PivotPointX`: x coordinate of the pivot point about which rotation occurs
- `PivotPointY`: y coordinate of the pivot point about which rotation occurs
- `RotateAngle`: Rotation angle
- `EntityTypeLongArray`: Array of longs of the types of entities to rotate as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)
- `EntitiesArray`: Array of objects of the entities to rotate

## Examples

[Rotate and Copy Entities (C#)](Rotate_and_Copy_Entities_Example_CSharp.htm)
[Rotate and Copy Entities (VB.NET)](Rotate_and_Copy_Entities_Example_VBNET.htm)
[Rotate and Copy Entities (VBA)](Rotate_and_Copy_Entities_Example_VBA.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::Rotate3DEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Rotate3DEntities.html)

## Availability

DraftSight V1R1.3
