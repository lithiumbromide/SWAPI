---
title: "GetToolbars Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetToolbars"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetToolbars.html"
---

# GetToolbars Method (IApplication)

Obsolete. Superseded by [IWorkspace::GetToolbars](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~GetToolbars.html).

## Syntax

### Visual Basic

```vb
Function GetToolbars( _
   ByVal UIState As dsUIState_e _
) As System.Object
```

### C#

```csharp
System.object GetToolbars(
   dsUIState_e UIState
)
```

### JScript

```
function GetToolbars(
   UIState : dsUIState_e
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetToolbars(
   dsUIState_e UIState
)
```

### C++/CLI

```cpp
System.Object^ GetToolbars(
   dsUIState_e UIState
)
```

### Parameters

- `UIState`: Where to get the toolbars as defined in [dsUIState_e](Interop.dsAutomation~Interop.dsAutomation.dsUIState_e.html)

### Return Value

Array of [toolbars](Interop.dsAutomation~Interop.dsAutomation.IToolbar.html)

## Remarks

This method is valid only for the Classic Default workspace as of DraftSight 2017 SP0.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::AddToolbar Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddToolbar.html)

## Availability

DraftSight V1R1
