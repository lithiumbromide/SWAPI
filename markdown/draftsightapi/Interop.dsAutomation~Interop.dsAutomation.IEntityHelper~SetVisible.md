---
title: "SetVisible Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "SetVisible"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~SetVisible.html"
---

# SetVisible Method (IEntityHelper)

Sets whether to show the specified entity.

## Syntax

### Visual Basic

```vb
Sub SetVisible( _
   ByVal Obj As System.Object, _
   ByVal NewVal As System.Boolean _
)
```

### C#

```csharp
void SetVisible(
   System.object Obj,
   System.bool NewVal
)
```

### JScript

```
function SetVisible(
   Obj : System.Object,
   NewVal : System.boolean
);
```

### Managed Extensions for C++

```
void SetVisible(
   System.Object* Obj,
   System.bool NewVal
)
```

### C++/CLI

```cpp
void SetVisible(
   System.Object^ Obj,
   System.bool NewVal
)
```

### Parameters

- `Obj`: Entity
- `NewVal`: True to show the specified entity, false to hide it

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::GetVisible Method](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetVisible.html)

## Availability

DraftSight V1R3.0
