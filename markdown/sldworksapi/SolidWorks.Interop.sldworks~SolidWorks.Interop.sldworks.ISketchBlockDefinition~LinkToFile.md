---
title: "LinkToFile Property (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "LinkToFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~LinkToFile.html"
---

# LinkToFile Property (ISketchBlockDefinition)

Gets or sets whether the block definition file is linked to a file.

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkToFile As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.Boolean

instance.LinkToFile = value

value = instance.LinkToFile
```

### C#

```csharp
System.bool LinkToFile {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkToFile {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the block definition is linked to a file, false if not

## VBA Syntax

See [SketchBlockDefinition::LinkToFile](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~LinkToFile.html).

## Examples

[Get and Set Blocks in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)
[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)

## Remarks

The file can be either a native SOLIDWORKS block file (.sldblk) or a non-native SOLIDWORKS file (.dxf or .dwg).

This property indicates whether the block definition is linked to an external file, which you can enable or disable on the block definition without destroying the file name. That is, the file name continues to be stored even if the link is disabled.

Use [ISketchBlockDefinition::FileName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~FileName.html) to get the name of the file to which a block definition is linked.

You can link a block definition to a .sldblk file. However, you cannot save a block definition to a .sldblk file by only calling SketchBlockDefinition::FileName (True) and SketchBlockDefinition::LinkToFile (Filename). You must first either save the block by selecting it and calling [ISketchBlockDefinition::Save](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~Save.html), or you can assign the block to an already existing .sldblk file.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::MakeSketchBlockFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.html)
[ISketchBlockDefinition::MakeSketchBlockFromSelected Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.html)
[ISketchBlockDefinition::MakeSketchBlockFromSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
