---
title: "InsertRibbonPanel Method (IRibbonTab)"
project: ""
interface: "IRibbonTab"
member: "InsertRibbonPanel"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonTab~InsertRibbonPanel.html"
---

# InsertRibbonPanel Method (IRibbonTab)

Inserts the specified ribbon panel into this ribbon tab.

## Syntax

### Visual Basic

```vb
Function InsertRibbonPanel( _
   ByVal ApiUuid As System.String, _
   ByVal Position As System.Integer, _
   ByVal PanelName As System.String, _
   ByVal DisplayText As System.String _
) As RibbonPanel
```

### C#

```csharp
RibbonPanel InsertRibbonPanel(
   System.string ApiUuid,
   System.int Position,
   System.string PanelName,
   System.string DisplayText
)
```

### JScript

```
function InsertRibbonPanel(
   ApiUuid : System.String,
   Position : System.int,
   PanelName : System.String,
   DisplayText : System.String
) : RibbonPanel;
```

### Managed Extensions for C++

```
RibbonPanel* InsertRibbonPanel(
   System.string* ApiUuid,
   System.int Position,
   System.string* PanelName,
   System.string* DisplayText
)
```

### C++/CLI

```cpp
RibbonPanel^ InsertRibbonPanel(
   System.String^ ApiUuid,
   System.int Position,
   System.String^ PanelName,
   System.String^ DisplayText
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `Position`: Position of the ribbon panel (1-based index)
- `PanelName`: Name of the ribbon panel
- `DisplayText`: Text that is shown for the ribbon panel

### Return Value

[IRibbonPanel](Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel.html)

## Examples

See the [IRibbonTab](Interop.dsAutomation~Interop.dsAutomation.IRibbonTab.html) example.

## See Also

[IRibbonTab Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonTab.html)
[IRibbonTab Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonTab_members.html)

## Availability

DraftSight 2017 SP0
