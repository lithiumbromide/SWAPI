---
title: "IRibbonRowItem Interface"
project: ""
interface: "IRibbonRowItem"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonRowItem.html"
---

# IRibbonRowItem Interface

Allows access to items in a ribbon row.

## Syntax

### Visual Basic

```vb
Public Interface IRibbonRowItem
```

### C#

```csharp
public interface IRibbonRowItem
```

### JScript

```
public interface IRibbonRowItem
```

### Managed Extensions for C++

```
public __gc __interface IRibbonRowItem
```

### C++/CLI

```cpp
public interface class IRibbonRowItem
```

## Examples

See the following ribbon-based add-in projects:

- `install_dir`**\APISDK\samples\C#\Simple\Ribbon**
- `install_dir`**\APISDK\samples\C++\Simple\Ribbon**
- `install_dir`**\APISDK\samples\COM\Simple\RibbonSample**
- `install_dir`**\APISDK\samples\JS\Simple\RibbonSample.html**

## Remarks

IRibbonRowItem is the base class for the following objects that can reside in a ribbon row:

- [IRibbonCommandButton](Interop.dsAutomation~Interop.dsAutomation.IRibbonCommandButton.html)
- [IRibbonRowPanel](Interop.dsAutomation~Interop.dsAutomation.IRibbonRowPanel.html)
- [IRibbonSeparator](Interop.dsAutomation~Interop.dsAutomation.IRibbonSeparator.html)
- [IRibbonSplitButton](Interop.dsAutomation~Interop.dsAutomation.IRibbonSplitButton.html)

This interface cannot be instantiated directly. After calling its accessor, this interface allows you to enable, name, or remove the different types of items in a ribbon row.

## Accessors

[IRibbonRow::GetRibbonRowItems](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow~GetRibbonRowItems.html)

## Access Diagram

DSObjectModel.pdf#RibbonRowItem

[RibbonRowItem](DSObjectModel.pdf#RibbonRowItem)

## See Also

[IRibbonRowItem Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonRowItem_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
