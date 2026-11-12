---
title: "InsertRibbonSystemMenuItem Method (IRibbonSystemMenu)"
project: ""
interface: "IRibbonSystemMenu"
member: "InsertRibbonSystemMenuItem"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenu~InsertRibbonSystemMenuItem.html"
---

# InsertRibbonSystemMenuItem Method (IRibbonSystemMenu)

Inserts the specified menu item at the top level of this ribbon system menu.

## Syntax

### Visual Basic

```vb
Function InsertRibbonSystemMenuItem( _
   ByVal ApiUuid As System.String, _
   ByVal ItemType As dsRibbonItemType_e, _
   ByVal Position As System.Integer, _
   ByVal ItemName As System.String, _
   ByVal UserCmdID As System.String _
) As RibbonSystemMenuItem
```

### C#

```csharp
RibbonSystemMenuItem InsertRibbonSystemMenuItem(
   System.string ApiUuid,
   dsRibbonItemType_e ItemType,
   System.int Position,
   System.string ItemName,
   System.string UserCmdID
)
```

### JScript

```
function InsertRibbonSystemMenuItem(
   ApiUuid : System.String,
   ItemType : dsRibbonItemType_e,
   Position : System.int,
   ItemName : System.String,
   UserCmdID : System.String
) : RibbonSystemMenuItem;
```

### Managed Extensions for C++

```
RibbonSystemMenuItem* InsertRibbonSystemMenuItem(
   System.string* ApiUuid,
   dsRibbonItemType_e ItemType,
   System.int Position,
   System.string* ItemName,
   System.string* UserCmdID
)
```

### C++/CLI

```cpp
RibbonSystemMenuItem^ InsertRibbonSystemMenuItem(
   System.String^ ApiUuid,
   dsRibbonItemType_e ItemType,
   System.int Position,
   System.String^ ItemName,
   System.String^ UserCmdID
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `ItemType`: Ribbon item type as defined in [dsRibbonItemType_e](Interop.dsAutomation~Interop.dsAutomation.dsRibbonItemType_e.html) (see **Remarks**)
- `Position`: Position where to insert the system menu item
- `ItemName`: Name of the system menu item to insert (see **Remarks**)
- `UserCmdID`: User-defined command ID (see **Remarks**)

### Return Value

[IRibbonSystemMenuItem](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenuItem.html)

## Examples

See the [IRibbonSystemMenu](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenu.html) example.

## Remarks

Ribbon system menu items can be nested only one level deep.

If ItemType is dsRibbonItemType_e.dsRibbonItemType_Separator, then set ItemName to an empty string and UserCmdID to Nothing or null.

## See Also

[IRibbonSystemMenu Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenu.html)
[IRibbonSystemMenu Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenu_members.html)
[IRibbonSystemMenuItem::InsertRibbonSystemMenuItem Method ()](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenuItem~InsertRibbonSystemMenuItem.html)

## Availability

DraftSight 2017 SP0
