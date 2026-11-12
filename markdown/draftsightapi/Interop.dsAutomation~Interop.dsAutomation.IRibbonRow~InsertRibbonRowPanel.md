---
title: "InsertRibbonRowPanel Method (IRibbonRow)"
project: ""
interface: "IRibbonRow"
member: "InsertRibbonRowPanel"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonRow~InsertRibbonRowPanel.html"
---

# InsertRibbonRowPanel Method (IRibbonRow)

Inserts the specified ribbon row panel into this ribbon row.

## Syntax

### Visual Basic

```vb
Function InsertRibbonRowPanel( _
   ByVal ApiUuid As System.String, _
   ByVal PanelName As System.String _
) As RibbonRowPanel
```

### C#

```csharp
RibbonRowPanel InsertRibbonRowPanel(
   System.string ApiUuid,
   System.string PanelName
)
```

### JScript

```
function InsertRibbonRowPanel(
   ApiUuid : System.String,
   PanelName : System.String
) : RibbonRowPanel;
```

### Managed Extensions for C++

```
RibbonRowPanel* InsertRibbonRowPanel(
   System.string* ApiUuid,
   System.string* PanelName
)
```

### C++/CLI

```cpp
RibbonRowPanel^ InsertRibbonRowPanel(
   System.String^ ApiUuid,
   System.String^ PanelName
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `PanelName`: Name of the ribbon row panel

### Return Value

[IRibbonRowPanel](Interop.dsAutomation~Interop.dsAutomation.IRibbonRowPanel.html)

## Examples

Only one ribbon row panel can be added to a ribbon row.

## See Also

[IRibbonRow Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html)
[IRibbonRow Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow_members.html)
[IRibbonRow::GetRibbonRowItems Method ()](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow~GetRibbonRowItems.html)
[IRibbonRow::GetRibbonRowPanel Method ()](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow~GetRibbonRowPanel.html)

## Availability

DraftSight 2017 SP0
