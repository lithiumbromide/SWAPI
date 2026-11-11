---
title: "PromptForBool Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForBool"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForBool.html"
---

# PromptForBool Method (ICommandMessage)

Displays the specified prompt and default Boolean value in the command window and gets the Boolean input by the user.

## Syntax

### Visual Basic

```vb
Function PromptForBool( _
   ByVal Prompt As System.String, _
   ByVal StringForTrue As System.String, _
   ByVal StringForFalse As System.String, _
   ByVal DefaultValue As System.Boolean, _
   ByRef Value As System.Boolean _
) As System.Boolean
```

### C#

```csharp
System.bool PromptForBool(
   System.string Prompt,
   System.string StringForTrue,
   System.string StringForFalse,
   System.bool DefaultValue,
   out System.bool Value
)
```

### JScript

```
function PromptForBool(
   Prompt : System.String,
   StringForTrue : System.String,
   StringForFalse : System.String,
   DefaultValue : System.boolean,
   Value : System.boolean
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PromptForBool(
   System.string* Prompt,
   System.string* StringForTrue,
   System.string* StringForFalse,
   System.bool DefaultValue,
   [PARAMFLAG::Out] System.bool Value
)
```

### C++/CLI

```cpp
System.bool PromptForBool(
   System.String^ Prompt,
   System.String^ StringForTrue,
   System.String^ StringForFalse,
   System.bool DefaultValue,
   [Out] System.bool Value
)
```

### Parameters

- `Prompt`: Text of prompt
- `StringForTrue`: Text that indicates to return true (see **Remarks**)
- `StringForFalse`: Text that indicates to return false (see **Remarks**)
- `DefaultValue`: Default value
- `Value`: Boolean value

### Return Value

True if the prompt appears in the command window, false if not

## Remarks

StringForTrue and StringForFalse:

- can contain any combination of numbers, letters, and hyphens or only numbers, only letters, or only hyphens.
- cannot contain spaces or any other special characters or symbols.

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForBoolOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForBoolOrKeyword.html)

## Availability

DraftSight V1R1.1
