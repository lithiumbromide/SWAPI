---
title: "SetColor Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "SetColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~SetColor.html"
---

# SetColor Method (IEntityHelper)

Sets the LineColor of the specified entity.

## Syntax

### Visual Basic

```vb
Sub SetColor( _
   ByVal Obj As System.Object, _
   ByVal NewVal As Color _
)
```

### C#

```csharp
void SetColor(
   System.object Obj,
   Color NewVal
)
```

### JScript

```
function SetColor(
   Obj : System.Object,
   NewVal : Color
);
```

### Managed Extensions for C++

```
void SetColor(
   System.Object* Obj,
   Color* NewVal
)
```

### C++/CLI

```cpp
void SetColor(
   System.Object^ Obj,
   Color^ NewVal
)
```

### Parameters

- `Obj`: Entity
- `NewVal`: [LineColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Examples

[Insert Splines (C#)](Insert_Splines_Example_CSharp.htm)
[Insert Splines (VB.NET)](Insert_Splines_Example_VBNET.htm)
[Insert Splines (VBA)](Insert_Splines_Example_VBA.htm)
[Select and Change Entities (JavaScript)](Select_and_Change_Entities_Example_JS.htm)
[Create and Change EntityGroups (C#)](Create_and_Change_EntityGroups_Example_CSharp.htm)
[Create and Change EntityGroups (VB.NET)](Create_and_Change_EntityGroups_Example_VBNET.htm)
[Create and Change EntityGroups (VBA)](Create_and_Change_EntityGroups_Example_VBA.htm)
[Create and Change EntityGroups (JavaScript)](Create_and_Change_EntityGroups_Example_JS.htm)

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::GetColor Method](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetColor.html)

## Availability

DraftSight V1R3.0
