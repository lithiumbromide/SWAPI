---
title: "LastError Property (ICommand)"
project: ""
interface: "ICommand"
member: "LastError"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommand~LastError.html"
---

# LastError Property (ICommand)

Gets or sets the status of the last-run command.

## Syntax

### Visual Basic

```vb
Property LastError As dsRunCommandError_e
```

### C#

```csharp
dsRunCommandError_e LastError {get; set;}
```

### JScript

```
function get,set LastError : dsRunCommandError_e
```

### Managed Extensions for C++

```
__property dsRunCommandError_e get_LastError();
__property void set_LastError(
   dsRunCommandError_e value
);
```

### C++/CLI

```cpp
property dsRunCommandError_e LastError {
   dsRunCommandError_e get();
   void set (    dsRunCommandError_e value);
}
```

### Property Value

Status of the last-run command as defined in [dsRunCommandError_e](Interop.dsAutomation~Interop.dsAutomation.dsRunCommandError_e.html)

## See Also

[ICommand Interface](Interop.dsAutomation~Interop.dsAutomation.ICommand.html)
[ICommand Members](Interop.dsAutomation~Interop.dsAutomation.ICommand_members.html)
[IApplication::RunCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~RunCommand.html)
[ICommandMessage::GetLastError Method](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~GetLastError.html)
