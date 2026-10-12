---
title: "ISketchBlockInstance Interface"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html"
---

# ISketchBlockInstance Interface

Allows access to block instances.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISketchBlockInstance
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
```

### C#

```csharp
public interface ISketchBlockInstance
```

### C++/CLI

```cpp
public interface class ISketchBlockInstance
```

## VBA Syntax

See [SketchBlockInstance](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance.html).

## Examples

[Get and Set Blocks Data in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)
[Get Block Instance in Part or Assembly (VBA)](Get_Block_Instance_in_Part_or_Assembly_Example_VB.htm)
[Get Blocks in Drawing (VBA)](Get_Blocks_in_Drawing_Example_VB.htm)
[Create Block Definition and Insert Block Instance (C#)](Create_Block_Definition_and_Insert_Block_Instance_Example_CSharp.htm)
[Create Block Definition and Insert Block Instance (VBA)](Create_Block_Definition_and_Insert_Block_Instance_Example_VB.htm)
[Create Block Definition and Insert Block Instance (VB.NET)](Create_Block_Definition_and_Insert_Block_Instance_Example_VBNET.htm)

## Remarks

Using this interface, you can:

- get the block instance's [block definition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition.html)
- get the sketch in which the block instance is present
- Get or set the block instance's:

  - Angle
  - Attributes (notes that have tag names and that are not read-only)
  - Layer
  - Leader styles
  - Name
  - Position
  - Scale
  - Text display state
- Get block instances on a drawing sheet format and edit the sheet format using [IDrawingDoc::EditTempate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditTemplate.html) and [IModelDoc2::GetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetActiveSketch2.html) or [IModelDoc2::IGetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetActiveSketch2.html), which gains access to the [sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html) that contains the block instances.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## Accessors

[ILayer::GetItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~GetItems.html)

[ISketch::GetSketchBlockInstances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchBlockInstances.html) and [ISketch::IGetSketchBlockInstances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchBlockInstances.html)

[ISketchBlockDefinition::GetInstances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetInstances.html) and [ISketchBlockDefinition::IGetInstances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetInstances.html)

[ISketchManager::ExplodeSketchBlockInstance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~ExplodeSketchBlockInstance.html)

[ISketchManager::InsertSketchBlockInstance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketchBlockInstance.html)

## Access Diagram

[SketchBlockInstance](SWObjectModel.pdf#SketchBlockInstance)

## See Also

[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
