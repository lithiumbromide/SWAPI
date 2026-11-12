---
title: "DetachImageDefinition Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "DetachImageDefinition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~DetachImageDefinition.html"
---

# DetachImageDefinition Method (ISketchManager)

Detaches the specified image definition from the drawing.

## Syntax

### Visual Basic

```vb
Function DetachImageDefinition( _
   ByVal ImageDefinition As ImageDefinition _
) As System.Boolean
```

### C#

```csharp
System.bool DetachImageDefinition(
   ImageDefinition ImageDefinition
)
```

### JScript

```
function DetachImageDefinition(
   ImageDefinition : ImageDefinition
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool DetachImageDefinition(
   ImageDefinition* ImageDefinition
)
```

### C++/CLI

```cpp
System.bool DetachImageDefinition(
   ImageDefinition^ ImageDefinition
)
```

### Parameters

- `ImageDefinition`: Image definition

### Return Value

True if successful, false if not

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertPicture Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPicture.html)

## Availability

DraftSight 2024 SP02
