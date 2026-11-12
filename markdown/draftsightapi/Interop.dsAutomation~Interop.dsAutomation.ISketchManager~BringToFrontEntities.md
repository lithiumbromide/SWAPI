---
title: "BringToFrontEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "BringToFrontEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~BringToFrontEntities.html"
---

# BringToFrontEntities Method (ISketchManager)

Moves the specified entities to the top of the drawing order.

## Syntax

### Visual Basic

```vb
Sub BringToFrontEntities( _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void BringToFrontEntities(
   System.object EntitiesArray
)
```

### JScript

```
function BringToFrontEntities(
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void BringToFrontEntities(
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void BringToFrontEntities(
   System.Object^ EntitiesArray
)
```

### Parameters

- `EntitiesArray`: Array of entities to move to the top of the drawing order

## Remarks

The specified entities become the last-drawn entities in the drawing.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::BringAboveEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~BringAboveEntities.html)
[ISketchManager::SendToBackEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SendToBackEntities.html)
[ISketchManager::SendToUnderEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SendToUnderEntities.html)

## Availability

DraftSight V1R4.0
