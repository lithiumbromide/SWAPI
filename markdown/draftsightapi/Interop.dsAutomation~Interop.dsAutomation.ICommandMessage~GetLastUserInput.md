---
title: "GetLastUserInput Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "GetLastUserInput"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~GetLastUserInput.html"
---

# GetLastUserInput Method (ICommandMessage)

Gets the last value input by a user in the command window.

## Syntax

### Visual Basic

```vb
Function GetLastUserInput() As System.String
```

### C#

```csharp
System.string GetLastUserInput()
```

### JScript

```
function GetLastUserInput() : System.String;
```

### Managed Extensions for C++

```
System.string* GetLastUserInput();
```

### C++/CLI

```cpp
System.String^ GetLastUserInput();
```

### Return Value

Last value input by a user in the command window (see **Remarks**)

## Remarks

If the user:

- picked a point instead of typing a value for a point, then **Return Value** is empty.
- input an invalid value for an angle, then checking **Return Value** might be helpful.

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)

## Availability

DraftSight V1R6.0
