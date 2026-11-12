---
title: "InsertRibbonSystemMenuItem Method (IRibbonSystemMenuItem)"
project: ""
interface: "IRibbonSystemMenuItem"
member: "InsertRibbonSystemMenuItem"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenuItem~InsertRibbonSystemMenuItem.html"
---

# InsertRibbonSystemMenuItem Method (IRibbonSystemMenuItem)

Inserts the specified menu item beneath this menu item in the ribbon system menu.

## Syntax

### Visual Basic

```vb
Function InsertRibbonSystemMenuItem( _
   ByVal ApiUuid As System.String, _
   ByVal ItemType As dsRibbonItemType_e, _
   ByVal ItemName As System.String, _
   ByVal UserCmdID As System.String _
) As RibbonSystemMenuItem
```

### C#

```csharp
RibbonSystemMenuItem InsertRibbonSystemMenuItem(
   System.string ApiUuid,
   dsRibbonItemType_e ItemType,
   System.string ItemName,
   System.string UserCmdID
)
```

### JScript

```
function InsertRibbonSystemMenuItem(
   ApiUuid : System.String,
   ItemType : dsRibbonItemType_e,
   ItemName : System.String,
   UserCmdID : System.String
) : RibbonSystemMenuItem;
```

### Managed Extensions for C++

```
RibbonSystemMenuItem* InsertRibbonSystemMenuItem(
   System.string* ApiUuid,
   dsRibbonItemType_e ItemType,
   System.string* ItemName,
   System.string* UserCmdID
)
```

### C++/CLI

```cpp
RibbonSystemMenuItem^ InsertRibbonSystemMenuItem(
   System.String^ ApiUuid,
   dsRibbonItemType_e ItemType,
   System.String^ ItemName,
   System.String^ UserCmdID
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `ItemType`: Ribbon item type as defined in [dsRibbonItemType_e](Interop.dsAutomation~Interop.dsAutomation.dsRibbonItemType_e.html) (see **Remarks**)
- `ItemName`: Name of the system menu item to insert (see **Remarks**)
- `UserCmdID`: User-defined command ID (see **Remarks**)

### Return Value

[IRibbonSystemMenuItem](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenuItem.html)

## Remarks

Ribbon system menu items can be nested only one level deep.

If ItemType is dsRibbonItemType_e.dsRibbonItemType_Separator, then set ItemName to an empty string and UserCmdID to Nothing or null.

## See Also

[IRibbonSystemMenuItem Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenuItem.html)
[IRibbonSystemMenuItem Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenuItem_members.html)
[IRibbonSystemMenu::InsertRibbonSystemMenuItem Method ()](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenu~InsertRibbonSystemMenuItem.html)

## Availability

DraftSight 2017 SP0
