---
title: "PromptForPointOrKeyword Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForPointOrKeyword"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForPointOrKeyword.html"
---

# PromptForPointOrKeyword Method (ICommandMessage)

Displays the specified prompt, local keywords, and default value for the point in the command window and gets the user's input.

## Syntax

### Visual Basic

```vb
Function PromptForPointOrKeyword( _
   ByVal Prompt As System.String, _
   ByVal ErrorMsg As System.String, _
   ByVal GlobalKeywordStrArray As System.Object, _
   ByVal LocalKeywordStrArray As System.Object, _
   ByVal PromptInit As System.Integer, _
   ByVal ShowRubberLine As System.Boolean, _
   ByVal DefaultValue As MathPoint, _
   ByVal BasePoint As MathPoint, _
   ByRef Keyword As System.String, _
   ByRef ResultPoint As MathPoint, _
   ByVal Plane As MathPlane _
) As dsPromptResultType_e
```

### C#

```csharp
dsPromptResultType_e PromptForPointOrKeyword(
   System.string Prompt,
   System.string ErrorMsg,
   System.object GlobalKeywordStrArray,
   System.object LocalKeywordStrArray,
   System.int PromptInit,
   System.bool ShowRubberLine,
   MathPoint DefaultValue,
   MathPoint BasePoint,
   out System.string Keyword,
   out MathPoint ResultPoint,
   MathPlane Plane
)
```

### JScript

```
function PromptForPointOrKeyword(
   Prompt : System.String,
   ErrorMsg : System.String,
   GlobalKeywordStrArray : System.Object,
   LocalKeywordStrArray : System.Object,
   PromptInit : System.int,
   ShowRubberLine : System.boolean,
   DefaultValue : MathPoint,
   BasePoint : MathPoint,
   Keyword : System.String,
   ResultPoint : MathPoint,
   Plane : MathPlane
) : dsPromptResultType_e;
```

### Managed Extensions for C++

```
dsPromptResultType_e PromptForPointOrKeyword(
   System.string* Prompt,
   System.string* ErrorMsg,
   System.Object* GlobalKeywordStrArray,
   System.Object* LocalKeywordStrArray,
   System.int PromptInit,
   System.bool ShowRubberLine,
   MathPoint* DefaultValue,
   MathPoint* BasePoint,
   [PARAMFLAG::Out] System.string* Keyword,
   [PARAMFLAG::Out] MathPoint* ResultPoint,
   MathPlane* Plane
)
```

### C++/CLI

```cpp
dsPromptResultType_e PromptForPointOrKeyword(
   System.String^ Prompt,
   System.String^ ErrorMsg,
   System.Object^ GlobalKeywordStrArray,
   System.Object^ LocalKeywordStrArray,
   System.int PromptInit,
   System.bool ShowRubberLine,
   MathPoint^ DefaultValue,
   MathPoint^ BasePoint,
   [Out] System.String^ Keyword,
   [Out] MathPoint^ ResultPoint,
   MathPlane^ Plane
)
```

### Parameters

- `Prompt`: Text for the prompt to display in the command window
- `ErrorMsg`: Error message to display in the command window if the user input is invalid
- `GlobalKeywordStrArray`: Array of global keywords, which typically are language independent (see **Remarks**)
- `LocalKeywordStrArray`: Array of local keywords, which are typically translated to the local language (see **Remarks**)
- `PromptInit`: Prompt initialization as defined in [dsPromptInit_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptInit_e.html) (see **Remarks**)
- `ShowRubberLine`: True to display a rubber line from the origin, or from the BasePoint, to the location of the cursor; false to not display the rubber line (see **Remarks**)
- `DefaultValue`: Default value for the point in the prompt in the command window (see **Remarks**)
- `BasePoint`: [Base point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `Keyword`: Keyword input by user
- `ResultPoint`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) input by user
- `Plane`: Projection [plane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html) cursor coordinates

### Return Value

Result as defined in [dsPromptResultType_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptResultType_e.html)

## Remarks

ShowRubberLine must be set to true for the values specified for BasePoint to have an effect. The rubber line extends to the location of the cursor in the drawing.

Keywords are context-sensitive options that are available in the Options toolbar when executing a command. Local keywords can be seen in the prompt in the command window during user interaction. Global keywords cannot be seen in the prompt in the command window. However, users can type global keywords at the prompt in the command window if they know them.

If the PromptInit parameter is set to:

- dsPromptInit_e.dsPromptInit_NoDefault and a value is specified for DefaultValue, then the value is not used or displayed in the prompt in the command window.
- dsPromptInit_e.UsePromptExplanation, then call [ICommandMessage::PromptExplanation](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptExplanation.html) to specify the text for PromptInit.

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForPoint2 Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForPoint2.html)

## Availability

DraftSight V1R4.0
