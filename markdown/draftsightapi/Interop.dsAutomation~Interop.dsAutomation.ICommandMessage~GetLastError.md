---
title: "GetLastError Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "GetLastError"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~GetLastError.html"
---

# GetLastError Method (ICommandMessage)

Displays the status of the last-run command in the command window.

## Syntax

### Visual Basic

```vb
Function GetLastError() As dsRunCommandError_e
```

### C#

```csharp
dsRunCommandError_e GetLastError()
```

### JScript

```
function GetLastError() : dsRunCommandError_e;
```

### Managed Extensions for C++

```
dsRunCommandError_e GetLastError();
```

### C++/CLI

```cpp
dsRunCommandError_e GetLastError();
```

### Return Value

Status of last-run command as defined in [dsRunCommandError_e](Interop.dsAutomation~Interop.dsAutomation.dsRunCommandError_e.html)

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[Application::RunCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~RunCommand.html)
[ICommand::LastError Property](Interop.dsAutomation~Interop.dsAutomation.ICommand~LastError.html)

## Availability

DraftSight V1R3.0
