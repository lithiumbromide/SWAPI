---
title: "PromptExplanation Property (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptExplanation"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptExplanation.html"
---

# PromptExplanation Property (ICommandMessage)

Gets or sets the text for the prompt in the command window.

## Syntax

### Visual Basic

```vb
Property PromptExplanation As System.String
```

### C#

```csharp
System.string PromptExplanation {get; set;}
```

### JScript

```
function get,set PromptExplanation : System.String
```

### Managed Extensions for C++

```
__property System.string* get_PromptExplanation();
__property void set_PromptExplanation(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ PromptExplanation {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Text for the prompt in the command window

## Remarks

If any method on the ICommandMessage interface (see the **See Also** list) has its PromptInit parameter set to [dsPromptInit_e.UsePromptExplanation](Interop.dsAutomation~Interop.dsAutomation.dsPromptInit_e.html), then the text specified by this property is used for that prompt in the command window.

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForAngleOrKeyword2 Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForAngleOrKeyword2.html)
[ICommandMessage::PromptForBoolOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForBoolOrKeyword.html)
[ICommandMessage::PromptForDistanceOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForDistanceOrKeyword.html)
[ICommandMessage::PromptForDoubleOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForDoubleOrKeyword.html)
[ICommandMessage::PromptForFileNameOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForFileNameOrKeyword.html)
[ICommandMessage::PromptForIntegerOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForIntegerOrKeyword.html)
[ICommandMessage::PromptForKeyword2 Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForKeyword2.html)
[ICommandMessage::PromptForOrientationOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForOrientationOrKeyword.html)
[ICommandMessage::PromptForPointOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForPointOrKeyword.html)
[ICommandMessage::PromptForSelectionOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForSelectionOrKeyword.html)
[ICommandMessage::PromptForStringOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForStringOrKeyword.html)

## Availability

DraftSight V1R5.0
