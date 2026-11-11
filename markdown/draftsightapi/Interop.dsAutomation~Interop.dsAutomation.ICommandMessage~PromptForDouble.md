---
title: "PromptForDouble Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForDouble"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForDouble.html"
---

# PromptForDouble Method (ICommandMessage)

Displays the specified prompt and default value for the double in the command window and gets the double input by the user.

## Syntax

### Visual Basic

```vb
Function PromptForDouble( _
   ByVal Prompt As System.String, _
   ByVal DefaultValue As System.Double, _
   ByRef Value As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool PromptForDouble(
   System.string Prompt,
   System.double DefaultValue,
   out System.double Value
)
```

### JScript

```
function PromptForDouble(
   Prompt : System.String,
   DefaultValue : System.double,
   Value : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PromptForDouble(
   System.string* Prompt,
   System.double DefaultValue,
   [PARAMFLAG::Out] System.double Value
)
```

### C++/CLI

```cpp
System.bool PromptForDouble(
   System.String^ Prompt,
   System.double DefaultValue,
   [Out] System.double Value
)
```

### Parameters

- `Prompt`: Text of prompt
- `DefaultValue`: Default double value
- `Value`: Double value

### Return Value

True if the prompt is displayed in the command window, false if not

## Examples

[Prompt for Mouse or Keyword (C#)](Prompt_for_Mouse_or_Keyword_Example_CSharp.htm)

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForDoubleOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForDoubleOrKeyword.html)

## Availability

DraftSight V1R1.1
