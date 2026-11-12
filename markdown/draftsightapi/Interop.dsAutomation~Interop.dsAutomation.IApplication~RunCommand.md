---
title: "RunCommand Method (IApplication)"
project: ""
interface: "IApplication"
member: "RunCommand"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~RunCommand.html"
---

# RunCommand Method (IApplication)

Obsolete. Superseded by [IApplication::RunCommand2](Interop.dsAutomation~Interop.dsAutomation.IApplication~RunCommand2.html).

## Syntax

### Visual Basic

```vb
Function RunCommand( _
   ByVal CommandString As System.String, _
   ByVal HideCommandTitle As System.Boolean _
) As dsRunCommandError_e
```

### C#

```csharp
dsRunCommandError_e RunCommand(
   System.string CommandString,
   System.bool HideCommandTitle
)
```

### JScript

```
function RunCommand(
   CommandString : System.String,
   HideCommandTitle : System.boolean
) : dsRunCommandError_e;
```

### Managed Extensions for C++

```
dsRunCommandError_e RunCommand(
   System.string* CommandString,
   System.bool HideCommandTitle
)
```

### C++/CLI

```cpp
dsRunCommandError_e RunCommand(
   System.String^ CommandString,
   System.bool HideCommandTitle
)
```

### Parameters

- `CommandString`: Name of command to run (see **Remarks**)
- `HideCommandTitle`: True to hide the command in the command window, false to show the command in the command window

### Return Value

Status of running the command as defined in [dsRunCommandError_e](Interop.dsAutomation~interop.dsAutomation.dsRunCommandError_e.html)

## Remarks

Depending on the programming language that you use, either:

For example:

| To delete all entities in a drawing in this programming language... | Call... |
| --- | --- |
| C# | int state; state = (int)dsApp. RunCommand (" DELETE ALL\n\n ", false); |
| VB.NET | Dim state as Integer; state = dsApp. RunCommand (" DELETE ALL" & Chr(10) & Chr(10) , False) |
| VBA | Dim state as Long; state = dsApp. RunCommand (" DELETE ALL" & Chr(10) & Chr(10) , False) |

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::AbortRunningCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~AbortRunningCommand.html)
[IApplication::CreateCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand.html)
[IApplication::GetRunningCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRunningCommand.html)
[ICommand Interface](Interop.dsAutomation~Interop.dsAutomation.ICommand.html)
[ICommand Event ExecuteNotify](Interop.dsAutomation~Interop.dsAutomation._ICommandEvents_ExecuteNotifyEventHandler.html)
[ICommandMessage::GetLastError Method](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~GetLastError.html)
[ICommand::LastError Property](Interop.dsAutomation~Interop.dsAutomation.ICommand~LastError.html)
[IApplication Event CommandCancelNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandCancelNotifyEventHandler.html)
[IApplication Event CommandPostNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandPostNotifyEventHandler.html)
[IApplication Events CommandPreNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_CommandPreNotifyEventHandler.html)

## Availability

DraftSight V1R1
