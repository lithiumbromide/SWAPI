---
title: "ScaleEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "ScaleEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ScaleEntities.html"
---

# ScaleEntities Method (ISketchManager)

Scales the specified entities while keeping their proportions the same.

## Syntax

### Visual Basic

```vb
Sub ScaleEntities( _
   ByVal BasePointX As System.Double, _
   ByVal BasePointY As System.Double, _
   ByVal BasePointZ As System.Double, _
   ByVal ScaleFactor As System.Double, _
   ByVal EntityTypeLongArray As System.Object, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void ScaleEntities(
   System.double BasePointX,
   System.double BasePointY,
   System.double BasePointZ,
   System.double ScaleFactor,
   System.object EntityTypeLongArray,
   System.object EntitiesArray
)
```

### JScript

```
function ScaleEntities(
   BasePointX : System.double,
   BasePointY : System.double,
   BasePointZ : System.double,
   ScaleFactor : System.double,
   EntityTypeLongArray : System.Object,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void ScaleEntities(
   System.double BasePointX,
   System.double BasePointY,
   System.double BasePointZ,
   System.double ScaleFactor,
   System.Object* EntityTypeLongArray,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void ScaleEntities(
   System.double BasePointX,
   System.double BasePointY,
   System.double BasePointZ,
   System.double ScaleFactor,
   System.Object^ EntityTypeLongArray,
   System.Object^ EntitiesArray
)
```

### Parameters

- `BasePointX`: x coordinate of the base point (see **Remarks**)
- `BasePointY`: y coordinate of the base point (see **Remarks**)
- `BasePointZ`: z coordinate of the base point (see **Remarks**)
- `ScaleFactor`: Factor by which to scale the entities (see **Remarks**)
- `EntityTypeLongArray`: Array of longs of the types of entities to scale as defined [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)
- `EntitiesArray`: Array of objects of the entities to scale

## Remarks

The base point, if located on any of the specified entities, holds its original position during scaling, while all other points move by the same relative values in the direction of the x axis, y axis, and optional z axis. You can also select a point not on an existing entity as the base point. In this case, the distance from the base point to all other points making up the entity change by the same scale factor.

| A scaling factor... | Causes the entities to be... |
| --- | --- |
| larger than 1 | enlarged by this factor. |
| between 0 and 1 | reduced by this factor. |

For example, the scaling factor of 3 enlarges the specified entities three times, while a scaling factor of 0.25 reduces the entities to a quarter of their original size.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::CopyEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CopyEntities.html)
[ISketchManager::MirrorEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MirrorEntities.html)
[ISketchManager::PatternCircular Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternCircular.html)
[ISketchManager::PatternLinear Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternLinear.html)
[ISketchManager::RotateEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RotateEntities.html)
[ISelectionManager::GetSelectedObject Method](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)
[ISketchManager::ExtendEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtendEntities.html)
[ISketchManager::GetEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)
[ISketchManager::MoveEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MoveEntities.html)
[ISketchManager::StretchEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StretchEntities.html)
[ISketchManager::TrimEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~TrimEntities.html)
[ISketchManager::ChamferEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferEntities.html)
[ISketchManager::FilletEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletEntities.html)

## Availability

DraftSight V1R1.3
