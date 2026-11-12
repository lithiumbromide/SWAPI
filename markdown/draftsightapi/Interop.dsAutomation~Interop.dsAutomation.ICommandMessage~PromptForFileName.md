---
title: "PromptForFileName Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForFileName"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForFileName.html"
---

# PromptForFileName Method (ICommandMessage)

Displays the specified prompt in the command window and gets the file name input by the user.

## Syntax

### Visual Basic

```vb
Function PromptForFileName( _
   ByVal Prompt As System.String, _
   ByRef FileName As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool PromptForFileName(
   System.string Prompt,
   out System.string FileName
)
```

### JScript

```
function PromptForFileName(
   Prompt : System.String,
   FileName : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PromptForFileName(
   System.string* Prompt,
   [PARAMFLAG::Out] System.string* FileName
)
```

### C++/CLI

```cpp
System.bool PromptForFileName(
   System.String^ Prompt,
   [Out] System.String^ FileName
)
```

### Parameters

- `Prompt`: Text of prompt to display in the command window
- `FileName`: Document's path and file name

### Return Value

True if the prompt is displayed in the command window and a document's path and file name are returned, false if not

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForFileNameOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForFileNameOrKeyword.html)

## Availability

DraftSight V1R2.0
