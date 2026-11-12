---
title: "SetLineWeight Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "SetLineWeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~SetLineWeight.html"
---

# SetLineWeight Method (IEntityHelper)

Sets the LineWeight for the specified entity.

## Syntax

### Visual Basic

```vb
Sub SetLineWeight( _
   ByVal Obj As System.Object, _
   ByVal NewVal As dsLineWeight_e _
)
```

### C#

```csharp
void SetLineWeight(
   System.object Obj,
   dsLineWeight_e NewVal
)
```

### JScript

```
function SetLineWeight(
   Obj : System.Object,
   NewVal : dsLineWeight_e
);
```

### Managed Extensions for C++

```
void SetLineWeight(
   System.Object* Obj,
   dsLineWeight_e NewVal
)
```

### C++/CLI

```cpp
void SetLineWeight(
   System.Object^ Obj,
   dsLineWeight_e NewVal
)
```

### Parameters

- `Obj`: Entity
- `NewVal`: LineWeight as defined in [dsLineWeight_e](Interop.dsAutomation~Interop.dsAutomation.dsLineWeight_e.html)

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::GetLineWeight Method](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetLineWeight.html)

## Availability

DraftSight V1R3.0
