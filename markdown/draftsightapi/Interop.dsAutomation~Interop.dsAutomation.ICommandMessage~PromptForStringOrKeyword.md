---
title: "PromptForStringOrKeyword Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForStringOrKeyword"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForStringOrKeyword.html"
---

# PromptForStringOrKeyword Method (ICommandMessage)

Displays the specified prompt, local keywords, and default string in the command window and gets the user's input.

## Syntax

### Visual Basic

```vb
Function PromptForStringOrKeyword( _
   ByVal IgnoreSpaces As System.Boolean, _
   ByVal Prompt As System.String, _
   ByVal ErrorMsg As System.String, _
   ByVal GlobalKeywordStrArray As System.Object, _
   ByVal LocalKeywordStrArray As System.Object, _
   ByVal PromptInit As System.Integer, _
   ByVal DefaultString As System.String, _
   ByRef Keyword As System.String, _
   ByRef ResultString As System.String _
) As dsPromptResultType_e
```

### C#

```csharp
dsPromptResultType_e PromptForStringOrKeyword(
   System.bool IgnoreSpaces,
   System.string Prompt,
   System.string ErrorMsg,
   System.object GlobalKeywordStrArray,
   System.object LocalKeywordStrArray,
   System.int PromptInit,
   System.string DefaultString,
   out System.string Keyword,
   out System.string ResultString
)
```

### JScript

```
function PromptForStringOrKeyword(
   IgnoreSpaces : System.boolean,
   Prompt : System.String,
   ErrorMsg : System.String,
   GlobalKeywordStrArray : System.Object,
   LocalKeywordStrArray : System.Object,
   PromptInit : System.int,
   DefaultString : System.String,
   Keyword : System.String,
   ResultString : System.String
) : dsPromptResultType_e;
```

### Managed Extensions for C++

```
dsPromptResultType_e PromptForStringOrKeyword(
   System.bool IgnoreSpaces,
   System.string* Prompt,
   System.string* ErrorMsg,
   System.Object* GlobalKeywordStrArray,
   System.Object* LocalKeywordStrArray,
   System.int PromptInit,
   System.string* DefaultString,
   [PARAMFLAG::Out] System.string* Keyword,
   [PARAMFLAG::Out] System.string* ResultString
)
```

### C++/CLI

```cpp
dsPromptResultType_e PromptForStringOrKeyword(
   System.bool IgnoreSpaces,
   System.String^ Prompt,
   System.String^ ErrorMsg,
   System.Object^ GlobalKeywordStrArray,
   System.Object^ LocalKeywordStrArray,
   System.int PromptInit,
   System.String^ DefaultString,
   [Out] System.String^ Keyword,
   [Out] System.String^ ResultString
)
```

### Parameters

- `IgnoreSpaces`: True to ignore spaces, false to not
- `Prompt`: Text to display as the prompt in the command window
- `ErrorMsg`: Error message to display in the command window when the user input is invalid
- `GlobalKeywordStrArray`: Array of global keywords, which are typically language independent (see **Remarks**)
- `LocalKeywordStrArray`: Array of local keywords, which are typically translated to the local language (see **Remarks**)
- `PromptInit`: Prompt initialization as defined in [dsPromptInit_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptInit_e.html) (see **Remarks**)
- `DefaultString`: Default string to show at the prompt in the command window (see **Remarks**)
- `Keyword`: Keyword input by user
- `ResultString`: String input by user

### Return Value

Result as defined in [dsPromptResultType_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptResultType_e.html)

## Remarks

Keywords are context-sensitive options that are available in the Options toolbar when executing a command. Local keywords can be seen in the prompt in the command window during user interaction. Global keywords cannot be seen in the prompt in the command window. However, users can type global keywords at the prompt in the command window if they know them.

If the PromptInit parameter is set to:

- dsPromptInit_e.dsPromptInit_NoDefault and a value is specified for DefaultValue, then the value is not used or displayed in the prompt in the command window.
- dsPromptInit_e.UsePromptExplanation, then call [ICommandMessage::PromptExplanation](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptExplanation.html) to specify the text for PromptInit.

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForString Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForString.html)

## Availability

DraftSight V1R4.0
