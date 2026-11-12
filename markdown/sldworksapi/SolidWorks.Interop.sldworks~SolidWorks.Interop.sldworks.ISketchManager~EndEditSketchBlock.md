---
title: "EndEditSketchBlock Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "EndEditSketchBlock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EndEditSketchBlock.html"
---

# EndEditSketchBlock Method (ISketchManager)

Saves or discards your edits of the block and then ends the current editing session of this block.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EndEditSketchBlock( _
   ByVal AcceptChanges As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim AcceptChanges As System.Boolean

instance.EndEditSketchBlock(AcceptChanges)
```

### C#

```csharp
void EndEditSketchBlock(
   System.bool AcceptChanges
)
```

### C++/CLI

```cpp
void EndEditSketchBlock(
   System.bool AcceptChanges
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AcceptChanges`: True to save your edits, false to discard them

## VBA Syntax

See [SketchManager::EndEditSketchBlock](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~EndEditSketchBlock.html).

## Remarks

Use [ISketchManager::EditSketchBlock](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~EditSketchBlock.html) to put the block in edit mode.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
