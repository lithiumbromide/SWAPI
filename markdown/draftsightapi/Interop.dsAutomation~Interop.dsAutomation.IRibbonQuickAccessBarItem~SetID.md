---
title: "SetID Method (IRibbonQuickAccessBarItem)"
project: ""
interface: "IRibbonQuickAccessBarItem"
member: "SetID"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonQuickAccessBarItem~SetID.html"
---

# SetID Method (IRibbonQuickAccessBarItem)

Sets the user-defined ID of this ribbon quick access toolbar item.

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

- `NewVal`: Unique ID of this ribbon quick access bar item

## Remarks

Use a GUID tool to generate a unique NewVal.

It is recommended that you set the IDs of only custom controls. Do not attempt to change the IDs of system controls, as they are used for internal processing.

## See Also

[IRibbonQuickAccessBarItem Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonQuickAccessBarItem.html)
[IRibbonQuickAccessBarItem Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonQuickAccessBarItem_members.html)
[IRibbonQuickAccessBarItem::GetID Method ()](Interop.dsAutomation~Interop.dsAutomation.IRibbonQuickAccessBarItem~GetID.html)

## Availability

DraftSight 2019 SP0
