---
title: "IRibbonPanel Interface"
project: ""
interface: "IRibbonPanel"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel.html"
---

# IRibbonPanel Interface

Allows access to a ribbon panel.

## Syntax

### Visual Basic

```vb
Public Interface IRibbonPanel
```

### C#

```csharp
public interface IRibbonPanel
```

### JScript

```
public interface IRibbonPanel
```

### Managed Extensions for C++

```
public __gc __interface IRibbonPanel
```

### C++/CLI

```cpp
public interface class IRibbonPanel
```

## Examples

See the following ribbon-based add-in projects:

- `install_dir`**\APISDK\samples\C#\Simple\Ribbon**
- `install_dir`**\APISDK\samples\C++\Simple\Ribbon**
- `install_dir`**\APISDK\samples\COM\Simple\RibbonSample**
- `install_dir`**\APISDK\samples\JS\Simple\RibbonSample.html**

## Remarks

A [ribbon tab](Interop.dsAutomation~Interop.dsAutomation.IRibbonTab.html) can contain one or more ribbon panels. You must insert a ribbon panel into a ribbon tab before laying out other user interface components in the ribbon panel. Only one [ribbon row](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html) can be added to a ribbon panel.

## Accessors

[IRibbonTab::GetRibbonPanels](Interop.dsAutomation~Interop.dsAutomation.IRibbonTab~GetRibbonPanels.html)

[IRibbonTab::InsertRibbonPanel](Interop.dsAutomation~Interop.dsAutomation.IRibbonTab~InsertRibbonPanel.html)

[IWorkspace::AddRibbonPanel](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~AddRibbonPanel.html)

[IWorkspace::GetRibbonPanels](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~GetRibbonPanels.html)

## Access Diagram

DSObjectModel.pdf#RibbonPanel

[RibbonPanel](DSObjectModel.pdf#RibbonPanel)

## See Also

[IRibbonPanel Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
