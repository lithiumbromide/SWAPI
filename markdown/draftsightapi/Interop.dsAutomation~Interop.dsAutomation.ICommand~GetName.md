---
title: "GetName Method (ICommand)"
project: ""
interface: "ICommand"
member: "GetName"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommand~GetName.html"
---

# GetName Method (ICommand)

Gets the command's local name, which is displayed to the user and which can be used as input.

## Syntax

### Visual Basic

```vb
Function GetName() As System.String
```

### C#

```csharp
System.string GetName()
```

### JScript

```
function GetName() : System.String;
```

### Managed Extensions for C++

```
System.string* GetName();
```

### C++/CLI

```cpp
System.String^ GetName();
```

### Return Value

Command's local name

## Examples

This code snippet shows how to get the local name of the command.

##### COM native C++

//Get command name

bstr_t commandName = m_DsCommand->GetName();

## See Also

[ICommand Interface](Interop.dsAutomation~Interop.dsAutomation.ICommand.html)
[ICommand Members](Interop.dsAutomation~Interop.dsAutomation.ICommand_members.html)
[ICommand::GetGlobalName ()](Interop.dsAutomation~Interop.dsAutomation.ICommand~GetGlobalName.html)

## Availability

DraftSight V1R1
