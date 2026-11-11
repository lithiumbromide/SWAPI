---
title: "BringAboveEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "BringAboveEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~BringAboveEntities.html"
---

# BringAboveEntities Method (ISketchManager)

Moves the specified entities above the specified reference entities.

## Syntax

### Visual Basic

```vb
Sub BringAboveEntities( _
   ByVal EntitiesArray As System.Object, _
   ByVal ReferenceEntitiesArray As System.Object _
)
```

### C#

```csharp
void BringAboveEntities(
   System.object EntitiesArray,
   System.object ReferenceEntitiesArray
)
```

### JScript

```
function BringAboveEntities(
   EntitiesArray : System.Object,
   ReferenceEntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void BringAboveEntities(
   System.Object* EntitiesArray,
   System.Object* ReferenceEntitiesArray
)
```

### C++/CLI

```cpp
void BringAboveEntities(
   System.Object^ EntitiesArray,
   System.Object^ ReferenceEntitiesArray
)
```

### Parameters

- `EntitiesArray`: Array of entities to move above ReferenceEntitiesArray
- `ReferenceEntitiesArray`: Array of reference entities

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::BringToFrontEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~BringToFrontEntities.html)
[ISketchManager::SendToBackEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SendToBackEntities.html)
[ISketchManager::SendToUnderEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SendToUnderEntities.html)

## Availability

DraftSight V1R4.0
