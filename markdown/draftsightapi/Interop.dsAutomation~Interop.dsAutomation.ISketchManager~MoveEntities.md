---
title: "MoveEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "MoveEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MoveEntities.html"
---

# MoveEntities Method (ISketchManager)

Moves the specified sketch entities to the specified relative location.

## Syntax

### Visual Basic

```vb
Sub MoveEntities( _
   ByVal DisplacementX As System.Double, _
   ByVal DisplacementY As System.Double, _
   ByVal DisplacementZ As System.Double, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void MoveEntities(
   System.double DisplacementX,
   System.double DisplacementY,
   System.double DisplacementZ,
   System.object EntitiesArray
)
```

### JScript

```
function MoveEntities(
   DisplacementX : System.double,
   DisplacementY : System.double,
   DisplacementZ : System.double,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void MoveEntities(
   System.double DisplacementX,
   System.double DisplacementY,
   System.double DisplacementZ,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void MoveEntities(
   System.double DisplacementX,
   System.double DisplacementY,
   System.double DisplacementZ,
   System.Object^ EntitiesArray
)
```

### Parameters

- `DisplacementX`: Distance to move the entity along the x axis
- `DisplacementY`: Distance to move the entity along the y axis
- `DisplacementZ`: Distance to move the entity along the z axis
- `EntitiesArray`: Array of entities to move

## Remarks

This method works like the DraftSight MOVE command to move sketch entities.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::CopyEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CopyEntities.html)
[ISketchManager::ExtendEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtendEntities.html)
[ISketchManager::GetEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)
[ISketchManager::MirrorEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MirrorEntities.html)
[ISketchManager::RotateEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RotateEntities.html)
[ISketchManager::ScaleEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ScaleEntities.html)
[ISketchManager::StretchEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StretchEntities.html)
[ISketchManager::TrimEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~TrimEntities.html)
[ISketchManager::ChamferEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferEntities.html)
[ISketchManager::FilletEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletEntities.html)

## Availability

DraftSight V1R1.4
