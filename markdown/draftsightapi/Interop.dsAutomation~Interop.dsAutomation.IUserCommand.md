---
title: "IUserCommand Interface"
project: ""
interface: "IUserCommand"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IUserCommand.html"
---

# IUserCommand Interface

Allows access to a command created for a [menu item](Interop.dsAutomation~Interop.dsAutomation.IMenuItem.html) or [toolbar item](Interop.dsAutomation~Interop.dsAutomation.IToolbarItem.html).

## Syntax

### Visual Basic

```vb
Public Interface IUserCommand
```

### C#

```csharp
public interface IUserCommand
```

### JScript

```
public interface IUserCommand
```

### Managed Extensions for C++

```
public __gc __interface IUserCommand
```

### C++/CLI

```cpp
public interface class IUserCommand
```

## Examples

The following code snippets show how to add a command to list of available commands:

- COM native C++ (from the DraftSight API [COM native C++ template files](GettingStarted-draftsightapi.html) **DsAddinUserCommand.h**, **DsAddinConnection.cpp**, and **DsAddinUserCommand.cpp**)
- [C++](#CPP) (from the DraftSight API [C++ template file](GettingStarted-draftsightapi.html) **dsAddinConnection.cpp**)

##### COM native C++

**DsAddinUserCommand.h**

private:
CComQIPtr<IUserCommand> m_DsUserCommand;

**DsAddinConnection.cpp**

DsAddinUserCommand pNotepad(m_sApiUuid, L"Notepad", L"^C^CNotepad", L"Opens Notepad", L"`path_and_file_name`.bmp", L"`path_and_file_name`.png");

**DsAddinUserCommand.cpp**

// DsAddinUserCommand constructor
DsAddinUserCommand::DsAddinUserCommand( _bstr_t ApiUuid, _bstr_t UserCmdName, _bstr_t CmdString, _bstr_t Description, _bstr_t SmallIcon, _bstr_t LargeIcon )

{

CDsAddinConnection *dsConnection = getMyApp();

dsCreateCommandError_e commandErr;

// User command dependent on pre-defined command

ICommand* pCommand = dsConnection->m_DsApp->CreateCommand( ApiUuid, UserCmdName, &commandErr );

m_DsUserCommand = dsConnection->m_DsApp->**C**reateUserCommand( ApiUuid, UserCmdName, CmdString, Description, SmallIcon, LargeIcon, &commandErr );

}

##### C++

bool myApplication::CreateUserInterfaceAndCommands()

{

dsString emptyStr = L"";

dsString UserCommandName = L"qAddin1_Notepad";

dsString Description = L"Opens Notepad";

dsString UserCmdString = L"^C^CqAddin1_Notepad";

const int MENU_POSITION = 9; //Menu should be between "Modify" and "Tools" menus

dsApplication_c *dsApp = getDsApp();

dsCreateCommandError_e Error;

// User command dependent on pre-defined command

dsApp->CreateCommand(myApplication::appID, UserCommandName, &Error, &pCmd );

if(( Error == 0 ) )

{

RegisterCommandExecuteNotifyHook( pCmd );

dsUserCommand_ptr pUserCmd;

dsApp->CreateUserCommand( myApplication::appID, UserCommandName, UserCmdString, Description, L"`path_and_file_name`.bmp", L"`path_and_file_name`.png", dsUIState_Document, &Error, &pUserCmd );

[Back to top](#exampleBookmark)

## Examples

[Create Context-sensitive Menu Items (C#)](Create_Context-sensitive_Menu_Items_Example_CSharp.htm)
[Create Context-sensitive Menu Items (VB.NET)](Create_Context-sensitive_Menu_Items_Example_VBNET.htm)
[Create Context-sensitive Menu Items (VBA)](Create_Context-sensitive_Menu_Items_Example_VBA.htm)

## Remarks

To see a list of existing commands:

1. Right-click a toolbar in the user interface.
2. Select **Customize Interface**.
3. Click **Commands** on the left side of the dialog.
4. Use the scroll bar to see the list of existing commands.
5. To quickly locate a command that you've added:

  1. Type the name of the command in **Find.**
  2. Click the name of the command in the Name column.
  3. Examine the information at the bottom of the dialog.

## Accessors

[IApplication::CreateUserCommand](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateUserCommand.html)

## Access Diagram

DSObjectModel.pdf#UserCommand

[UserCommand](DSObjectModel.pdf#UserCommand)

## See Also

[IUserCommand Members](Interop.dsAutomation~Interop.dsAutomation.IUserCommand_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ICommand Interface](Interop.dsAutomation~Interop.dsAutomation.ICommand.html)
