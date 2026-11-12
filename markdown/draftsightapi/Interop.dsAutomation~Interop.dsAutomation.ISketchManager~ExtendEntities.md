---
title: "ExtendEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "ExtendEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtendEntities.html"
---

# ExtendEntities Method (ISketchManager)

Extends the specified sketch entities.

## Syntax

### Visual Basic

```vb
Sub ExtendEntities( _
   ByVal BoundaryEntitiesArray As System.Object, _
   ByVal EntitiesToExtendArray As System.Object, _
   ByVal PointOnEntityDblArray As System.Object _
)
```

### C#

```csharp
void ExtendEntities(
   System.object BoundaryEntitiesArray,
   System.object EntitiesToExtendArray,
   System.object PointOnEntityDblArray
)
```

### JScript

```
function ExtendEntities(
   BoundaryEntitiesArray : System.Object,
   EntitiesToExtendArray : System.Object,
   PointOnEntityDblArray : System.Object
);
```

### Managed Extensions for C++

```
void ExtendEntities(
   System.Object* BoundaryEntitiesArray,
   System.Object* EntitiesToExtendArray,
   System.Object* PointOnEntityDblArray
)
```

### C++/CLI

```cpp
void ExtendEntities(
   System.Object^ BoundaryEntitiesArray,
   System.Object^ EntitiesToExtendArray,
   System.Object^ PointOnEntityDblArray
)
```

### Parameters

- `BoundaryEntitiesArray`: Array of entities that make up the boundary edges
- `EntitiesToExtendArray`: Array of entities to extend
- `PointOnEntityDblArray`: Array of the doubles of x, y, and z coordinates of the points on the entities to extend; these points define the sides of the entities that you want to extend

## Remarks

This method works like the DraftSight EXTEND command to extend sketch entities.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::CopyEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CopyEntities.html)
[ISketchManager::GetEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)
[ISketchManager::MirrorEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MirrorEntities.html)
[ISketchManager::MoveEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MoveEntities.html)
[ISketchManager::RotateEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RotateEntities.html)
[ISketchManager::ScaleEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ScaleEntities.html)
[ISketchManager::StretchEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StretchEntities.html)
[ISketchManager::TrimEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~TrimEntities.html)
[ISketchManager::ChamferEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferEntities.html)
[ISketchManager::FilletEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletEntities.html)

## Availability

DraftSight V1R1.4
