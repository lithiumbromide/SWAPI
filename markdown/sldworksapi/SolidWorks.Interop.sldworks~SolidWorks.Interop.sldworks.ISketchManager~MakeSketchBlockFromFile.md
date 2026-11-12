---
title: "MakeSketchBlockFromFile Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "MakeSketchBlockFromFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.html"
---

# MakeSketchBlockFromFile Method (ISketchManager)

Creates a block definition using the specified file.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeSketchBlockFromFile( _
   ByVal InsertionPoint As MathPoint, _
   ByVal FileName As System.String, _
   ByVal LinkedToFile As System.Boolean, _
   ByVal Scale As System.Double, _
   ByVal Angle As System.Double _
) As SketchBlockDefinition
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim InsertionPoint As MathPoint
Dim FileName As System.String
Dim LinkedToFile As System.Boolean
Dim Scale As System.Double
Dim Angle As System.Double
Dim value As SketchBlockDefinition

value = instance.MakeSketchBlockFromFile(InsertionPoint, FileName, LinkedToFile, Scale, Angle)
```

### C#

```csharp
SketchBlockDefinition MakeSketchBlockFromFile(
   MathPoint InsertionPoint,
   System.string FileName,
   System.bool LinkedToFile,
   System.double Scale,
   System.double Angle
)
```

### C++/CLI

```cpp
SketchBlockDefinition^ MakeSketchBlockFromFile(
   MathPoint^ InsertionPoint,
   System.String^ FileName,
   System.bool LinkedToFile,
   System.double Scale,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InsertionPoint`: [Insertion point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html), which is a 2D point with z = 0.0, for the block definition
- `FileName`: Name of the external file to use to create the block definition
- `LinkedToFile`: True to link the block definition to the file, false to not
- `Scale`: Scale for the block definition
- `Angle`: Rotation angle for the block definition

### Return Value

[Block definition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.html)

## VBA Syntax

See [SketchManager::MakeSketchBlockFromFile](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~MakeSketchBlockFromFile.html).

## Remarks

If the entities of a block are associated with one or more layers and those layers do not already exist in the drawing, then the layers are inserted in the drawing and the associations between the entities of the block and the layers are maintained.

The block instance is inserted on the current drawing layer.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::MakeSketchBlockFromSelected Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.html)
[ISketchManager::MakeSketchBlockFromSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.html)
[ISketchBlockDefinition::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~FileName.html)
[ISketchBlockDefinition::LinkToFile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~LinkToFile.html)
[ISketchBlockDefinition::Save Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~Save.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
