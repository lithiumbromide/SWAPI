---
title: "PromptForSelectionOrKeyword Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForSelectionOrKeyword"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForSelectionOrKeyword.html"
---

# PromptForSelectionOrKeyword Method (ICommandMessage)

Displays the specified prompt and local keywords for selecting one or more entities in the command window and gets the user's input.

## Syntax

### Visual Basic

```vb
Function PromptForSelectionOrKeyword( _
   ByVal SingleSelection As System.Boolean, _
   ByVal Prompt As System.String, _
   ByVal ErrorMsg As System.String, _
   ByVal GlobalKeywordStrArray As System.Object, _
   ByVal LocalKeywordStrArray As System.Object, _
   ByVal PromptInit As System.Integer, _
   ByRef Keyword As System.String _
) As dsPromptResultType_e
```

### C#

```csharp
dsPromptResultType_e PromptForSelectionOrKeyword(
   System.bool SingleSelection,
   System.string Prompt,
   System.string ErrorMsg,
   System.object GlobalKeywordStrArray,
   System.object LocalKeywordStrArray,
   System.int PromptInit,
   out System.string Keyword
)
```

### JScript

```
function PromptForSelectionOrKeyword(
   SingleSelection : System.boolean,
   Prompt : System.String,
   ErrorMsg : System.String,
   GlobalKeywordStrArray : System.Object,
   LocalKeywordStrArray : System.Object,
   PromptInit : System.int,
   Keyword : System.String
) : dsPromptResultType_e;
```

### Managed Extensions for C++

```
dsPromptResultType_e PromptForSelectionOrKeyword(
   System.bool SingleSelection,
   System.string* Prompt,
   System.string* ErrorMsg,
   System.Object* GlobalKeywordStrArray,
   System.Object* LocalKeywordStrArray,
   System.int PromptInit,
   [PARAMFLAG::Out] System.string* Keyword
)
```

### C++/CLI

```cpp
dsPromptResultType_e PromptForSelectionOrKeyword(
   System.bool SingleSelection,
   System.String^ Prompt,
   System.String^ ErrorMsg,
   System.Object^ GlobalKeywordStrArray,
   System.Object^ LocalKeywordStrArray,
   System.int PromptInit,
   [Out] System.String^ Keyword
)
```

### Parameters

- `SingleSelection`: True to prompt for a single selection, false to prompt for multiple selections
- `Prompt`: Prompt to display in the command window
- `ErrorMsg`: Error message to display in the command window when the user's input is invalid
- `GlobalKeywordStrArray`: Array of global keywords, which are typically language independent (see **Remarks**)
- `LocalKeywordStrArray`: Array of local keywords, which are typically translated to the local language (see **Remarks**)
- `PromptInit`: Prompt initialization as defined in [dsPromptInit_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptInit_e.html) (see **Remarks**)
- `Keyword`: Keyword input by the user

### Return Value

Result as defined in [dsPromptResultType_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptResultType_e.html)

## Remarks

Keywords are context-sensitive options that are available in the Options toolbar when executing a command. Local keywords can be seen in the prompt in the command window during user interaction. Global keywords cannot be seen in the prompt in the command window. However, users can type global keywords at the prompt in the command window if they know them.

If the PromptInit parameter is set to:

- dsPromptInit_e.dsPromptInit_NoDefault and a value is specified for DefaultValue, then the value is not used or displayed in the prompt in the command window.
- dsPromptInit_e.UsePromptExplanation, then call [ICommandMessage::PromptExplanation](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptExplanation.html) to specify the text for PromptInit.

You can allow or disallow the selection of an entity by calling [ISelectionManager::RemoveOptions](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~RemoveOptions.html) before calling this method.

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForSelection Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForSelection.html)
[ISelectionManager::PaperSpaceSelectionEnabled Property ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~PaperSpaceSelectionEnabled.html)

## Availability

DraftSight V1R4.0
