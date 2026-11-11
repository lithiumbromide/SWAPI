---
title: "SendToUnderEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "SendToUnderEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SendToUnderEntities.html"
---

# SendToUnderEntities Method (ISketchManager)

Moves the specified entities under the specified reference entities.

## Syntax

### Visual Basic

```vb
Sub SendToUnderEntities( _
   ByVal EntitiesArray As System.Object, _
   ByVal ReferenceEntitiesArray As System.Object _
)
```

### C#

```csharp
void SendToUnderEntities(
   System.object EntitiesArray,
   System.object ReferenceEntitiesArray
)
```

### JScript

```
function SendToUnderEntities(
   EntitiesArray : System.Object,
   ReferenceEntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void SendToUnderEntities(
   System.Object* EntitiesArray,
   System.Object* ReferenceEntitiesArray
)
```

### C++/CLI

```cpp
void SendToUnderEntities(
   System.Object^ EntitiesArray,
   System.Object^ ReferenceEntitiesArray
)
```

### Parameters

- `EntitiesArray`: Array of entities to move under ReferenceEntitiesArray
- `ReferenceEntitiesArray`: Array of reference entities

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::BringAboveEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~BringAboveEntities.html)
[ISketchManager::BringToFrontEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~BringToFrontEntities.html)
[ISketchManager::SendToBackEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SendToBackEntities.html)

## Availability

DraftSight V1R4.0
