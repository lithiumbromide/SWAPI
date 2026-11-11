---
title: "AddRibbonTab Method (IWorkspace)"
project: ""
interface: "IWorkspace"
member: "AddRibbonTab"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IWorkspace~AddRibbonTab.html"
---

# AddRibbonTab Method (IWorkspace)

Adds the specified ribbon tab to this workspace.

## Syntax

### Visual Basic

```vb
Function AddRibbonTab( _
   ByVal ApiUuid As System.String, _
   ByVal Position As System.Integer, _
   ByVal TabName As System.String, _
   ByVal DisplayText As System.String _
) As RibbonTab
```

### C#

```csharp
RibbonTab AddRibbonTab(
   System.string ApiUuid,
   System.int Position,
   System.string TabName,
   System.string DisplayText
)
```

### JScript

```
function AddRibbonTab(
   ApiUuid : System.String,
   Position : System.int,
   TabName : System.String,
   DisplayText : System.String
) : RibbonTab;
```

### Managed Extensions for C++

```
RibbonTab* AddRibbonTab(
   System.string* ApiUuid,
   System.int Position,
   System.string* TabName,
   System.string* DisplayText
)
```

### C++/CLI

```cpp
RibbonTab^ AddRibbonTab(
   System.String^ ApiUuid,
   System.int Position,
   System.String^ TabName,
   System.String^ DisplayText
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `Position`: Position of the ribbon tab (1-based index)
- `TabName`: Name of the ribbon tab
- `DisplayText`: Text that is shown for the ribbon tab

### Return Value

[IRibbonTab](Interop.dsAutomation~Interop.dsAutomation.IRibbonTab.html)

## Examples

See the [IWorkspace](Interop.dsAutomation~Interop.dsAutomation.IWorkspace.html) example.

## See Also

[IWorkspace Interface](Interop.dsAutomation~Interop.dsAutomation.IWorkspace.html)
[IWorkspace Members](Interop.dsAutomation~Interop.dsAutomation.IWorkspace_members.html)
[IWorkspace::GetRibbonTabs Method ()](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~GetRibbonTabs.html)

## Availability

DraftSight 2017 SP0
