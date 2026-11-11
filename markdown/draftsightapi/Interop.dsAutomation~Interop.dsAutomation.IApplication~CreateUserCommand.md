---
title: "CreateUserCommand Method (IApplication)"
project: ""
interface: "IApplication"
member: "CreateUserCommand"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateUserCommand.html"
---

# CreateUserCommand Method (IApplication)

Creates a command for a menu item and toolbar.

## Syntax

### Visual Basic

```vb
Function CreateUserCommand( _
   ByVal ApiUuid As System.String, _
   ByVal UserCmdName As System.String, _
   ByVal CmdString As System.String, _
   ByVal Description As System.String, _
   ByVal SmallIcon As System.String, _
   ByVal LargeIcon As System.String, _
   ByVal UIState As dsUIState_e, _
   ByRef Error As dsCreateCommandError_e _
) As UserCommand
```

### C#

```csharp
UserCommand CreateUserCommand(
   System.string ApiUuid,
   System.string UserCmdName,
   System.string CmdString,
   System.string Description,
   System.string SmallIcon,
   System.string LargeIcon,
   dsUIState_e UIState,
   out dsCreateCommandError_e Error
)
```

### JScript

```
function CreateUserCommand(
   ApiUuid : System.String,
   UserCmdName : System.String,
   CmdString : System.String,
   Description : System.String,
   SmallIcon : System.String,
   LargeIcon : System.String,
   UIState : dsUIState_e,
   Error : dsCreateCommandError_e
) : UserCommand;
```

### Managed Extensions for C++

```
UserCommand* CreateUserCommand(
   System.string* ApiUuid,
   System.string* UserCmdName,
   System.string* CmdString,
   System.string* Description,
   System.string* SmallIcon,
   System.string* LargeIcon,
   dsUIState_e UIState,
   [PARAMFLAG::Out] dsCreateCommandError_e Error
)
```

### C++/CLI

```cpp
UserCommand^ CreateUserCommand(
   System.String^ ApiUuid,
   System.String^ UserCmdName,
   System.String^ CmdString,
   System.String^ Description,
   System.String^ SmallIcon,
   System.String^ LargeIcon,
   dsUIState_e UIState,
   [Out] dsCreateCommandError_e Error
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or non add-in application
- `UserCmdName`: Command name for the menu item or the toolbar button's ToolTip (see **Remarks**)
- `CmdString`: Command string (see **Remarks**)
- `Description`: Description of the command
- `SmallIcon`: Path image's file name for the command's small icon (see **Remarks**)
- `LargeIcon`: Path and image's file name for the command's large icon (see **Remarks**)
- `UIState`: Where to add the user command as defined in [dsUIState_e](Interop.dsAutomation~Interop.dsAutomation.dsUIState_e.html)
- `Error`: Status of creating the command as defined in [dsCreateCommandError_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateCommandError_e.html)

### Return Value

[User command](Interop.dsAutomation~Interop.dsAutomation.IUserCommand.html)

## Examples

The following code snippets show how to create a command for a menu item and toolbar:

- COM native C++ (from the DraftSight API [COM native C++ template files](GettingStarted-draftsightapi.html) **DsAddinConnection.cpp** and **DsAddinUserCommand.cpp**)
- [C++](#CPP) (from the DraftSight API [C++ template file](GettingStarted-draftsightapi.html) **dsAddinConnection.cpp**)

##### COM native C++

**DsAddinConnection.cpp**

DsAddinUserCommand pNotepad(m_sApiUuid, L"Notepad", L"^C^CNotepad", L"Opens Notepad", L"`path_and_file_name`.bmp", L"`path_and_file_name`.png");

**DsAddinUserCommand.cpp**

DsAddinUserCommand::DsAddinUserCommand( _bstr_t ApiUuid, _bstr_t UserCmdName, _bstr_t CmdString, _bstr_t Description, _bstr_t SmallIcon, _bstr_t LargeIcon )

{

CDsAddinConnection *dsConnection = getMyApp();

dsCreateCommandError_e commandErr;

// User command dependent on pre-defined command

ICommand* pCommand = dsConnection->m_DsApp->CreateCommand( ApiUuid, UserCmdName, &commandErr );

m_DsUserCommand = dsConnection->m_DsApp->CreateUserCommand( ApiUuid, UserCmdName, CmdString, Description, SmallIcon, LargeIcon, &commandErr );

DsAddinCommand *dsAddCom = new DsAddinCommand(pCommand);

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

// User command dependent on pre-defined command

dsApp->CreateCommand(myApplication::appID, UserCommandName, &Error, &pCmd );

if

(( Error == 0 ) )

{

RegisterCommandExecuteNotifyHook( pCmd );

dsUserCommand_ptr pUserCmd;

dsApp->CreateUserCommand( myApplication::appID, UserCommandName, UserCmdString, Description, L

"`path_and_file_name`.bmp", L"`path_and_file_name`.png", dsUIState_Document, &Error, &pUserCmd );

[Back to top](#exampleBookmark)

## Examples

[Create Context-sensitive Menu Items (C#)](Create_Context-sensitive_Menu_Items_Example_CSharp.htm)
[Create Context-sensitive Menu Items (VB.NET)](Create_Context-sensitive_Menu_Items_Example_VBNET.htm)
[Create Context-sensitive Menu Items (VBA)](Create_Context-sensitive_Menu_Items_Example_VBA.htm)

## Remarks

If UserCmdName already exists, then dsCreateCommand_e.dsCreateCommandError_CommandNameExisted is returned for Error.

Specify the same string for UserCmdName as specified for [IApplication::CreateCommand's](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand.html) CmdName parameter; e.g.; `apiCmd`.

The string to specify for CmdString is the same string specified for UserCmdName prefaced by ^C^C; e.g., ^C^C`apiCmd`.

To see a list of existing commands:

1. Right-click a toolbar in the user interface.
2. Select **Customize Interface**.
3. Click **Commands** on the left side of the dialog.
4. Use the scroll bar to see the list of existing commands.
5. To quickly locate a command that you've added:

  1. Type the name of the command in **Find**.
  2. Click the name of the command in the Name column.
  3. Examine the information at the bottom of the dialog.

The recommended size for:

- SmallIcon is 16 x 16
- LargeIcon is 24 x 24.

The supported format for both images is **.png** (Portable Network Graphics bitmap image).

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::AbortRunningCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~AbortRunningCommand.html)
[IApplication::GetRunningCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRunningCommand.html)
[IApplication::RunCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~RunCommand.html)
[IApplication::RunScript Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~RunScript.html)
[IMenuItem::InsertMenuItem Method](Interop.dsAutomation~Interop.dsAutomation.IMenuItem~InsertMenuItem.html)
[IToolbar::InsertToolbarItem Method](Interop.dsAutomation~Interop.dsAutomation.IToolbar~InsertToolbarItem.html)
[IInterfaceFiles::CustomIconPath Property ()](Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles~CustomIconPath.html)

## Availability

DraftSight V1R1
