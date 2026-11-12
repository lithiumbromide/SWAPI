---
title: "CopyEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "CopyEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CopyEntities.html"
---

# CopyEntities Method (ISketchManager)

Obsolete. Superseded by [ISketchManager::CopyEntities2](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~CopyEntities2.html).

## Syntax

### Visual Basic

```vb
Sub CopyEntities( _
   ByVal DisplacementX As System.Double, _
   ByVal DisplacementY As System.Double, _
   ByVal DisplacementZ As System.Double, _
   ByVal EntityTypeLongArray As System.Object, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void CopyEntities(
   System.double DisplacementX,
   System.double DisplacementY,
   System.double DisplacementZ,
   System.object EntityTypeLongArray,
   System.object EntitiesArray
)
```

### JScript

```
function CopyEntities(
   DisplacementX : System.double,
   DisplacementY : System.double,
   DisplacementZ : System.double,
   EntityTypeLongArray : System.Object,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void CopyEntities(
   System.double DisplacementX,
   System.double DisplacementY,
   System.double DisplacementZ,
   System.Object* EntityTypeLongArray,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void CopyEntities(
   System.double DisplacementX,
   System.double DisplacementY,
   System.double DisplacementZ,
   System.Object^ EntityTypeLongArray,
   System.Object^ EntitiesArray
)
```

### Parameters

- `DisplacementX`: x delta of the relative location for the displacement
- `DisplacementY`: y delta of the relative location for the displacement
- `DisplacementZ`: z delta of the relative location for the displacement
- `EntityTypeLongArray`: Array of longs indicating the types of entities to copy as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)
- `EntitiesArray`: Array of objects of the entities to copy

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::MirrorEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MirrorEntities.html)
[ISketchManager::PatternCircular Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternCircular.html)
[ISketchManager::PatternLinear Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~PatternLinear.html)
[ISketchManager::RotateEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RotateEntities.html)
[ISketchManager::ScaleEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ScaleEntities.html)
[ISketchManager::ExtendEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtendEntities.html)
[ISketchManager::MoveEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~MoveEntities.html)
[ISketchManager::StretchEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~StretchEntities.html)
[ISketchManager::TrimEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~TrimEntities.html)
[ISketchManager::ChamferEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferEntities.html)
[ISketchManager::FilletEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletEntities.html)

## Availability

DraftSight V1R1.3
