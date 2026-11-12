---
title: "PromptForPoint Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForPoint.html"
---

# PromptForPoint Method (ICommandMessage)

Obsolete. Superseded by [ICommandMessage::PromptForPoint2](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForPoint2.html).

## Syntax

### Visual Basic

```vb
Function PromptForPoint( _
   ByVal Prompt As System.String, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool PromptForPoint(
   System.string Prompt,
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function PromptForPoint(
   Prompt : System.String,
   X : System.double,
   Y : System.double,
   Z : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PromptForPoint(
   System.string* Prompt,
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
System.bool PromptForPoint(
   System.String^ Prompt,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `Prompt`: Text of prompt
- `X`: x coordinate of a point
- `Y`: y coordinate of a point
- `Z`: z coordinate of a point

### Return Value

True if the prompt is displayed in the command window, false if not

## Examples

[Insert Lines and Angular Dimension (JavaScript)](Insert_Lines_and_Angular_Dimension_Example_JS.htm)
[Create Circles on Different Layers (JavaScript)](Create_Circles_on_Different_Layers_Example_JS.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)
[Insert Splines (JavaScript)](Insert_Splines_Example_JS.htm)
[Insert HyperLink (JavaScript)](Insert_HyperLink_Example_JS.htm)
[Insert and Dimension Sketch (JavaScript)](Insert_and_Dimension_Sketch_Example_JS.htm)
[Mirror Entities (JavaScript)](Mirror_Entities_Example_JS.htm)
[Insert Hatch by Entities or Internal Points (C#)](Insert_Hatch_by_Entities_or_Internal_Points_CSharp.htm)
[Insert Hatch by Entities or Internal Points (VB.NET)](Insert_Hatch_by_Entities_or_Internal_Points_Example_VBNET.htm)
[Insert Hatch by Entities or Internal Points (VBA)](Insert_Hatch_by_Entities_or_Internal_Points_Example_VBA.htm)

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)

## Availability

DraftSight V1R1.1
