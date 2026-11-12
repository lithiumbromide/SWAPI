---
title: "InsertRibbonQuickAccessBarItem Method (IRibbonQuickAccessBar)"
project: ""
interface: "IRibbonQuickAccessBar"
member: "InsertRibbonQuickAccessBarItem"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonQuickAccessBar~InsertRibbonQuickAccessBarItem.html"
---

# InsertRibbonQuickAccessBarItem Method (IRibbonQuickAccessBar)

Inserts the specified toolbar item into this ribbon quick access toolbar.

## Syntax

### Visual Basic

```vb
Function InsertRibbonQuickAccessBarItem( _
   ByVal ApiUuid As System.String, _
   ByVal ItemName As System.String, _
   ByVal UserCmdID As System.String _
) As RibbonQuickAccessBarItem
```

### C#

```csharp
RibbonQuickAccessBarItem InsertRibbonQuickAccessBarItem(
   System.string ApiUuid,
   System.string ItemName,
   System.string UserCmdID
)
```

### JScript

```
function InsertRibbonQuickAccessBarItem(
   ApiUuid : System.String,
   ItemName : System.String,
   UserCmdID : System.String
) : RibbonQuickAccessBarItem;
```

### Managed Extensions for C++

```
RibbonQuickAccessBarItem* InsertRibbonQuickAccessBarItem(
   System.string* ApiUuid,
   System.string* ItemName,
   System.string* UserCmdID
)
```

### C++/CLI

```cpp
RibbonQuickAccessBarItem^ InsertRibbonQuickAccessBarItem(
   System.String^ ApiUuid,
   System.String^ ItemName,
   System.String^ UserCmdID
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `ItemName`: Name of the quick access toolbar item to insert
- `UserCmdID`: User-defined command ID

### Return Value

[IRibbonQuickAccessBarItem](Interop.dsAutomation~Interop.dsAutomation.IRibbonQuickAccessBarItem.html)

## Examples

See the [IRibbonQuickAccessBar](Interop.dsAutomation~Interop.dsAutomation.IRibbonQuickAccessBar.html) example.

## See Also

[IRibbonQuickAccessBar Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonQuickAccessBar.html)
[IRibbonQuickAccessBar Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonQuickAccessBar_members.html)

## Availability

DraftSight 2017 SP0
