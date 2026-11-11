---
title: "SetErased Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "SetErased"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~SetErased.html"
---

# SetErased Method (IEntityHelper)

Erases or restores the specified entity.

## Syntax

### Visual Basic

```vb
Sub SetErased( _
   ByVal Obj As System.Object, _
   ByVal NewVal As System.Boolean _
)
```

### C#

```csharp
void SetErased(
   System.object Obj,
   System.bool NewVal
)
```

### JScript

```
function SetErased(
   Obj : System.Object,
   NewVal : System.boolean
);
```

### Managed Extensions for C++

```
void SetErased(
   System.Object* Obj,
   System.bool NewVal
)
```

### C++/CLI

```cpp
void SetErased(
   System.Object^ Obj,
   System.bool NewVal
)
```

### Parameters

- `Obj`: Entity
- `NewVal`: True to erase the specified entity from the group of entities, false to restore it (see **Remarks**)

## Remarks

| If this property is set to true... | Then the entity... |
| --- | --- |
| and the drawing remains open | is not displayed and can be restored by setting this property to false. |
| when the drawing is closed | is deleted from the drawing and cannot be restored. |

To determine if an entity is erased, call [IEntityHelper::GetErased](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetErased.html)

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)

## Availability

DraftSight V1R5.0
