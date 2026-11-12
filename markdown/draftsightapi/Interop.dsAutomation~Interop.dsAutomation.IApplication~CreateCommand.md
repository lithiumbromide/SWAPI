---
title: "CreateCommand Method (IApplication)"
project: ""
interface: "IApplication"
member: "CreateCommand"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand.html"
---

# CreateCommand Method (IApplication)

Obsolete. Superseded by [IApplication::CreateCommand2](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand2.html).

## Syntax

### Visual Basic

```vb
Function CreateCommand( _
   ByVal ApiUuid As System.String, _
   ByVal CmdName As System.String, _
   ByRef Error As dsCreateCommandError_e _
) As Command
```

### C#

```csharp
Command CreateCommand(
   System.string ApiUuid,
   System.string CmdName,
   out dsCreateCommandError_e Error
)
```

### JScript

```
function CreateCommand(
   ApiUuid : System.String,
   CmdName : System.String,
   Error : dsCreateCommandError_e
) : Command;
```

### Managed Extensions for C++

```
Command* CreateCommand(
   System.string* ApiUuid,
   System.string* CmdName,
   [PARAMFLAG::Out] dsCreateCommandError_e Error
)
```

### C++/CLI

```cpp
Command^ CreateCommand(
   System.String^ ApiUuid,
   System.String^ CmdName,
   [Out] dsCreateCommandError_e Error
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or non add-in application
- `CmdName`: Unique name for the command (see **Remarks**)
- `Error`: Status of creating the command as defined in [dsCreateCommandError_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateCommandError_e.html)

### Return Value

[Command](Interop.dsAutomation~Interop.dsAutomation.ICommand.html)

## Examples

The following code snippets show how to add a command for the command window:

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

## Remarks

If CmdName already exists, then dsCreateCommand_e.dsCreateCommandError_CommandNameExisted is returned for Error.

Use the string specified for CmdName for [IApplication::CreateUserCommand's](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateUserCommand.html) UserCmdName parameter; e.g.; **apiCmd**.

To see a list of existing commands:

1. Right-click a toolbar in the user interface.
2. Select **Customize Interface**.
3. Click **Commands** on the left side of the dialog.
4. Use the scroll bar to see the list of existing commands.
5. To quickly locate a command that you've added:

  1. Type the name of the command in **Find.**
  2. Click the name of the command in the Name column.
  3. Examine the information at the bottom of the dialog.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetRunningCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRunningCommand.html)
[IApplication::RunCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~RunCommand.html)
[IApplication::AbortRunningCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~AbortRunningCommand.html)

## Availability

DraftSight V1R1
