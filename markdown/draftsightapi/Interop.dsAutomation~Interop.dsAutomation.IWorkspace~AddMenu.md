---
title: "AddMenu Method (IWorkspace)"
project: ""
interface: "IWorkspace"
member: "AddMenu"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IWorkspace~AddMenu.html"
---

# AddMenu Method (IWorkspace)

Adds the specified menu item to this workspace.

## Syntax

### Visual Basic

```vb
Function AddMenu( _
   ByVal ApiUuid As System.String, _
   ByVal Position As System.Integer, _
   ByVal MenuName As System.String _
) As MenuItem
```

### C#

```csharp
MenuItem AddMenu(
   System.string ApiUuid,
   System.int Position,
   System.string MenuName
)
```

### JScript

```
function AddMenu(
   ApiUuid : System.String,
   Position : System.int,
   MenuName : System.String
) : MenuItem;
```

### Managed Extensions for C++

```
MenuItem* AddMenu(
   System.string* ApiUuid,
   System.int Position,
   System.string* MenuName
)
```

### C++/CLI

```cpp
MenuItem^ AddMenu(
   System.String^ ApiUuid,
   System.int Position,
   System.String^ MenuName
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `Position`: Position of the menu item (1-based index)
- `MenuName`: Name of the menu item

### Return Value

[IMenuItem](Interop.dsAutomation~Interop.dsAutomation.IMenuItem.html)

## See Also

[IWorkspace Interface](Interop.dsAutomation~Interop.dsAutomation.IWorkspace.html)
[IWorkspace Members](Interop.dsAutomation~Interop.dsAutomation.IWorkspace_members.html)
[IWorkspace::GetMenuItems Method ()](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~GetMenuItems.html)

## Availability

DraftSight 2017 SP0
