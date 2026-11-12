---
title: "ICommand Interface"
project: ""
interface: "ICommand"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommand.html"
---

# ICommand Interface

Allows access to a command for the command window.

## Syntax

### Visual Basic

```vb
Public Interface ICommand
```

### C#

```csharp
public interface ICommand
```

### JScript

```
public interface ICommand
```

### Managed Extensions for C++

```
public __gc __interface ICommand
```

### C++/CLI

```cpp
public interface class ICommand
```

## Examples

The following code snippets show how to add a command to the list of commands for the command window:

- COM native C++ (from the DraftSight API [COM native C++ template files](GettingStarted-draftsightapi.html) **DsAddinCommand.h**, **DsAddinCommand.cpp**, and **DsAddinUserCommand.cpp**).
- [C++](#CPP) ( from the DraftSight API [C++ template file](GettingStarted-draftsightapi.html) **dsAddinUserConnection.cpp**).

##### COM Native C++

**DsAddinCommand.h**

public:

CComQIPtr<ICommand> m_DsCommand;

**DsAddinCommand.cpp**

// DsAddinCommand constructor
DsAddinCommand::DsAddinCommand( ICommand* dsCommand ): m_DsCommand( dsCommand )
{
IUnknown* dsUnk = NULL ;
HRESULT hr = m_DsCommand->QueryInterface(IID_IUnknown, (void **) &dsUnk);
hr = DispEventAdvise(dsUnk);
}

**DsAddinUserCommand.cpp**

DsAddinUserCommand::DsAddinUserCommand( _bstr_t ApiUuid, _bstr_t UserCmdName, _bstr_t CmdString, _bstr_t Description, _bstr_t SmallIcon, _bstr_t LargeIcon )

{

{

CDsAddinConnection *dsConnection = getMyApp();

dsCreateCommandError_e commandErr;

// User command dependent on pre-defined command

ICommand* pCommand = dsConnection->m_DsApp->CreateCommand( ApiUuid, UserCmdName, &commandErr );

m_DsUserCommand = dsConnection->m_DsApp->CreateUserCommand( ApiUuid, UserCmdName, CmdString, Description, SmallIcon, LargeIcon, &commandErr );

DsAddinCommand *dsAddCom = new DsAddinCommand(pCommand);

}

##### C++

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

[IApplication::CreateCommand2](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand2.html)

## Access Diagram

DSObjectModel.pdf#Command

[Command](DSObjectModel.pdf#Command)

## See Also

[ICommand Members](Interop.dsAutomation~Interop.dsAutomation.ICommand_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IApplication::RemoveCommand Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~RemoveCommand.html)
[IUserCommand Interface](Interop.dsAutomation~Interop.dsAutomation.IUserCommand.html)
[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommand Event ExecuteNotify](Interop.dsAutomation~Interop.dsAutomation._ICommandEvents_ExecuteNotifyEventHandler.html)
