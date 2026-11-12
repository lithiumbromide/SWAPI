---
title: "PromptForFileNameOrKeyword Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForFileNameOrKeyword"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForFileNameOrKeyword.html"
---

# PromptForFileNameOrKeyword Method (ICommandMessage)

Displays the specified prompt, local keywords, and default value for the file name in command window and gets the user's input.

## Syntax

### Visual Basic

```vb
Function PromptForFileNameOrKeyword( _
   ByVal Prompt As System.String, _
   ByVal ErrorMsg As System.String, _
   ByVal GlobalKeywordStrArray As System.Object, _
   ByVal LocalKeywordStrArray As System.Object, _
   ByVal PromptInit As System.Integer, _
   ByVal DefaultFileName As System.String, _
   ByRef Keyword As System.String, _
   ByRef FileName As System.String _
) As dsPromptResultType_e
```

### C#

```csharp
dsPromptResultType_e PromptForFileNameOrKeyword(
   System.string Prompt,
   System.string ErrorMsg,
   System.object GlobalKeywordStrArray,
   System.object LocalKeywordStrArray,
   System.int PromptInit,
   System.string DefaultFileName,
   out System.string Keyword,
   out System.string FileName
)
```

### JScript

```
function PromptForFileNameOrKeyword(
   Prompt : System.String,
   ErrorMsg : System.String,
   GlobalKeywordStrArray : System.Object,
   LocalKeywordStrArray : System.Object,
   PromptInit : System.int,
   DefaultFileName : System.String,
   Keyword : System.String,
   FileName : System.String
) : dsPromptResultType_e;
```

### Managed Extensions for C++

```
dsPromptResultType_e PromptForFileNameOrKeyword(
   System.string* Prompt,
   System.string* ErrorMsg,
   System.Object* GlobalKeywordStrArray,
   System.Object* LocalKeywordStrArray,
   System.int PromptInit,
   System.string* DefaultFileName,
   [PARAMFLAG::Out] System.string* Keyword,
   [PARAMFLAG::Out] System.string* FileName
)
```

### C++/CLI

```cpp
dsPromptResultType_e PromptForFileNameOrKeyword(
   System.String^ Prompt,
   System.String^ ErrorMsg,
   System.Object^ GlobalKeywordStrArray,
   System.Object^ LocalKeywordStrArray,
   System.int PromptInit,
   System.String^ DefaultFileName,
   [Out] System.String^ Keyword,
   [Out] System.String^ FileName
)
```

### Parameters

- `Prompt`: Text for the prompt to display in the command window
- `ErrorMsg`: Error message to display in the command window when the user's input is invalid
- `GlobalKeywordStrArray`: Array of global keywords, which are typically language independent (see **Remarks**)
- `LocalKeywordStrArray`: Array of local keywords, which are typically translated to the local language (see **Remarks**)
- `PromptInit`: Prompt initialization as defined in [dsPromptInit_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptInit_e.html) (see **Remarks**)
- `DefaultFileName`: Default value for the path and file name to display in the command window (see **Remarks**)
- `Keyword`: Keyword input by the user
- `FileName`: Path and file name input by the user

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
[ICommandMessage::PromptForFileName Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForFileName.html)

## Availability

DraftSight V1R4.0
