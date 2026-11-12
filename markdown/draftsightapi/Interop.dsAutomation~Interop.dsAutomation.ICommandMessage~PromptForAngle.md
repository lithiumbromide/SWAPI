---
title: "PromptForAngle Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForAngle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForAngle.html"
---

# PromptForAngle Method (ICommandMessage)

Displays the specified prompt and default value for an angle in the command window and gets the angle input by the user.

## Syntax

### Visual Basic

```vb
Function PromptForAngle( _
   ByVal Prompt As System.String, _
   ByVal DefaultValue As System.Double, _
   ByRef Value As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool PromptForAngle(
   System.string Prompt,
   System.double DefaultValue,
   out System.double Value
)
```

### JScript

```
function PromptForAngle(
   Prompt : System.String,
   DefaultValue : System.double,
   Value : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PromptForAngle(
   System.string* Prompt,
   System.double DefaultValue,
   [PARAMFLAG::Out] System.double Value
)
```

### C++/CLI

```cpp
System.bool PromptForAngle(
   System.String^ Prompt,
   System.double DefaultValue,
   [Out] System.double Value
)
```

### Parameters

- `Prompt`: Prompt message
- `DefaultValue`: Default value
- `Value`: User input angle

### Return Value

True if the prompt appears in the command window, false if not

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForAngleOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForAngleOrKeyword.html)

## Availability

DraftSight V1R1.4
