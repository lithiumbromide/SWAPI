---
title: "AddToolbar Method (IWorkspace)"
project: ""
interface: "IWorkspace"
member: "AddToolbar"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IWorkspace~AddToolbar.html"
---

# AddToolbar Method (IWorkspace)

Adds a toolbar to this workspace.

## Syntax

### Visual Basic

```vb
Function AddToolbar( _
   ByVal ApiUuid As System.String, _
   ByVal ToolBarName As System.String _
) As Toolbar
```

### C#

```csharp
Toolbar AddToolbar(
   System.string ApiUuid,
   System.string ToolBarName
)
```

### JScript

```
function AddToolbar(
   ApiUuid : System.String,
   ToolBarName : System.String
) : Toolbar;
```

### Managed Extensions for C++

```
Toolbar* AddToolbar(
   System.string* ApiUuid,
   System.string* ToolBarName
)
```

### C++/CLI

```cpp
Toolbar^ AddToolbar(
   System.String^ ApiUuid,
   System.String^ ToolBarName
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `ToolBarName`: Name of the toolbar

### Return Value

[IToolbar](Interop.dsAutomation~Interop.dsAutomation.IToolbar.html)

## See Also

[IWorkspace Interface](Interop.dsAutomation~Interop.dsAutomation.IWorkspace.html)
[IWorkspace Members](Interop.dsAutomation~Interop.dsAutomation.IWorkspace_members.html)
[IWorkspace::GetToolbars Method ()](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~GetToolbars.html)

## Availability

DraftSight 2017 SP0
