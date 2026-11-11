---
title: "PromptForKeyword Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForKeyword"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForKeyword.html"
---

# PromptForKeyword Method (ICommandMessage)

Obsoleted. Superseded by [ICommandMessage::PromptForKeyword2](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForKeyword2.html).

## Syntax

### Visual Basic

```vb
Function PromptForKeyword( _
   ByVal Prompt As System.String, _
   ByVal KeywordsStrArray As System.Object, _
   ByVal DefaultValue As System.String, _
   ByRef Value As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool PromptForKeyword(
   System.string Prompt,
   System.object KeywordsStrArray,
   System.string DefaultValue,
   out System.string Value
)
```

### JScript

```
function PromptForKeyword(
   Prompt : System.String,
   KeywordsStrArray : System.Object,
   DefaultValue : System.String,
   Value : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PromptForKeyword(
   System.string* Prompt,
   System.Object* KeywordsStrArray,
   System.string* DefaultValue,
   [PARAMFLAG::Out] System.string* Value
)
```

### C++/CLI

```cpp
System.bool PromptForKeyword(
   System.String^ Prompt,
   System.Object^ KeywordsStrArray,
   System.String^ DefaultValue,
   [Out] System.String^ Value
)
```

### Parameters

- `Prompt`: Text of prompt to display in the command window
- `KeywordsStrArray`: Array of keywords
- `DefaultValue`: Default string value
- `Value`: Keyword string

### Return Value

True if the prompt is displayed in the command window, false if not

## Examples

[Insert Hatch by Entities or Internal Points (VB.NET)](Insert_Hatch_by_Entities_or_Internal_Points_Example_VBNET.htm)
[Insert Hatch by Entities or Internal Points (C#)](Insert_Hatch_by_Entities_or_Internal_Points_CSharp.htm)

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)

## Availability

DraftSight V1R1.4
