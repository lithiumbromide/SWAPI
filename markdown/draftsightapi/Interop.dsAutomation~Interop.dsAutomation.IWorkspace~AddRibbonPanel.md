---
title: "AddRibbonPanel Method (IWorkspace)"
project: ""
interface: "IWorkspace"
member: "AddRibbonPanel"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IWorkspace~AddRibbonPanel.html"
---

# AddRibbonPanel Method (IWorkspace)

Adds the specified ribbon panel to this workspace.

## Syntax

### Visual Basic

```vb
Function AddRibbonPanel( _
   ByVal ApiUuid As System.String, _
   ByVal Position As System.Integer, _
   ByVal PanelName As System.String, _
   ByVal DisplayText As System.String, _
   ByVal RibbonTabArray As System.Object _
) As RibbonPanel
```

### C#

```csharp
RibbonPanel AddRibbonPanel(
   System.string ApiUuid,
   System.int Position,
   System.string PanelName,
   System.string DisplayText,
   System.object RibbonTabArray
)
```

### JScript

```
function AddRibbonPanel(
   ApiUuid : System.String,
   Position : System.int,
   PanelName : System.String,
   DisplayText : System.String,
   RibbonTabArray : System.Object
) : RibbonPanel;
```

### Managed Extensions for C++

```
RibbonPanel* AddRibbonPanel(
   System.string* ApiUuid,
   System.int Position,
   System.string* PanelName,
   System.string* DisplayText,
   System.Object* RibbonTabArray
)
```

### C++/CLI

```cpp
RibbonPanel^ AddRibbonPanel(
   System.String^ ApiUuid,
   System.int Position,
   System.String^ PanelName,
   System.String^ DisplayText,
   System.Object^ RibbonTabArray
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `Position`: Position of the ribbon panel (1-based index)
- `PanelName`: Name of the ribbon panel
- `DisplayText`: Text that is shown for the ribbon panel
- `RibbonTabArray`: Array of ribbon tabs using this ribbon panel

### Return Value

[IRibbonPanel](Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel.html)

## See Also

[IWorkspace Interface](Interop.dsAutomation~Interop.dsAutomation.IWorkspace.html)
[IWorkspace Members](Interop.dsAutomation~Interop.dsAutomation.IWorkspace_members.html)
[IWorkspace::GetRibbonPanels Method ()](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~GetRibbonPanels.html)

## Availability

DraftSight 2017 SP0
