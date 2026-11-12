---
title: "CommandString Property (IUserCommand)"
project: ""
interface: "IUserCommand"
member: "CommandString"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IUserCommand~CommandString.html"
---

# CommandString Property (IUserCommand)

Gets or sets the user command's command string.

## Syntax

### Visual Basic

```vb
Property CommandString As System.String
```

### C#

```csharp
System.string CommandString {get; set;}
```

### JScript

```
function get,set CommandString : System.String
```

### Managed Extensions for C++

```
__property System.string* get_CommandString();
__property void set_CommandString(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ CommandString {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

User command's command string

## Remarks

The return value is the string specified for [IApplication::CreateUserCommand's](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateUserCommand.html) CmdString parameter (e.g., ^C^C`apiCmd`) or the string set by this property.

## See Also

[IUserCommand Interface](Interop.dsAutomation~Interop.dsAutomation.IUserCommand.html)
[IUserCommand Members](Interop.dsAutomation~Interop.dsAutomation.IUserCommand_members.html)

## Availability

DraftSight V1R1
