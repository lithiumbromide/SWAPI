---
title: "SetID Method (IMenuItem)"
project: ""
interface: "IMenuItem"
member: "SetID"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMenuItem~SetID.html"
---

# SetID Method (IMenuItem)

Sets the user-defined ID of this menu item.

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

- `NewVal`: Unique ID of this menu item

## Remarks

Use a GUID tool to generate a unique NewVal.

It is recommended that you set the IDs of only custom controls. Do not attempt to change the IDs of system controls, as they are used for internal processing.

## See Also

[IMenuItem Interface](Interop.dsAutomation~Interop.dsAutomation.IMenuItem.html)
[IMenuItem Members](Interop.dsAutomation~Interop.dsAutomation.IMenuItem_members.html)
[IMenuItem::GetID Method ()](Interop.dsAutomation~Interop.dsAutomation.IMenuItem~GetID.html)

## Availability

DraftSight 2019 SP0
