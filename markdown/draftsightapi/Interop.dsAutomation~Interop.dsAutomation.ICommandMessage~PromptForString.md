---
title: "PromptForString Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForString"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForString.html"
---

# PromptForString Method (ICommandMessage)

Displays the specified prompt and default value in the command window and gets the user's input.

## Syntax

### Visual Basic

```vb
Function PromptForString( _
   ByVal IgnoreSpaces As System.Boolean, _
   ByVal Prompt As System.String, _
   ByVal DefaultString As System.String, _
   ByRef ResultString As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool PromptForString(
   System.bool IgnoreSpaces,
   System.string Prompt,
   System.string DefaultString,
   out System.string ResultString
)
```

### JScript

```
function PromptForString(
   IgnoreSpaces : System.boolean,
   Prompt : System.String,
   DefaultString : System.String,
   ResultString : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PromptForString(
   System.bool IgnoreSpaces,
   System.string* Prompt,
   System.string* DefaultString,
   [PARAMFLAG::Out] System.string* ResultString
)
```

### C++/CLI

```cpp
System.bool PromptForString(
   System.bool IgnoreSpaces,
   System.String^ Prompt,
   System.String^ DefaultString,
   [Out] System.String^ ResultString
)
```

### Parameters

- `IgnoreSpaces`: True to ignore spaces, false to not
- `Prompt`: Prompt message
- `DefaultString`: Default value
- `ResultString`: User input value

### Return Value

True if the prompt appears in the command window, false if not

## Examples

[Prompt for Mouse or Keyword (C#)](Prompt_for_Mouse_or_Keyword_Example_CSharp.htm)

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForStringOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForStringOrKeyword.html)

## Availability

DraftSight V1R1.4
