---
title: "SetID Method (IUserCommand)"
project: ""
interface: "IUserCommand"
member: "SetID"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IUserCommand~SetID.html"
---

# SetID Method (IUserCommand)

Sets the user-defined ID of this user command.

## Syntax

### Visual Basic

```vb
Sub SetID( _
   ByVal NewVal As System.String _
)
```

### C#

```csharp
void SetID(
   System.string NewVal
)
```

### JScript

```
function SetID(
   NewVal : System.String
);
```

### Managed Extensions for C++

```
void SetID(
   System.string* NewVal
)
```

### C++/CLI

```cpp
void SetID(
   System.String^ NewVal
)
```

### Parameters

- `NewVal`: Unique ID of this user command

## Remarks

Use a GUID tool to generate a unique NewVal.

It is recommended that you set the IDs of only custom controls. Do not attempt to change the IDs of system controls, as they are used for internal processing.

## See Also

[IUserCommand Interface](Interop.dsAutomation~Interop.dsAutomation.IUserCommand.html)
[IUserCommand Members](Interop.dsAutomation~Interop.dsAutomation.IUserCommand_members.html)
[IUserCommand::GetID Method ()](Interop.dsAutomation~Interop.dsAutomation.IUserCommand~GetID.html)

## Availability

DraftSight 2019 SP0
