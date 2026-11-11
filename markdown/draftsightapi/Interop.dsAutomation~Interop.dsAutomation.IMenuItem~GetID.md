---
title: "GetID Method (IMenuItem)"
project: ""
interface: "IMenuItem"
member: "GetID"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMenuItem~GetID.html"
---

# GetID Method (IMenuItem)

Gets the ID of this menu item.

## Syntax

### Visual Basic

```vb
Function GetID() As System.String
```

### C#

```csharp
System.string GetID()
```

### JScript

```
function GetID() : System.String;
```

### Managed Extensions for C++

```
System.string* GetID();
```

### C++/CLI

```cpp
System.String^ GetID();
```

### Return Value

ID of this menu item

## Examples

This code snippet shows how to add user commands, a menu, menu item, toolbar, and toolbar button to the DraftSight user interface (from the DraftSight API [C++ template file](GettingStarted-draftsightapi.html) **dsAddinConnection.cpp**).

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

## Remarks

The return value is the string specified for [IMenuItem::InsertMenuItem's](Interop.dsAutomation~Interop.dsAutomation.IMenuItem~InsertMenuItem.html) UserCmdID parameter.

## See Also

[IMenuItem Interface](Interop.dsAutomation~Interop.dsAutomation.IMenuItem.html)
[IMenuItem Members](Interop.dsAutomation~Interop.dsAutomation.IMenuItem_members.html)
[IMenuItem::SetID Method ()](Interop.dsAutomation~Interop.dsAutomation.IMenuItem~SetID.html)

## Availability

DraftSight V1R1
