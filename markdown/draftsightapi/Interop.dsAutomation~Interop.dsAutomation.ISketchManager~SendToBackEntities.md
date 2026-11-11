---
title: "SendToBackEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "SendToBackEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SendToBackEntities.html"
---

# SendToBackEntities Method (ISketchManager)

Moves the specified entities to the bottom of the drawing order.

## Syntax

### Visual Basic

```vb
Sub SendToBackEntities( _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void SendToBackEntities(
   System.object EntitiesArray
)
```

### JScript

```
function SendToBackEntities(
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void SendToBackEntities(
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void SendToBackEntities(
   System.Object^ EntitiesArray
)
```

### Parameters

- `EntitiesArray`: Array of entities to move to the bottom of the drawing order

## Remarks

The specified entities become the first-drawn entities in the drawing.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::BringAboveEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~BringAboveEntities.html)
[ISketchManager::BringToFrontEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~BringToFrontEntities.html)
[ISketchManager::SendToUnderEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SendToUnderEntities.html)

## Availability

DraftSight V1R4.0
