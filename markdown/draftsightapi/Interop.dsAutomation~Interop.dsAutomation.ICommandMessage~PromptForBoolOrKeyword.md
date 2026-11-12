---
title: "PromptForBoolOrKeyword Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForBoolOrKeyword"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForBoolOrKeyword.html"
---

# PromptForBoolOrKeyword Method (ICommandMessage)

Displays the specified prompt, local keywords, and default value for the Boolean in the command window and gets the user's input.

## Syntax

### Visual Basic

```vb
Function PromptForBoolOrKeyword( _
   ByVal Prompt As System.String, _
   ByVal ErrorMsg As System.String, _
   ByVal GlobalKeywordStrArray As System.Object, _
   ByVal LocalKeywordStrArray As System.Object, _
   ByVal PromptInit As System.Integer, _
   ByVal StringForTrue As System.String, _
   ByVal StringForFalse As System.String, _
   ByVal DefaultValue As System.Boolean, _
   ByRef Keyword As System.String, _
   ByRef Value As System.Boolean _
) As dsPromptResultType_e
```

### C#

```csharp
dsPromptResultType_e PromptForBoolOrKeyword(
   System.string Prompt,
   System.string ErrorMsg,
   System.object GlobalKeywordStrArray,
   System.object LocalKeywordStrArray,
   System.int PromptInit,
   System.string StringForTrue,
   System.string StringForFalse,
   System.bool DefaultValue,
   out System.string Keyword,
   out System.bool Value
)
```

### JScript

```
function PromptForBoolOrKeyword(
   Prompt : System.String,
   ErrorMsg : System.String,
   GlobalKeywordStrArray : System.Object,
   LocalKeywordStrArray : System.Object,
   PromptInit : System.int,
   StringForTrue : System.String,
   StringForFalse : System.String,
   DefaultValue : System.boolean,
   Keyword : System.String,
   Value : System.boolean
) : dsPromptResultType_e;
```

### Managed Extensions for C++

```
dsPromptResultType_e PromptForBoolOrKeyword(
   System.string* Prompt,
   System.string* ErrorMsg,
   System.Object* GlobalKeywordStrArray,
   System.Object* LocalKeywordStrArray,
   System.int PromptInit,
   System.string* StringForTrue,
   System.string* StringForFalse,
   System.bool DefaultValue,
   [PARAMFLAG::Out] System.string* Keyword,
   [PARAMFLAG::Out] System.bool Value
)
```

### C++/CLI

```cpp
dsPromptResultType_e PromptForBoolOrKeyword(
   System.String^ Prompt,
   System.String^ ErrorMsg,
   System.Object^ GlobalKeywordStrArray,
   System.Object^ LocalKeywordStrArray,
   System.int PromptInit,
   System.String^ StringForTrue,
   System.String^ StringForFalse,
   System.bool DefaultValue,
   [Out] System.String^ Keyword,
   [Out] System.bool Value
)
```

### Parameters

- `Prompt`: Text to display as the prompt in the command window
- `ErrorMsg`: Error message to display in the command window when the user input is invalid
- `GlobalKeywordStrArray`: Array of global keywords, which are typically language independent (see **Remarks**)
- `LocalKeywordStrArray`: Array of local keywords to display in the command window, which are typically translated to the local language (see **Remarks**)
- `PromptInit`: Prompt initialization as defined in [dsPromptInit_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptInit_e.html) (see **Remarks**)
- `StringForTrue`: Text that indicates to return true (see **Remarks**)
- `StringForFalse`: Text that indicates to return false (see **Remarks**)
- `DefaultValue`: Default Boolean value to display in the prompt in the command window (see **Remarks**)
- `Keyword`: Keyword input by the user
- `Value`: Boolean value input by the user

### Return Value

Result as defined in [dsPromptResultType_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptResultType_e.html)

## Remarks

Keywords are context-sensitive options that are available in the Options toolbar when executing a command. Local keywords can be seen in the prompt in the command window during user interaction. Global keywords cannot be seen in the prompt in the command window. However, users can type global keywords at the prompt in the command window if they know them.

The StringForTrue and StringForFalse parameters:

- can contain any combination of numbers, letters, and hyphens or only numbers, only letters, or only hyphens.
- cannot contain spaces or any other special characters or symbols.

If the PromptInit parameter is set to:

- dsPromptInit_e.dsPromptInit_NoDefault and a value is specified for DefaultValue, then the value is not used or displayed in the prompt in the command window.
- dsPromptInit_e.UsePromptExplanation, then call [ICommandMessage::PromptExplanation](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptExplanation.html) to specify the text for PromptInit.

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForBool Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForBool.html)

## Availability

DraftSight V1R4.0
