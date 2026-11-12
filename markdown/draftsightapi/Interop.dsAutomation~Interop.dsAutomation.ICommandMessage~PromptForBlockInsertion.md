---
title: "PromptForBlockInsertion Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForBlockInsertion"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForBlockInsertion.html"
---

# PromptForBlockInsertion Method (ICommandMessage)

Prompts the user for the insertion point, scale factors, and rotation angle to use when inserting a [Block Instance](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html).

## Syntax

### Visual Basic

```vb
Function PromptForBlockInsertion( _
   ByVal PreviewBlockName As System.String, _
   ByVal SpecifyScale As System.Boolean, _
   ByVal DefaultScaleX As System.Double, _
   ByVal DefaultScaleY As System.Double, _
   ByVal DefaultScaleZ As System.Double, _
   ByVal SpecifyRotation As System.Boolean, _
   ByVal DefaultRotation As System.Double, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double, _
   ByRef ScaleX As System.Double, _
   ByRef ScaleY As System.Double, _
   ByRef ScaleZ As System.Double, _
   ByRef Rotation As System.Double _
) As dsPromptResultType_e
```

### C#

```csharp
dsPromptResultType_e PromptForBlockInsertion(
   System.string PreviewBlockName,
   System.bool SpecifyScale,
   System.double DefaultScaleX,
   System.double DefaultScaleY,
   System.double DefaultScaleZ,
   System.bool SpecifyRotation,
   System.double DefaultRotation,
   out System.double X,
   out System.double Y,
   out System.double Z,
   out System.double ScaleX,
   out System.double ScaleY,
   out System.double ScaleZ,
   out System.double Rotation
)
```

### JScript

```
function PromptForBlockInsertion(
   PreviewBlockName : System.String,
   SpecifyScale : System.boolean,
   DefaultScaleX : System.double,
   DefaultScaleY : System.double,
   DefaultScaleZ : System.double,
   SpecifyRotation : System.boolean,
   DefaultRotation : System.double,
   X : System.double,
   Y : System.double,
   Z : System.double,
   ScaleX : System.double,
   ScaleY : System.double,
   ScaleZ : System.double,
   Rotation : System.double
) : dsPromptResultType_e;
```

### Managed Extensions for C++

```
dsPromptResultType_e PromptForBlockInsertion(
   System.string* PreviewBlockName,
   System.bool SpecifyScale,
   System.double DefaultScaleX,
   System.double DefaultScaleY,
   System.double DefaultScaleZ,
   System.bool SpecifyRotation,
   System.double DefaultRotation,
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z,
   [PARAMFLAG::Out] System.double ScaleX,
   [PARAMFLAG::Out] System.double ScaleY,
   [PARAMFLAG::Out] System.double ScaleZ,
   [PARAMFLAG::Out] System.double Rotation
)
```

### C++/CLI

```cpp
dsPromptResultType_e PromptForBlockInsertion(
   System.String^ PreviewBlockName,
   System.bool SpecifyScale,
   System.double DefaultScaleX,
   System.double DefaultScaleY,
   System.double DefaultScaleZ,
   System.bool SpecifyRotation,
   System.double DefaultRotation,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double ScaleX,
   [Out] System.double ScaleY,
   [Out] System.double ScaleZ,
   [Out] System.double Rotation
)
```

### Parameters

- `PreviewBlockName`: Name of the Block definition to insert to create the Block instance
- `SpecifyScale`: True to use the values specified for DefaultScaleX, DefaultScaleY, and DefaultScaleZ for the Block instance's scale factors, false to use the user-interactive values (see **Remarks**)
- `DefaultScaleX`: Scale factor for the x axis for the Block instance if SpecifyScale is set to true (see **Remarks**)
- `DefaultScaleY`: Scale factor for the y axis for the Block instance if SpecifyScale is set to true (see **Remarks**)
- `DefaultScaleZ`: Scale factor for the z axis for the Block instance if SpecifyScale is set to true (see **Remarks**)
- `SpecifyRotation`: True to use the value specified for DefaultRotation for the Block instance's rotation angle, false to use the user-interactive value (see **Remarks**)
- `DefaultRotation`: Angle, in radians, by which to rotate the Block instance if SpecifyRotation is set to true (see **Remarks**)
- `X`: x coordinate where to insert the Block instance
- `Y`: y coordinate where to insert the Block instance
- `Z`: z coordinate where to insert the Block instance
- `ScaleX`: Scale factor for the x axis of the Block instance
- `ScaleY`: Scale factor for the y axis of the Block instance
- `ScaleZ`: Scale factor for the z axis of the Block instance
- `Rotation`: Angle, in radians, by which to rotate the Block instance

### Return Value

Status of the input for inserting the Block instance as defined in [dsPromptResultType_e](Interop.dsAutomation~Interop.dsAutomation.dsPromptResultType_e.html)

## Examples

[Prompt for Block Insertion (JavaScript)](Prompt_for_Block_Insertion_Example_JS.htm)

## Remarks

| If this parameter... | Is set to... | Then... |
| --- | --- | --- |
| SpecifyScale | True | The DefaultScaleX, DefaultScaleY, and DefaultScaleZ values are used to scale the Block instance when the user presses the Enter key when prompted for these values in the command window. |
|  | False | Either the values typed in the command window, or the coordinates that correspond to the point where the user clicks in the graphics area, are used to scale the Block instance. |
| SpecifyRotation | True | The DefaultRotation value is used for the rotation angle of the Block instance when the user presses the Enter key when prompted for this value in the command window. |
|  | False | Either the value typed in the command window, or the angle that corresponds to the point where the user clicks in the graphics area, is used for the rotation angle of the Block instance. |

**NOTE**: A positive value for the rotation angle rotates the Block instance counterclockwise, and a negative value rotates the Block instance clockwise.

Typical use of this method involves:

1. Defining the Block definition using [IDocument::CreateBlockDefinition](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateBlockDefinition.html), if needed. If a Block definition already exists, skip this step.
2. Defining how to insert the Block using ICommandMessage::PromptForBlockInsertion.
3. Inserting the Block using [ISketchManager::InsertBlock2](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertBlock2.html) and the output values of ICommandMessage::PromptForBlockInsertion.

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)

## Availability

DraftSight V1R3.1
