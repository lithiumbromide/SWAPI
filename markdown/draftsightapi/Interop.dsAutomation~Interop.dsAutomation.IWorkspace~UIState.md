---
title: "UIState Property (IWorkspace)"
project: ""
interface: "IWorkspace"
member: "UIState"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IWorkspace~UIState.html"
---

# UIState Property (IWorkspace)

Gets the user-interface location of this workspace.

## Syntax

### Visual Basic

```vb
ReadOnly Property UIState As dsUIState_e
```

### C#

```csharp
dsUIState_e UIState {get;}
```

### JScript

```
function get UIState : dsUIState_e
```

### Managed Extensions for C++

```
__property dsUIState_e get_UIState();
```

### C++/CLI

```cpp
property dsUIState_e UIState {
   dsUIState_e get();
}
```

### Property Value

User interface location as defined in [dsUIState_e](Interop.dsAutomation~Interop.dsAutomation.dsUIState_e.html)

## Remarks

By default, the user-interface location of new workspaces is dsUIState_e.dsUIState_Document.

## See Also

[IWorkspace Interface](Interop.dsAutomation~Interop.dsAutomation.IWorkspace.html)
[IWorkspace Members](Interop.dsAutomation~Interop.dsAutomation.IWorkspace_members.html)

## Availability

DraftSight 2017 SP0
