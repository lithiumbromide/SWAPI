---
title: "PromptForDistance Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForDistance"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForDistance.html"
---

# PromptForDistance Method (ICommandMessage)

Displays the specified prompt and default value for the linear distance in the command window and gets the linear distance input by the user.

## Syntax

### Visual Basic

```vb
Function PromptForDistance( _
   ByVal Prompt As System.String, _
   ByVal DefaultValue As System.Double, _
   ByRef Value As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool PromptForDistance(
   System.string Prompt,
   System.double DefaultValue,
   out System.double Value
)
```

### JScript

```
function PromptForDistance(
   Prompt : System.String,
   DefaultValue : System.double,
   Value : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PromptForDistance(
   System.string* Prompt,
   System.double DefaultValue,
   [PARAMFLAG::Out] System.double Value
)
```

### C++/CLI

```cpp
System.bool PromptForDistance(
   System.String^ Prompt,
   System.double DefaultValue,
   [Out] System.double Value
)
```

### Parameters

- `Prompt`: Prompt message
- `DefaultValue`: Default value
- `Value`: User input linear distance

### Return Value

True if the prompt appears in the command window, false if not

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForDistanceOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForDistanceOrKeyword.html)

## Availability

DraftSight V1R1.4
