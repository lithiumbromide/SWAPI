---
title: "MakeSketchBlockFromSketch Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "MakeSketchBlockFromSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.html"
---

# MakeSketchBlockFromSketch Method (ISketchManager)

Creates a block definition at the specified location using all of the sketch entities in the active sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeSketchBlockFromSketch( _
   ByVal InsertionPoint As MathPoint, _
   ByVal Sketch As Sketch _
) As SketchBlockDefinition
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim InsertionPoint As MathPoint
Dim Sketch As Sketch
Dim value As SketchBlockDefinition

value = instance.MakeSketchBlockFromSketch(InsertionPoint, Sketch)
```

### C#

```csharp
SketchBlockDefinition MakeSketchBlockFromSketch(
   MathPoint InsertionPoint,
   Sketch Sketch
)
```

### C++/CLI

```cpp
SketchBlockDefinition^ MakeSketchBlockFromSketch(
   MathPoint^ InsertionPoint,
   Sketch^ Sketch
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InsertionPoint`: [Insertion point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html), which is a 2D point with z = 0.0, for the block definition
- `Sketch`: [Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html) to use

### Return Value

[Block definition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition.html)

## VBA Syntax

See [SketchManager::MakeSketchBlockFromSketch](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~MakeSketchBlockFromSketch.html).

## Remarks

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::MakeSketchBlockFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.html)
[ISketchManager::MakeSketchBlockFromSelected Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
