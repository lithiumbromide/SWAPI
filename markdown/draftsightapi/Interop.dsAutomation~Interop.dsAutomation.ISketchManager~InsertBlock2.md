---
title: "InsertBlock2 Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertBlock2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertBlock2.html"
---

# InsertBlock2 Method (ISketchManager)

Inserts a Block instance.

## Syntax

### Visual Basic

```vb
Function InsertBlock2( _
   ByVal BlockName As System.String, _
   ByVal InsertX As System.Double, _
   ByVal InsertY As System.Double, _
   ByVal InsertZ As System.Double, _
   ByVal ScaleX As System.Double, _
   ByVal ScaleY As System.Double, _
   ByVal ScaleZ As System.Double, _
   ByVal Rotation As System.Double _
) As BlockInstance
```

### C#

```csharp
BlockInstance InsertBlock2(
   System.string BlockName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double ScaleX,
   System.double ScaleY,
   System.double ScaleZ,
   System.double Rotation
)
```

### JScript

```
function InsertBlock2(
   BlockName : System.String,
   InsertX : System.double,
   InsertY : System.double,
   InsertZ : System.double,
   ScaleX : System.double,
   ScaleY : System.double,
   ScaleZ : System.double,
   Rotation : System.double
) : BlockInstance;
```

### Managed Extensions for C++

```
BlockInstance* InsertBlock2(
   System.string* BlockName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double ScaleX,
   System.double ScaleY,
   System.double ScaleZ,
   System.double Rotation
)
```

### C++/CLI

```cpp
BlockInstance^ InsertBlock2(
   System.String^ BlockName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double ScaleX,
   System.double ScaleY,
   System.double ScaleZ,
   System.double Rotation
)
```

### Parameters

- `BlockName`: Name for the Block instance
- `InsertX`: x coordinate where to insert the Block instance
- `InsertY`: y coordinate where to insert the Block instance
- `InsertZ`: z coordinate where to insert the Block instance
- `ScaleX`: Scale factor for the x axis
- `ScaleY`: Scale factor for the y axis
- `ScaleZ`: Scale factor for the z axis
- `Rotation`: Angle, in radians, by which to rotate the Block instance (see **Remarks**)

### Return Value

[Block instance](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)

## Examples

This code snippet shows how to insert a Block instance.

##### COM native C++

//Insert the existing Block instance or insert Block instance from a DWG file

bstr_t blockFileName ( L"<`path_and_DWG_file_name_OR_existing_Block_name`>" );

double insertX = 0, insertY = 0, insertZ = 0, scaleX = 1, scaleY = 1, scaleZ = 1, rotation = 0;

BlockInstancePtr blockInstance = sketchMgr->InsertBlock2( blockFileName, insertX, insertY, insertZ, scaleX, scaleY, scaleZ, rotation );

## Examples

[Insert Block Instance (C#)](Insert_Block_Instance_Example_CSharp.htm)
[Insert Block Instance (VB.NET)](Insert_Block_Instance_Example_VBNET.htm)
[Insert Block Instance (VBA)](Insert_Block_Instance_Example_VBA.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)

## Remarks

Before calling this method, you can call [ICommandMessage::PromptForBlockInsertion](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForBlockInsertion.html) if you want to prompt the user to specify how to insert the Block instance.

Use a positive value for Rotation to rotate the Block instance counterclockwise and a negative value to rotate the Block instance clockwise.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R2.1
