---
title: "MakeSketchBlockFromSelected Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "MakeSketchBlockFromSelected"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.html"
---

# MakeSketchBlockFromSelected Method (ISketchManager)

Creates a block definition at the specified location from the selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeSketchBlockFromSelected( _
   ByVal InsertionPoint As MathPoint _
) As SketchBlockDefinition
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim InsertionPoint As MathPoint
Dim value As SketchBlockDefinition

value = instance.MakeSketchBlockFromSelected(InsertionPoint)
```

### C#

```csharp
SketchBlockDefinition MakeSketchBlockFromSelected(
   MathPoint InsertionPoint
)
```

### C++/CLI

```cpp
SketchBlockDefinition^ MakeSketchBlockFromSelected(
   MathPoint^ InsertionPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InsertionPoint`: [Insertion point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html), which is a 2D point with z = 0.0, for the block definition

### Return Value

[Block definition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition.html)

## VBA Syntax

See [SketchManager::MakeSketchBlockFromSelected](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~MakeSketchBlockFromSelected.html).

## Examples

[Create Block Definition and Insert Block Instance (VBA)](Create_Block_Definition_and_Insert_Block_Instance_Example_VB.htm)
[Create Block Definition and Insert Block Instance (C#)](Create_Block_Definition_and_Insert_Block_Instance_Example_CSharp.htm)
[Create Block Definition and Insert Block Instance (VB.NET)](Create_Block_Definition_and_Insert_Block_Instance_Example_VBNET.htm)

## Remarks

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::MakeSketchBlockFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.html)
[ISketchManager::MakeSketchBlockFromSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
