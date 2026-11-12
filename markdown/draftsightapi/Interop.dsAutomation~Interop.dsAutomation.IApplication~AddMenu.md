---
title: "AddMenu Method (IApplication)"
project: ""
interface: "IApplication"
member: "AddMenu"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~AddMenu.html"
---

# AddMenu Method (IApplication)

Obsolete. Superseded by [IWorkspace::AddMenu](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~AddMenu.html).

## Syntax

### Visual Basic

```vb
Function AddMenu( _
   ByVal ApiUuid As System.String, _
   ByVal UIState As dsUIState_e, _
   ByVal Position As System.Integer, _
   ByVal MenuName As System.String _
) As MenuItem
```

### C#

```csharp
MenuItem AddMenu(
   System.string ApiUuid,
   dsUIState_e UIState,
   System.int Position,
   System.string MenuName
)
```

### JScript

```
function AddMenu(
   ApiUuid : System.String,
   UIState : dsUIState_e,
   Position : System.int,
   MenuName : System.String
) : MenuItem;
```

### Managed Extensions for C++

```
MenuItem* AddMenu(
   System.string* ApiUuid,
   dsUIState_e UIState,
   System.int Position,
   System.string* MenuName
)
```

### C++/CLI

```cpp
MenuItem^ AddMenu(
   System.String^ ApiUuid,
   dsUIState_e UIState,
   System.int Position,
   System.String^ MenuName
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `UIState`: Where to add the menu item as defined in [dsUIState_e](Interop.dsAutomation~Interop.dsAutomation.dsUIState_e.html)
- `Position`: Position of the menu item
- `MenuName`: Name of the menu item

### Return Value

[Menu item](Interop.dsAutomation~Interop.dsAutomation.IMenuItem.html)

## Examples

The following code snippets show how to add a menu item to DraftSight's Classic Default workspace menu:

- COM native C++ (from the DraftSight API [COM native C++ template file](GettingStarted-draftsightapi.html) **DsAddinConnection.cpp**)
- C++ (from the DraftSight API [C++ template file](GettingStarted-draftsightapi.html) **dsAddinConnection.cpp**)

##### COM native C++

IMenuItemPtr pMenu = m_DsApp->AddMenu( m_sApiUuid, dsUIState_Document, MENU_POSITION, L"DsAddin" );

##### C++

dsMenuItem_ptr pMenu;

dsApp->AddMenu(myApplication::appID, dsUIState_Document, MENU_POSITION, UserCommandName, &pMenu);

## Remarks

This method is valid only for the Classic Default workspace menu as of DraftSight 2017 SP0.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetMenuItems Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetMenuItems.html)

## Availability

DraftSight V1R1
