---
title: "EditSketchBlock Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "EditSketchBlock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditSketchBlock.html"
---

# EditSketchBlock Method (ISketchManager)

Puts the block definition in edit mode.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditSketchBlock()
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager

instance.EditSketchBlock()
```

### C#

```csharp
void EditSketchBlock()
```

### C++/CLI

```cpp
void EditSketchBlock();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SketchManager::EditSketchBlock](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~EditSketchBlock.html).

## Remarks

When done editing the block definition, use [ISketchManager::EndEditSketchBlock](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~EndEditSketchBlock.html).

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
