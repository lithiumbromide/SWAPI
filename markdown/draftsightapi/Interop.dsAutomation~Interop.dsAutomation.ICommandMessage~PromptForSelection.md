---
title: "PromptForSelection Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForSelection"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForSelection.html"
---

# PromptForSelection Method (ICommandMessage)

Displays the specified prompt for selecting one or more entities.

## Syntax

### Visual Basic

```vb
Function PromptForSelection( _
   ByVal SingleSelection As System.Boolean, _
   ByVal Prompt As System.String, _
   ByVal ErrorMsg As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool PromptForSelection(
   System.bool SingleSelection,
   System.string Prompt,
   System.string ErrorMsg
)
```

### JScript

```
function PromptForSelection(
   SingleSelection : System.boolean,
   Prompt : System.String,
   ErrorMsg : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PromptForSelection(
   System.bool SingleSelection,
   System.string* Prompt,
   System.string* ErrorMsg
)
```

### C++/CLI

```cpp
System.bool PromptForSelection(
   System.bool SingleSelection,
   System.String^ Prompt,
   System.String^ ErrorMsg
)
```

### Parameters

- `SingleSelection`: True to prompt for a single selection, false to prompt for multiple selections
- `Prompt`: Prompt to display in the command window
- `ErrorMsg`: Error message to display in the command window when the user's input is invalid

### Return Value

True if the prompt is displayed in the command window, false if not

## Examples

[Get Hatch and Hatch Boundary Loop Data (C#)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_CSharp.htm)
[Get Hatch and Hatch Boundary Loop Data (VB.NET)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBNET.htm)
[Get Hatch and Hatch Boundary Loop Data (VBA)](Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBA.htm)
[Rotate and Copy Entities (C#)](Rotate_and_Copy_Entities_Example_CSharp.htm)
[Rotate and Copy Entities (VB.NET)](Rotate_and_Copy_Entities_Example_VBNET.htm)
[Rotate and Copy Entities (VBA)](Rotate_and_Copy_Entities_Example_VBA.htm)
[Insert Hatch (JavaScript)](Insert_Hatch_Example_JS.htm)
[Insert Hatch by Entities or Internal Points (VB.NET)](Insert_Hatch_by_Entities_or_Internal_Points_Example_VBNET.htm)
[Insert Hatch by Entities or Internal Points (C#)](Insert_Hatch_by_Entities_or_Internal_Points_CSharp.htm)
[Insert Hatch by Entities or Internal Points (VBA)](Insert_Hatch_by_Entities_or_Internal_Points_Example_VBA.htm)

## Remarks

You can allow or disallow the selection of an entity by calling [ISelectionManager::RemoveOptions](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~RemoveOptions.html) before calling this method.

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForSelectionOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForSelectionOrKeyword.html)
[ISelectionManager::PaperSpaceSelectionEnabled Property ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~PaperSpaceSelectionEnabled.html)
[ISelectionManager::RemoveOptions Property ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~RemoveOptions.html)

## Availability

DraftSight V1R1.1
