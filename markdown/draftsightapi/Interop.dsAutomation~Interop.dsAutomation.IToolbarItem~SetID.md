---
title: "SetID Method (IToolbarItem)"
project: ""
interface: "IToolbarItem"
member: "SetID"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IToolbarItem~SetID.html"
---

# SetID Method (IToolbarItem)

Sets the user-defined ID of this toolbar item.

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

- `NewVal`: Unique ID of this toolbar item

## Remarks

Use a GUID tool to generate a unique NewVal.

It is recommended that you set the IDs of only custom controls. Do not attempt to change the IDs of system controls, as they are used for internal processing.

## See Also

[IToolbarItem Interface](Interop.dsAutomation~Interop.dsAutomation.IToolbarItem.html)
[IToolbarItem Members](Interop.dsAutomation~Interop.dsAutomation.IToolbarItem_members.html)
[IToolbarItem::GetID Method ()](Interop.dsAutomation~Interop.dsAutomation.IToolbarItem~GetID.html)

## Availability

DraftSight 2019 SP0
