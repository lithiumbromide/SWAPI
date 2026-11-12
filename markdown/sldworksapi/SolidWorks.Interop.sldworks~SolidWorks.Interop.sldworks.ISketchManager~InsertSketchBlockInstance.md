---
title: "InsertSketchBlockInstance Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "InsertSketchBlockInstance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchBlockInstance.html"
---

# InsertSketchBlockInstance Method (ISketchManager)

Inserts a block instance at the specified location using the block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSketchBlockInstance( _
   ByVal BlockDef As SketchBlockDefinition, _
   ByVal Position As MathPoint, _
   ByVal Scale As System.Double, _
   ByVal Angle As System.Double _
) As SketchBlockInstance
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim BlockDef As SketchBlockDefinition
Dim Position As MathPoint
Dim Scale As System.Double
Dim Angle As System.Double
Dim value As SketchBlockInstance

value = instance.InsertSketchBlockInstance(BlockDef, Position, Scale, Angle)
```

### C#

```csharp
SketchBlockInstance InsertSketchBlockInstance(
   SketchBlockDefinition BlockDef,
   MathPoint Position,
   System.double Scale,
   System.double Angle
)
```

### C++/CLI

```cpp
SketchBlockInstance^ InsertSketchBlockInstance(
   SketchBlockDefinition^ BlockDef,
   MathPoint^ Position,
   System.double Scale,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BlockDef`: [Block](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition.html) for this block instance
- `Position`: [Position](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of this block instance
- `Scale`: Scale for this block instance
- `Angle`: Rotation angle for this block instance

### Return Value

[Block instance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance.html)

## VBA Syntax

See [SketchManager::InsertSketchBlockInstance](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~InsertSketchBlockInstance.html).

## Examples

[Create Block Definition and Insert Block Instance (VBA)](Create_Block_Definition_and_Insert_Block_Instance_Example_VB.htm)
[Create Block Definition and Insert Block Instance (C#)](Create_Block_Definition_and_Insert_Block_Instance_Example_CSharp.htm)
[Create Block Definition and Insert Block Instance (VB.NET)](Create_Block_Definition_and_Insert_Block_Instance_Example_VBNET.htm)

## Remarks

This method creates a block definition if the block definition does not exist.

- or -

If the definition exists, then this method uses that block definition to create the block instance. The name of the block instance is the same as the filename of the block file, without the filename extension.

If the entities of a block are associated with one or more layers and those layers do not already exist in the drawing, then the layers are inserted in the drawing and the associations between the entities of the block and the layers are maintained.

The block instance is inserted on the current drawing layer.

**TIP:** If inserting the same sketch block multiple times, do not create the block definition more than once. Instead, use the same block definition for each call to SketchManager::InsertSketchBlockInstance.

To save a block instance and its definition into a block file (**.sldblk**), use [ISketchBlockDefinition::Save](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~Save.html).

This method does not work for drawings opened in view-only mode.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
