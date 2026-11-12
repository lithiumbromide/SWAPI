---
title: "SketchOffset2 Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "SketchOffset2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset2.html"
---

# SketchOffset2 Method (ISketchManager)

Offsets the selected sketch entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchOffset2( _
   ByVal Offset As System.Double, _
   ByVal BothDirections As System.Boolean, _
   ByVal Chain As System.Boolean, _
   ByVal CapEnds As System.Integer, _
   ByVal MakeConstruction As System.Integer, _
   ByVal AddDimensions As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim Offset As System.Double
Dim BothDirections As System.Boolean
Dim Chain As System.Boolean
Dim CapEnds As System.Integer
Dim MakeConstruction As System.Integer
Dim AddDimensions As System.Boolean
Dim value As System.Boolean

value = instance.SketchOffset2(Offset, BothDirections, Chain, CapEnds, MakeConstruction, AddDimensions)
```

### C#

```csharp
System.bool SketchOffset2(
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain,
   System.int CapEnds,
   System.int MakeConstruction,
   System.bool AddDimensions
)
```

### C++/CLI

```cpp
System.bool SketchOffset2(
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain,
   System.int CapEnds,
   System.int MakeConstruction,
   System.bool AddDimensions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Offset`: Offset value; negative value offsets the sketch entities in the opposite direction
- `BothDirections`: True to offset the sketch entities in both directions, false to offset the sketch entities in one direction
- `Chain`: True to offset the chain of sketch entities, false to offset only the selected sketch entities (see **Remarks**)
- `CapEnds`: Cap the ends as defined by [swSkOffsetCapEndType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSkOffsetCapEndType_e.html)
- `MakeConstruction`: Convert original and offset sketch entities to construction sketch entities as defined by [swSkOffsetMakeConstructionType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSkOffsetMakeConstructionType_e.html)
- `AddDimensions`: True to include the offset distance in the sketch, false to not

### Return Value

True if the selected sketch entities are offset, false if not

## VBA Syntax

See [SketchManager::SketchOffset2](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~SketchOffset2.html).

## Examples

[Offset Sketch (C#)](Sketch_Offset_Example_CSharp.htm)
[Offset Sketch (VB.NET)](Sketch_Offset_Example_VBNET.htm)
[Offset Sketch (VBA)](Sketch_Offset_Example_VB.htm)

## Remarks

Specifying true for Chain offsets the selected sketch entities and any other sketch entities that belong to the same contour or chain (contiguous geometric entities like edges).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[IModelDoc2::SketchOffsetEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.html)
[IModelDoc2::SketchOffsetEdges Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEdges.html)
[IModelDocExtension::SketchOffsetOnSurface Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SketchOffsetOnSurface.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
