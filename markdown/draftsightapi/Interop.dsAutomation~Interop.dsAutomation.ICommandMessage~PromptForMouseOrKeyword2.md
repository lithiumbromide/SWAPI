---
title: "PromptForMouseOrKeyword2 Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForMouseOrKeyword2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForMouseOrKeyword2.html"
---

# PromptForMouseOrKeyword2 Method (ICommandMessage)

Displays the specified prompt in the command window with the specified local keywords, base point, and default mouse click point. Returns the user's input either from the command window (keyword) or the mouse/keyboard (mouse click point, mouse event type, and keyboard modificators).

## Syntax

### Visual Basic

```vb
Function PromptForMouseOrKeyword2( _
   ByVal Prompt As System.String, _
   ByVal ErrorMsg As System.String, _
   ByVal GlobalKeywordStrArray As System.Object, _
   ByVal LocalKeywordStrArray As System.Object, _
   ByVal PromptInit As System.Integer, _
   ByVal ShowRubberLine As System.Boolean, _
   ByVal DefaultValue As MathPoint, _
   ByVal BasePoint As MathPoint, _
   ByVal Plane As MathPlane, _
   ByRef Keyword As System.String, _
   ByRef ResultPoint As MathPoint, _
   ByRef Modificators As dsPromptKeyboardModificators2_e, _
   ByRef MouseResult As dsMouseEventType_e _
) As dsPromptResultType_e
```

### C#

```csharp
dsPromptResultType_e PromptForMouseOrKeyword2(
   System.string Prompt,
   System.string ErrorMsg,
   System.object GlobalKeywordStrArray,
   System.object LocalKeywordStrArray,
   System.int PromptInit,
   System.bool ShowRubberLine,
   MathPoint DefaultValue,
   MathPoint BasePoint,
   MathPlane Plane,
   out System.string Keyword,
   out MathPoint ResultPoint,
   out dsPromptKeyboardModificators2_e Modificators,
   out dsMouseEventType_e MouseResult
)
```

### JScript

```
function PromptForMouseOrKeyword2(
   Prompt : System.String,
   ErrorMsg : System.String,
   GlobalKeywordStrArray : System.Object,
   LocalKeywordStrArray : System.Object,
   PromptInit : System.int,
   ShowRubberLine : System.boolean,
   DefaultValue : MathPoint,
   BasePoint : MathPoint,
   Plane : MathPlane,
   Keyword : System.String,
   ResultPoint : MathPoint,
   Modificators : dsPromptKeyboardModificators2_e,
   MouseResult : dsMouseEventType_e
) : dsPromptResultType_e;
```

### Managed Extensions for C++

```
dsPromptResultType_e PromptForMouseOrKeyword2(
   System.string* Prompt,
   System.string* ErrorMsg,
   System.Object* GlobalKeywordStrArray,
   System.Object* LocalKeywordStrArray,
   System.int PromptInit,
   System.bool ShowRubberLine,
   MathPoint* DefaultValue,
   MathPoint* BasePoint,
   MathPlane* Plane,
   [PARAMFLAG::Out] System.string* Keyword,
   [PARAMFLAG::Out] MathPoint* ResultPoint,
   [PARAMFLAG::Out] dsPromptKeyboardModificators2_e Modificators,
   [PARAMFLAG::Out] dsMouseEventType_e MouseResult
)
```

### C++/CLI

```cpp
dsPromptResultType_e PromptForMouseOrKeyword2(
   System.String^ Prompt,
   System.String^ ErrorMsg,
   System.Object^ GlobalKeywordStrArray,
   System.Object^ LocalKeywordStrArray,
   System.int PromptInit,
   System.bool ShowRubberLine,
   MathPoint^ DefaultValue,
   MathPoint^ BasePoint,
   MathPlane^ Plane,
   [Out] System.String^ Keyword,
   [Out] MathPoint^ ResultPoint,
   [Out] dsPromptKeyboardModificators2_e Modificators,
   [Out] dsMouseEventType_e MouseResult
)
```

### Parameters

- `Prompt`: Text for the prompt to display in the command window
- `ErrorMsg`: Error message to display in the command window if the user input is invalid
- `GlobalKeywordStrArray`: Array of global keyword strings, which typically are language independent (see **Remarks**)
- `LocalKeywordStrArray`: Array of local keyword strings, which are typically translated to the local language (see **Remarks**)
- `PromptInit`: Prompt initialization as defined in [dsPromptInit_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptInit_e.html) (see **Remarks**)
- `ShowRubberLine`: True to display a rubber band that stretches from the origin, or from the BasePoint, to the location of the cursor; false to not display the rubber band (see **Remarks**)
- `DefaultValue`: Default value for the mouse click [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) in the command window prompt (see **Remarks**)
- `BasePoint`: [Base point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) (see **Remarks**)
- `Plane`: Projection [plane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)
- `Keyword`: User's keyword input
- `ResultPoint`: User's click [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `Modificators`: User's key click modifiers as defined in [dsPromptKeyboardModificators2_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptKeyboardModificators2_e.html)
- `MouseResult`: User's mouse click type as defined in [dsMouseEventType_e](Interop.dsAutomation~Interop.dsAutomation.dsMouseEventType_e.html)

### Return Value

Result as defined in [dsPromptResultType_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptResultType_e.html)

## Examples

[Prompt for Mouse or Keyword (C#)](Prompt_for_Mouse_or_Keyword_Example_CSharp.htm)
[Prompt for Mouse or Keyword (Javascript)](Prompt_for_Mouse_or_Keyword_Example_JS.htm)
[Prompt for Mouse or Keyword (VBA)](Prompt_for_Mouse_or_Keyword_Example_VBA.htm)
[Prompt for Mouse or Keyword (VB.NET)](Prompt_for_Mouse_or_Keyword_Example_VBNET.htm)

## Remarks

ShowRubberLine must be set to true for the values specified for BasePoint to have an effect. The rubber band stretches from the BasePoint (or origin) to the location of the cursor in the drawing.

Keywords are context-sensitive options that are available in the Options toolbar when executing a command. Keywords in LocalKeywordStrArray are displayed in the prompt in the command window during user interaction. Keywords in GlobalKeywordStrArray are not displayed in the prompt in the command window. However, users can type global keywords in the prompt in the command window if they know them.

If the PromptInit parameter is set to:

- dsPromptInit_e.dsPromptInit_NoDefault and a value is specified for DefaultValue, then the value is not used or displayed in the prompt in the command window.
- dsPromptInit_e.UsePromptExplanation, then call [ICommandMessage::PromptExplanation](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptExplanation.html) to specify the text for PromptInit.

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForKeyword2 Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForKeyword2.html)

## Availability

DraftSight 2020 SP3
