---
title: "ChamferEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "ChamferEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferEntities.html"
---

# ChamferEntities Method (ISketchManager)

Connects two sketch entities that meet in a beveled corner.

## Syntax

### Visual Basic

```vb
Sub ChamferEntities( _
   ByVal FirstPointOnEntityDblArray As System.Object, _
   ByVal FirstEntityArray As System.Object, _
   ByVal SecondPointOnEntityDblArray As System.Object, _
   ByVal SecondEntityArray As System.Object _
)
```

### C#

```csharp
void ChamferEntities(
   System.object FirstPointOnEntityDblArray,
   System.object FirstEntityArray,
   System.object SecondPointOnEntityDblArray,
   System.object SecondEntityArray
)
```

### JScript

```
function ChamferEntities(
   FirstPointOnEntityDblArray : System.Object,
   FirstEntityArray : System.Object,
   SecondPointOnEntityDblArray : System.Object,
   SecondEntityArray : System.Object
);
```

### Managed Extensions for C++

```
void ChamferEntities(
   System.Object* FirstPointOnEntityDblArray,
   System.Object* FirstEntityArray,
   System.Object* SecondPointOnEntityDblArray,
   System.Object* SecondEntityArray
)
```

### C++/CLI

```cpp
void ChamferEntities(
   System.Object^ FirstPointOnEntityDblArray,
   System.Object^ FirstEntityArray,
   System.Object^ SecondPointOnEntityDblArray,
   System.Object^ SecondEntityArray
)
```

### Parameters

- `FirstPointOnEntityDblArray`: Array of the doubles of x, y, and z coordinates of points on the entities in FirstEntityArray; these points define the sides of the entities that you want to chamfer
- `FirstEntityArray`: Array of sketch entities to chamfer (see **Remarks**)
- `SecondPointOnEntityDblArray`: Array of the doubles of x, y, and z coordinates of points on the entities in SecondEntityArray; these points define the sides of the entities that you want to chamfer
- `SecondEntityArray`: Array of sketch entities to chamfer (see **Remarks**)

## Remarks

This method works like the DraftSight CHAMFER command to chamfer sketch entities, except that entities are modified even if the specified points would not select the entities. Internally, the entity closest to the pick point is taken.

This method creates a chamfer for each FirstEntityArray[i] - SecondEntityArray[i] pair.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::ChamferPolyLine Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferPolyLine.html)
[ISketchManager::CopyEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CopyEntities.html)
[ISketchManager::ExtendEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtendEntities.html)
[ISketchManager::FilletEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletEntities.html)
[ISketchManager::GetEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)
[ISketchManager::MirrorEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MirrorEntities.html)
[ISketchManager::MoveEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MoveEntities.html)
[ISketchManager::RotateEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RotateEntities.html)
[ISketchManager::ScaleEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ScaleEntities.html)
[ISketchManager::StretchEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StretchEntities.html)
[ISketchManager::TrimEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~TrimEntities.html)

## Availability

DraftSight V1R1.4
