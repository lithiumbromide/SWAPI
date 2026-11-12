---
title: "IRibbonSystemMenuItem Interface"
project: ""
interface: "IRibbonSystemMenuItem"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenuItem.html"
---

# IRibbonSystemMenuItem Interface

Allows access to a ribbon system menu item.

## Syntax

### Visual Basic

```vb
Public Interface IRibbonSystemMenuItem
```

### C#

```csharp
public interface IRibbonSystemMenuItem
```

### JScript

```
public interface IRibbonSystemMenuItem
```

### Managed Extensions for C++

```
public __gc __interface IRibbonSystemMenuItem
```

### C++/CLI

```cpp
public interface class IRibbonSystemMenuItem
```

## Examples

See the following ribbon-based add-in projects:

- `install_dir`**\APISDK\samples\C#\Simple\Ribbon**
- `install_dir`**\APISDK\samples\C++\Simple\Ribbon**
- `install_dir`**\APISDK\samples\COM\Simple\RibbonSample**
- `install_dir`**\APISDK\samples\JS\Simple\RibbonSample.html**

## Remarks

Ribbon system menu items can be nested only one level deep.

For example, this is permitted:

System main menu

|

--- Menu item #1

|

--- Menu item #1a

|

--- Menu item #2

|

--- Menu item #2a

This is not permitted:

System main menu

|

--- Menu item #1

|

--- Menu item #1a

|

--- Menu item #1a1

|

--- Menu item #2

## Accessors

[IRibbonSystemMenu::GetRibbonSystemMenuItems](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenu~GetRibbonSystemMenuItems.html)

[IRibbonSystemMenu::InsertRibbonSystemMenuItem](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenu~InsertRibbonSystemMenuItem.html)

[IRibbonSystemMenuItem::GetRibbonSystemMenuItems](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenuItem~GetRibbonSystemMenuItems.html)

[IRibbonSystemMenuItem::InsertRibbonSystemMenuItem](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenuItem~InsertRibbonSystemMenuItem.html)

## Access Diagram

DSObjectModel.pdf#RibbonSystemMenuItem

[RibbonSystemMenuItem](DSObjectModel.pdf#RibbonSystemMenuItem)

## See Also

[IRibbonSystemMenuItem Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenuItem_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IMenuItem Interface](Interop.dsAutomation~Interop.dsAutomation.IMenuItem.html)
