---
title: "SetTransparency Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "SetTransparency"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~SetTransparency.html"
---

# SetTransparency Method (IEntityHelper)

Sets the transparency object for the specified entity.

## Syntax

### Visual Basic

```vb
Sub SetTransparency( _
   ByVal Obj As System.Object, _
   ByVal Val As Transparency _
)
```

### C#

```csharp
void SetTransparency(
   System.object Obj,
   Transparency Val
)
```

### JScript

```
function SetTransparency(
   Obj : System.Object,
   Val : Transparency
);
```

### Managed Extensions for C++

```
void SetTransparency(
   System.Object* Obj,
   Transparency* Val
)
```

### C++/CLI

```cpp
void SetTransparency(
   System.Object^ Obj,
   Transparency^ Val
)
```

### Parameters

- `Obj`: Entity for which to set its transparency object
- `Val`: [Transparency](Interop.dsAutomation~Interop.dsAutomation.ITransparency.html) object

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::GetTransparency Method ()](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetTransparency.html)

## Availability

DraftSight V1R6.0
