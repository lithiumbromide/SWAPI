---
title: "GetWorkspaces Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetWorkspaces"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetWorkspaces.html"
---

# GetWorkspaces Method (IApplication)

Gets all workspaces in the specified user-interface state.

## Syntax

### Visual Basic

```vb
Function GetWorkspaces( _
   ByVal UIState As dsUIState_e _
) As System.Object
```

### C#

```csharp
System.object GetWorkspaces(
   dsUIState_e UIState
)
```

### JScript

```
function GetWorkspaces(
   UIState : dsUIState_e
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetWorkspaces(
   dsUIState_e UIState
)
```

### C++/CLI

```cpp
System.Object^ GetWorkspaces(
   dsUIState_e UIState
)
```

### Parameters

- `UIState`: User-interface state as defined in [dsUIState_e](Interop.dsAutomation~Interop.dsAutomation.dsUIState_e.html)

### Return Value

Array of [IWorkspace](Interop.dsAutomation~Interop.dsAutomation.IWorkspace.html)s

## Examples

See the following ribbon-based add-in projects:

- `install_dir`**\APISDK\samples\C#\Simple\Ribbon**
- `install_dir`**\APISDK\samples\C++\Simple\Ribbon**
- `install_dir`**\APISDK\samples\COM\Simple\RibbonSample**
- `install_dir`**\APISDK\samples\JS\Simple\RibbonSample.html**

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::AddWorkspace Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddWorkspace.html)
[IApplication::GetActiveWorkspace Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetActiveWorkspace.html)
[IApplication::GetWorkspace Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetWorkspace.html)

## Availability

DraftSight 2017 SP0
