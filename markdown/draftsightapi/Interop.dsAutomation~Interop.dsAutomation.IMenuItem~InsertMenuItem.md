---
title: "InsertMenuItem Method (IMenuItem)"
project: ""
interface: "IMenuItem"
member: "InsertMenuItem"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMenuItem~InsertMenuItem.html"
---

# InsertMenuItem Method (IMenuItem)

Inserts a menu item.

## Syntax

### Visual Basic

```vb
Function InsertMenuItem( _
   ByVal ApiUuid As System.String, _
   ByVal ItemType As dsMenuItemType_e, _
   ByVal Position As System.Integer, _
   ByVal ItemName As System.String, _
   ByVal UserCmdID As System.String _
) As MenuItem
```

### C#

```csharp
MenuItem InsertMenuItem(
   System.string ApiUuid,
   dsMenuItemType_e ItemType,
   System.int Position,
   System.string ItemName,
   System.string UserCmdID
)
```

### JScript

```
function InsertMenuItem(
   ApiUuid : System.String,
   ItemType : dsMenuItemType_e,
   Position : System.int,
   ItemName : System.String,
   UserCmdID : System.String
) : MenuItem;
```

### Managed Extensions for C++

```
MenuItem* InsertMenuItem(
   System.string* ApiUuid,
   dsMenuItemType_e ItemType,
   System.int Position,
   System.string* ItemName,
   System.string* UserCmdID
)
```

### C++/CLI

```cpp
MenuItem^ InsertMenuItem(
   System.String^ ApiUuid,
   dsMenuItemType_e ItemType,
   System.int Position,
   System.String^ ItemName,
   System.String^ UserCmdID
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or non add-in application
- `ItemType`: Type of menu item to insert as defined in [dsMenuItemType_e](Interop.dsAutomation~Interop.dsAutomation.dsMenuItemType_e.html)
- `Position`: 1-based index indicating where to insert the menu item
- `ItemName`: Name of menu item
- `UserCmdID`: User-defined command ID when ItemType is dsMenuItemType_e.dsMenuItemType_UserCommand

### Return Value

[Menu item](Interop.dsAutomation~Interop.dsAutomation.IMenuItem.html)

## Examples

The following code snippets show how to add a menu item to a menu:

- COM native C++ (from the DraftSight API [COM native C++ template files](GettingStarted-draftsightapi.html) **DsAddinConnection.cpp** and **DsAddinUserCommand.cpp**)
- [C++](#CPP) (from the DraftSight API [C++ template file](GettingStarted-draftsightapi.html) **dsAddinConnection.cpp**)

##### COM native C++

**DsAddinConnection.cpp**

sAddinUserCommand pNotepad(m_sApiUuid, L"Notepad", L"^C^CNotepad", L"Opens Notepad", L"`path_and_file_name`.bmp", L"`path_and_file_name`.png");

IMenuItemPtr pMenu = m_DsApp->AddMenu( m_sApiUuid, dsUIState_Document, MENU_POSITION, L"DsAddin" );

pMenu->InsertMenuItem(m_sApiUuid, dsMenuItemType_UserCommand, 1, L"Open Notepad", pNotepad.GetUserCommandID());

**DsAddinUserCommand.cpp**

bstr_t DsAddinUserCommand::GetUserCommandID()
{
return m_DsUserCommand->GetID();
}

##### C++

dsUserCommand_ptr pUserCmd;

dsApp->CreateUserCommand( myApplication::appID, UserCommandName, UserCmdString, Description, L

"`path_and_file_name`.bmp", L"`path_and_file_name`.png"

, dsUIState_Document, &Error, &pUserCmd );

dsMenuItem_ptr pMenu;

dsApp->AddMenu(myApplication::appID, dsUIState_Document, MENU_POSITION, UserCommandName, &pMenu);

dsString UserCmdID1;

pUserCmd->GetID( &UserCmdID1 );

dsMenuItem_ptr pMenuItem;

pMenu->InsertMenuItem(myApplication::appID, dsMenuItemType_UserCommand, 1, L

"Open Notepad"

, UserCmdID1, &pMenu);

if

( ( dsCreateCommand_Succeeded == Error ) && ( NULL != pUserCmd ) )

{

dsString ToolbarName = L

"QAddIn1_Toolbar"

;

dsToolbar_ptr pToolbar;

dsApp->AddToolbar( myApplication::appID, dsUIState_Document, ToolbarName, &pToolbar );

if( NULL != pToolbar )

{

dsToolbarItem_ptr pToolbarItem;

dsString ButtonName = L

"Notepad"

;

dsString UserCmdID;

pMenu->GetID( &UserCmdID );

pToolbar->InsertToolbarItem( myApplication::appID, dsToolBarItemType_UserCommand, 1, ButtonName, UserCmdID, &pToolbarItem );

}

}

[Back to top](#exampleBookmark)

## See Also

[IMenuItem Interface](Interop.dsAutomation~Interop.dsAutomation.IMenuItem.html)
[IMenuItem Members](Interop.dsAutomation~Interop.dsAutomation.IMenuItem_members.html)

## Availability

DraftSight V1R1
