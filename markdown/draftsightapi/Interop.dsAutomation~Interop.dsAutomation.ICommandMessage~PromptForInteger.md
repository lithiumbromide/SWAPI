---
title: "PromptForInteger Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForInteger"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForInteger.html"
---

# PromptForInteger Method (ICommandMessage)

Displays the specified prompt and default value for the integer or long in the command window and gets the integer or long input by the user.

## Syntax

### Visual Basic

```vb
Function PromptForInteger( _
   ByVal Prompt As System.String, _
   ByVal DefaultValue As System.Integer, _
   ByRef Value As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool PromptForInteger(
   System.string Prompt,
   System.int DefaultValue,
   out System.int Value
)
```

### JScript

```
function PromptForInteger(
   Prompt : System.String,
   DefaultValue : System.int,
   Value : System.int
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PromptForInteger(
   System.string* Prompt,
   System.int DefaultValue,
   [PARAMFLAG::Out] System.int Value
)
```

### C++/CLI

```cpp
System.bool PromptForInteger(
   System.String^ Prompt,
   System.int DefaultValue,
   [Out] System.int Value
)
```

### Parameters

- `Prompt`: Text of prompt
- `DefaultValue`: Default integer or long value
- `Value`: Integer or long value

### Return Value

True if the prompt is displayed in the command window, false if not

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForIntegerOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForIntegerOrKeyword.html)

## Availability

DraftSight V1R1.1
