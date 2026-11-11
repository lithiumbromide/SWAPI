---
title: "TrimEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "TrimEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~TrimEntities.html"
---

# TrimEntities Method (ISketchManager)

Trims the specified sketch entities.

## Syntax

### Visual Basic

```vb
Sub TrimEntities( _
   ByVal CuttingEntitiesArray As System.Object, _
   ByVal EntitiesToRemoveArray As System.Object, _
   ByVal PointOnEntityDblArray As System.Object _
)
```

### C#

```csharp
void TrimEntities(
   System.object CuttingEntitiesArray,
   System.object EntitiesToRemoveArray,
   System.object PointOnEntityDblArray
)
```

### JScript

```
function TrimEntities(
   CuttingEntitiesArray : System.Object,
   EntitiesToRemoveArray : System.Object,
   PointOnEntityDblArray : System.Object
);
```

### Managed Extensions for C++

```
void TrimEntities(
   System.Object* CuttingEntitiesArray,
   System.Object* EntitiesToRemoveArray,
   System.Object* PointOnEntityDblArray
)
```

### C++/CLI

```cpp
void TrimEntities(
   System.Object^ CuttingEntitiesArray,
   System.Object^ EntitiesToRemoveArray,
   System.Object^ PointOnEntityDblArray
)
```

### Parameters

- `CuttingEntitiesArray`: Array of entities that are used as potential cutting edges; use Lines, InfiniteLines, Rays, PolyLines, Circles, Arcs, and Ellipses as cutting edges to trim the entities in EntitiesToRemoveArray
- `EntitiesToRemoveArray`: Array of entities to trim
- `PointOnEntityDblArray`: Array of the doubles of x, y, and z coordinates of the points on the entities in EntitiesToRemoveArray; these points define the sides of the entities that you want to trim

## Remarks

This method works like the DraftSight TRIM command to trim sketch entities.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::CopyEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CopyEntities.html)
[ISketchManager::ExtendEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtendEntities.html)
[ISketchManager::GetEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)
[ISketchManager::MirrorEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MirrorEntities.html)
[ISketchManager::MoveEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MoveEntities.html)
[ISketchManager::RotateEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RotateEntities.html)
[ISketchManager::ScaleEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ScaleEntities.html)
[ISketchManager::StretchEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StretchEntities.html)
[ISketchManager::ChamferEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferEntities.html)
[ISketchManager::FilletEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletEntities.html)

## Availability

DraftSight V1R1.4
