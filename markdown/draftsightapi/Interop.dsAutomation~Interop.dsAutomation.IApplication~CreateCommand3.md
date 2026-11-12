---
title: "CreateCommand3 Method (IApplication)"
project: ""
interface: "IApplication"
member: "CreateCommand3"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand3.html"
---

# CreateCommand3 Method (IApplication)

Creates the specified command for the command window with support for the specified context-sensitive (F1) help.

## Syntax

### Visual Basic

```vb
Function CreateCommand3( _
   ByVal ApiUuid As System.String, _
   ByVal CmdName As System.String, _
   ByVal HelpID As System.Integer, _
   ByVal ProductID As System.Integer, _
   ByRef Error As dsCreateCommandError_e _
) As Command
```

### C#

```csharp
Command CreateCommand3(
   System.string ApiUuid,
   System.string CmdName,
   System.int HelpID,
   System.int ProductID,
   out dsCreateCommandError_e Error
)
```

### JScript

```
function CreateCommand3(
   ApiUuid : System.String,
   CmdName : System.String,
   HelpID : System.int,
   ProductID : System.int,
   Error : dsCreateCommandError_e
) : Command;
```

### Managed Extensions for C++

```
Command* CreateCommand3(
   System.string* ApiUuid,
   System.string* CmdName,
   System.int HelpID,
   System.int ProductID,
   [PARAMFLAG::Out] dsCreateCommandError_e Error
)
```

### C++/CLI

```cpp
Command^ CreateCommand3(
   System.String^ ApiUuid,
   System.String^ CmdName,
   System.int HelpID,
   System.int ProductID,
   [Out] dsCreateCommandError_e Error
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or non add-in application
- `CmdName`: Unique name for the command
- `HelpID`: ID of the context-sensitive help topic to open when F1 is pressed
- `ProductID`: Product ID of the system help
- `Error`: Status of creating the command as defined in [dsCreateCommandError_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateCommandError_e.html)

### Return Value

[Command](Interop.dsAutomation~Interop.dsAutomation.ICommand.html)

## Examples

See the [IApplication::CreateCommand](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand.html) example.

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
[IApplication::AbortRunningCommand Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AbortRunningCommand.html)
[IApplication::GetRunningCommand Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRunningCommand.html)
[IApplication::RunCommand Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~RunCommand.html)

## Availability

DraftSight 2019 SP0
