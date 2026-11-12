---
title: "GetRibbonRowItems Method (IRibbonRow)"
project: ""
interface: "IRibbonRow"
member: "GetRibbonRowItems"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonRow~GetRibbonRowItems.html"
---

# GetRibbonRowItems Method (IRibbonRow)

Gets all of the items in this ribbon row.

## Syntax

### Visual Basic

```vb
Function GetRibbonRowItems() As System.Object
```

### C#

```csharp
System.object GetRibbonRowItems()
```

### JScript

```
function GetRibbonRowItems() : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetRibbonRowItems();
```

### C++/CLI

```cpp
System.Object^ GetRibbonRowItems();
```

### Return Value

Array of [IRibbonRowItem](Interop.dsAutomation~Interop.dsAutomation.IRibbonRowItem.html)s

## Examples

See the [IRibbonRow](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html) example.

## Remarks

After calling this method, use [IRibbonRowItem::GetType](Interop.dsAutomation~Interop.dsAutomation.IRibbonRowItem~GetType.html) to determine each object in the returned array.

## See Also

[IRibbonRow Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html)
[IRibbonRow Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow_members.html)

## Availability

DraftSight 2017 SP0
