---
title: "InsertToolbarItem Method (IToolbar)"
project: ""
interface: "IToolbar"
member: "InsertToolbarItem"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IToolbar~InsertToolbarItem.html"
---

# InsertToolbarItem Method (IToolbar)

Inserts a toolbar item.

## Syntax

### Visual Basic

```vb
Function InsertToolbarItem( _
   ByVal ApiUuid As System.String, _
   ByVal ItemType As dsToolbarItemType_e, _
   ByVal Position As System.Integer, _
   ByVal ItemName As System.String, _
   ByVal UserCmdID As System.String _
) As ToolbarItem
```

### C#

```csharp
ToolbarItem InsertToolbarItem(
   System.string ApiUuid,
   dsToolbarItemType_e ItemType,
   System.int Position,
   System.string ItemName,
   System.string UserCmdID
)
```

### JScript

```
function InsertToolbarItem(
   ApiUuid : System.String,
   ItemType : dsToolbarItemType_e,
   Position : System.int,
   ItemName : System.String,
   UserCmdID : System.String
) : ToolbarItem;
```

### Managed Extensions for C++

```
ToolbarItem* InsertToolbarItem(
   System.string* ApiUuid,
   dsToolbarItemType_e ItemType,
   System.int Position,
   System.string* ItemName,
   System.string* UserCmdID
)
```

### C++/CLI

```cpp
ToolbarItem^ InsertToolbarItem(
   System.String^ ApiUuid,
   dsToolbarItemType_e ItemType,
   System.int Position,
   System.String^ ItemName,
   System.String^ UserCmdID
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or non add-in application
- `ItemType`: Type of toolbar item as defined in [dsToolbarItemType_e](Interop.dsAutomation~Interop.dsAutomation.dsToolbarItemType_e.html)
- `Position`: 1-based index indicating where to insert toolbar item in the toolbar
- `ItemName`: Name of toolbar item
- `UserCmdID`: User-defined command ID when ItemType is dsToolbarItemType_e.dsToolBarItemType_UserCommand

### Return Value

[Toolbar item](Interop.dsAutomation~Interop.dsAutomation.IToolbarItem.html)

## Examples

The following code snippets show how to add a toolbar button with a ToolTip to a toolbar:

- COM native C++ (from the DraftSight API [COM native C++ template files](GettingStarted-draftsightapi.html) DsAddinConnection.cpp and DsAddinUserCommand.cpp)
- [C++](#CPP) (COM native C++ (from the DraftSight API [C++ template file](GettingStarted-draftsightapi.html) dsAddinConnection.cpp)

##### COM native C++

**DsAddinConnection.cpp**

DsAddinUserCommand pNotepad(m_sApiUuid, L"Notepad", L"^C^CNotepad", L"Opens Notepad", L"`path_and_file_name`.bmp", L"`path_and_file_name`.png");

IToolbarPtr pToolbar = m_DsApp->AddToolbar( m_sApiUuid, dsUIState_Document, L"DsAddin Toolbar");

IToolbarItemPtr pToolbarItem;

pToolbarItem = pToolbar->InsertToolbarItem( m_sApiUuid, dsToolBarItemType_UserCommand, ++position, L"Open Notepad", pNotepad.GetUserCommandID());

**DsAddinUserCommand.cpp**

bstr_t DsAddinUserCommand::GetUserCommandID()
{
return m_DsUserCommand->GetID();
}

##### C++

bool

myApplication::CreateUserInterfaceAndCommands()

{

dsString emptyStr = L

""

;

dsString UserCommandName = L

"qAddin1_Notepad"

;

dsString Description = L

"Opens Notepad"

;

dsString UserCmdString = L

"^C^CqAddin1_Notepad";

const int MENU_POSITION = 9; //Menu should be between "Modify" and "Tools" menus

dsApplication_c *dsApp = getDsApp();

dsCreateCommandError_e Error;

dsApp->CreateCommand(myApplication::appID, UserCommandName, &Error, &pCmd );

if

(( Error == 0 ) )

{

RegisterCommandExecuteNotifyHook( pCmd );

dsUserCommand_ptr pUserCmd;

dsApp->CreateUserCommand( myApplication::appID, UserCommandName, UserCmdString, Description, L"`path_and_file_name`.bmp", L"`path_and_file_name`.png", dsUIState_Document, &Error, &pUserCmd );

dsMenuItem_ptr pMenu;

dsApp->AddMenu(myApplication::appID, dsUIState_Document, MENU_POSITION, UserCommandName, &pMenu);

dsString UserCmdID1;

pUserCmd->GetID( &UserCmdID1 );

dsMenuItem_ptr pMenuItem;

pMenu->InsertMenuItem(myApplication::appID, dsMenuItemType_UserCommand, 1, L"Open Notepad", UserCmdID1, &pMenu);

if( ( dsCreateCommand_Succeeded == Error ) && ( NULL != pUserCmd ) )

{

dsString ToolbarName = L"QAddIn1_Toolbar";

dsToolbar_ptr pToolbar;

dsApp->AddToolbar( myApplication::appID, dsUIState_Document, ToolbarName, &pToolbar );

if( NULL != pToolbar )

{

dsToolbarItem_ptr pToolbarItem;

dsString ButtonName = L"Notepad";

dsString UserCmdID;

pMenu->GetID( &UserCmdID );

pToolbar->InsertToolbarItem( myApplication::appID, dsToolBarItemType_UserCommand, 1, ButtonName, UserCmdID, &pToolbarItem );

}

}

}

[Back to top](#exampleBookmark)

## Remarks

To display the list of available toolbars, right-click a toolbar in the DraftSight user interface and select **Toolbars** to open the Specify Toolbars dialog.

## See Also

[IToolbar Interface](Interop.dsAutomation~Interop.dsAutomation.IToolbar.html)
[IToolbar Members](Interop.dsAutomation~Interop.dsAutomation.IToolbar_members.html)

## Availability

DraftSight V1R1
