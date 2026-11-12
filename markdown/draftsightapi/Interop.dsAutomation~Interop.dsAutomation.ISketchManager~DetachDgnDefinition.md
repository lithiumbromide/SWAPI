---
title: "DetachDgnDefinition Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "DetachDgnDefinition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~DetachDgnDefinition.html"
---

# DetachDgnDefinition Method (ISketchManager)

Detaches the specified DGN definition from the drawing.

## Syntax

### Visual Basic

```vb
Function DetachDgnDefinition( _
   ByVal DgnDefinition As DgnDefinition _
) As System.Boolean
```

### C#

```csharp
System.bool DetachDgnDefinition(
   DgnDefinition DgnDefinition
)
```

### JScript

```
function DetachDgnDefinition(
   DgnDefinition : DgnDefinition
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool DetachDgnDefinition(
   DgnDefinition* DgnDefinition
)
```

### C++/CLI

```cpp
System.bool DetachDgnDefinition(
   DgnDefinition^ DgnDefinition
)
```

### Parameters

- `DgnDefinition`: Dgn definition

### Return Value

True if successful, false if not

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertDgn Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertDgn.html)

## Availability

DraftSight 2024 SP02
