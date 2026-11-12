---
title: "PromptForOrientationOrKeyword Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForOrientationOrKeyword"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForOrientationOrKeyword.html"
---

# PromptForOrientationOrKeyword Method (ICommandMessage)

Obsolete. Superseded by [ICommandMessage::PromptForOrientationOrKeyword2.](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForOrientationOrKeyword2.html)

## Syntax

### Visual Basic

```vb
Function PromptForOrientationOrKeyword( _
   ByVal Prompt As System.String, _
   ByVal ErrorMsg As System.String, _
   ByVal GlobalKeywordStrArray As System.Object, _
   ByVal LocalKeywordStrArray As System.Object, _
   ByVal PromptInit As System.Integer, _
   ByVal DefaultValue As System.Double, _
   ByRef Keyword As System.String, _
   ByRef Value As System.Double _
) As dsPromptResultType_e
```

### C#

```csharp
dsPromptResultType_e PromptForOrientationOrKeyword(
   System.string Prompt,
   System.string ErrorMsg,
   System.object GlobalKeywordStrArray,
   System.object LocalKeywordStrArray,
   System.int PromptInit,
   System.double DefaultValue,
   out System.string Keyword,
   out System.double Value
)
```

### JScript

```
function PromptForOrientationOrKeyword(
   Prompt : System.String,
   ErrorMsg : System.String,
   GlobalKeywordStrArray : System.Object,
   LocalKeywordStrArray : System.Object,
   PromptInit : System.int,
   DefaultValue : System.double,
   Keyword : System.String,
   Value : System.double
) : dsPromptResultType_e;
```

### Managed Extensions for C++

```
dsPromptResultType_e PromptForOrientationOrKeyword(
   System.string* Prompt,
   System.string* ErrorMsg,
   System.Object* GlobalKeywordStrArray,
   System.Object* LocalKeywordStrArray,
   System.int PromptInit,
   System.double DefaultValue,
   [PARAMFLAG::Out] System.string* Keyword,
   [PARAMFLAG::Out] System.double Value
)
```

### C++/CLI

```cpp
dsPromptResultType_e PromptForOrientationOrKeyword(
   System.String^ Prompt,
   System.String^ ErrorMsg,
   System.Object^ GlobalKeywordStrArray,
   System.Object^ LocalKeywordStrArray,
   System.int PromptInit,
   System.double DefaultValue,
   [Out] System.String^ Keyword,
   [Out] System.double Value
)
```

### Parameters

- `Prompt`: Text to display as the prompt in the command window
- `ErrorMsg`: Error message to display in the command window when the user input is invalid
- `GlobalKeywordStrArray`: Array of global keywords, which are typically language independent (see **Remarks**)
- `LocalKeywordStrArray`: Array of local keywords, which are typically translated to the local language (see **Remarks**)
- `PromptInit`: Prompt initialization as defined in [dsPromptInit_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptInit_e.html) (see **Remarks**)
- `DefaultValue`: Default orientation value to show in the prompt in the command window (see **Remarks**)
- `Keyword`: Keyword input by the user
- `Value`: Orientation value input by the user

### Return Value

Result as defined in [dsPromptResultType_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptResultType_e.html)

## Remarks

Local keywords can be seen in the prompt in the command window during user interaction. Global keywords cannot be seen in the prompt in the command window. However, users can type global keywords at the prompt in the command window if they know them.

If the PromptInit parameter is set to:

- dsPromptInit_e.dsPromptInit_NoDefault and a value is specified for DefaultValue, then the value is not used or displayed in the prompt in the command window.
- dsPromptInit_e.UsePromptExplanation, then call [ICommandMessage::PromptExplanation](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptExplanation.html) to specify the text for PromptInit.

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForOrientation Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForOrientation.html)

## Availability

DraftSight V1R4.0
