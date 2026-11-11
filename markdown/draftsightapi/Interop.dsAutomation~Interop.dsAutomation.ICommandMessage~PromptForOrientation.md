---
title: "PromptForOrientation Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForOrientation"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForOrientation.html"
---

# PromptForOrientation Method (ICommandMessage)

Displays the specified prompt and default value for the orientation in the command window and gets the orientation input by the user.

## Syntax

### Visual Basic

```vb
Function PromptForOrientation( _
   ByVal Prompt As System.String, _
   ByVal DefaultValue As System.Double, _
   ByRef Value As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool PromptForOrientation(
   System.string Prompt,
   System.double DefaultValue,
   out System.double Value
)
```

### JScript

```
function PromptForOrientation(
   Prompt : System.String,
   DefaultValue : System.double,
   Value : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PromptForOrientation(
   System.string* Prompt,
   System.double DefaultValue,
   [PARAMFLAG::Out] System.double Value
)
```

### C++/CLI

```cpp
System.bool PromptForOrientation(
   System.String^ Prompt,
   System.double DefaultValue,
   [Out] System.double Value
)
```

### Parameters

- `Prompt`: Text to display as the prompt in the command window
- `DefaultValue`: Default orientation value
- `Value`: Orientation value

### Return Value

True if the prompt is displayed in the command window, false if not

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForOrientationOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForOrientationOrKeyword.html)

## Availability

DraftSight V1R1.4
