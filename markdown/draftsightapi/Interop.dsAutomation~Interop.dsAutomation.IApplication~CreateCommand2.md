---
title: "CreateCommand2 Method (IApplication)"
project: ""
interface: "IApplication"
member: "CreateCommand2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand2.html"
---

# CreateCommand2 Method (IApplication)

Obsolete. Superseded by [IApplication::CreateCommand3](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand3.html) and [IApplication::CreateCommand4](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand4.html).

## Syntax

### Visual Basic

```vb
Function CreateCommand2( _
   ByVal ApiUuid As System.String, _
   ByVal GlobalCmdName As System.String, _
   ByVal LocalCmdName As System.String, _
   ByRef Error As dsCreateCommandError_e _
) As Command
```

### C#

```csharp
Command CreateCommand2(
   System.string ApiUuid,
   System.string GlobalCmdName,
   System.string LocalCmdName,
   out dsCreateCommandError_e Error
)
```

### JScript

```
function CreateCommand2(
   ApiUuid : System.String,
   GlobalCmdName : System.String,
   LocalCmdName : System.String,
   Error : dsCreateCommandError_e
) : Command;
```

### Managed Extensions for C++

```
Command* CreateCommand2(
   System.string* ApiUuid,
   System.string* GlobalCmdName,
   System.string* LocalCmdName,
   [PARAMFLAG::Out] dsCreateCommandError_e Error
)
```

### C++/CLI

```cpp
Command^ CreateCommand2(
   System.String^ ApiUuid,
   System.String^ GlobalCmdName,
   System.String^ LocalCmdName,
   [Out] dsCreateCommandError_e Error
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or non add-in application
- `GlobalCmdName`: Unique name for the global command, which is not displayed to the user but which can be used as input
- `LocalCmdName`: Unique name for the localized command, which is displayed to the user and which can be used as input
- `Error`: Status of creating the command as defined in [dsCreateCommandError_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateCommandError_e.html)

### Return Value

[Command](Interop.dsAutomation~Interop.dsAutomation.ICommand.html)

## Examples

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

DraftSight V1R5.0
