---
title: "SetID Method (IContextMenuItem)"
project: ""
interface: "IContextMenuItem"
member: "SetID"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~SetID.html"
---

# SetID Method (IContextMenuItem)

Sets the user-defined ID of this context-sensitive menu item.

## Syntax

### Visual Basic

```vb
Sub SetID( _
   ByVal NewVal As System.String _
)
```

### C#

```csharp
void SetID(
   System.string NewVal
)
```

### JScript

```
function SetID(
   NewVal : System.String
);
```

### Managed Extensions for C++

```
void SetID(
   System.string* NewVal
)
```

### C++/CLI

```cpp
void SetID(
   System.String^ NewVal
)
```

### Parameters

- `NewVal`: Unique ID of this context-sensitive menu item

## Remarks

Use a GUID tool to generate a unique NewVal.

It is recommended that you set the IDs of only custom controls. Do not attempt to change the IDs of system controls, as they are used for internal processing.

## See Also

[IContextMenuItem Interface](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem.html)
[IContextMenuItem Members](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem_members.html)
[IContextMenuItem::GetID Method ()](Interop.dsAutomation~Interop.dsAutomation.IContextMenuItem~GetID.html)

## Availability

DraftSight 2019 SP0
