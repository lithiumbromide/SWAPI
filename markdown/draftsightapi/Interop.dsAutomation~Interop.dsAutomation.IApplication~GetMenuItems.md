---
title: "GetMenuItems Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetMenuItems"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetMenuItems.html"
---

# GetMenuItems Method (IApplication)

Obsolete. Superseded by [IWorkspace::GetMenuItems](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~GetMenuItems.html).

## Syntax

### Visual Basic

```vb
Function GetMenuItems( _
   ByVal UIState As dsUIState_e _
) As System.Object
```

### C#

```csharp
System.object GetMenuItems(
   dsUIState_e UIState
)
```

### JScript

```
function GetMenuItems(
   UIState : dsUIState_e
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetMenuItems(
   dsUIState_e UIState
)
```

### C++/CLI

```cpp
System.Object^ GetMenuItems(
   dsUIState_e UIState
)
```

### Parameters

- `UIState`: Where to get the menu items as defined in [dsUIState_e](Interop.dsAutomation~Interop.dsAutomation.dsUIState_e.html)

### Return Value

Array of [menu items](Interop.dsAutomation~Interop.dsAutomation.IMenuItem.html)

## Remarks

This method is valid only for the Classic Default workspace menu as of DraftSight 2017 SP0.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::AddMenu Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddMenu.html)

## Availability

DraftSight V1R1
