---
title: "CreateCommand4 Method (IApplication)"
project: ""
interface: "IApplication"
member: "CreateCommand4"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand4.html"
---

# CreateCommand4 Method (IApplication)

Creates the specified command for the command window with support for the specified context-sensitive (F1) help.

## Syntax

### Visual Basic

```vb
Function CreateCommand4( _
   ByVal ApiUuid As System.String, _
   ByVal GlobalCmdName As System.String, _
   ByVal LocalCmdName As System.String, _
   ByVal HelpID As System.Integer, _
   ByVal ProductID As System.Integer, _
   ByRef Error As dsCreateCommandError_e _
) As Command
```

### C#

```csharp
Command CreateCommand4(
   System.string ApiUuid,
   System.string GlobalCmdName,
   System.string LocalCmdName,
   System.int HelpID,
   System.int ProductID,
   out dsCreateCommandError_e Error
)
```

### JScript

```
function CreateCommand4(
   ApiUuid : System.String,
   GlobalCmdName : System.String,
   LocalCmdName : System.String,
   HelpID : System.int,
   ProductID : System.int,
   Error : dsCreateCommandError_e
) : Command;
```

### Managed Extensions for C++

```
Command* CreateCommand4(
   System.string* ApiUuid,
   System.string* GlobalCmdName,
   System.string* LocalCmdName,
   System.int HelpID,
   System.int ProductID,
   [PARAMFLAG::Out] dsCreateCommandError_e Error
)
```

### C++/CLI

```cpp
Command^ CreateCommand4(
   System.String^ ApiUuid,
   System.String^ GlobalCmdName,
   System.String^ LocalCmdName,
   System.int HelpID,
   System.int ProductID,
   [Out] dsCreateCommandError_e Error
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or non add-in application
- `GlobalCmdName`: Unique name for the global command, which is not displayed to the user but which can be used as input
- `LocalCmdName`: Unique name for the localized command, which is displayed to the user and which can be used as input
- `HelpID`: ID of the context-sensitive help topic to open when F1 is pressed
- `ProductID`: Product ID of the system help
- `Error`: Status of creating the command as defined in [dsCreateCommandError_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateCommandError_e.html)

### Return Value

[Command](Interop.dsAutomation~Interop.dsAutomation.ICommand.html)

## Remarks

If either GlobalCmdName or LocalCmdName already exists, then dsCreateCommand_e.dsCreateCommandError_CommandNameExisted is returned for Error.

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
[IApplication::RemoveCommand Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~RemoveCommand.html)

## Availability

DraftSight 2019 SP0
