---
title: "SketchOffsetEntities2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchOffsetEntities2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.html"
---

# SketchOffsetEntities2 Method (IModelDoc2)

Generates entities in the active sketch by offsetting the selected geometry by the specified amount.

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchOffsetEntities2( _
   ByVal Offset As System.Double, _
   ByVal BothDirections As System.Boolean, _
   ByVal Chain As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Offset As System.Double
Dim BothDirections As System.Boolean
Dim Chain As System.Boolean
Dim value As System.Boolean

value = instance.SketchOffsetEntities2(Offset, BothDirections, Chain)
```

### C#

```csharp
System.bool SketchOffsetEntities2(
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain
)
```

### C++/CLI

```cpp
System.bool SketchOffsetEntities2(
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Offset`: Offset distance in meters
- `BothDirections`: True to offset in both directions, false to not
- `Chain`: True if you want entire chain of entities offset, false if you want only selected sketch entities offset (see **Remarks**)

### Return Value

True if the offset is successful, false if not

## VBA Syntax

See [ModelDoc2::SketchOffsetEntities2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchOffsetEntities2.html).

## Remarks

The geometry selected for offset can be an edge, loop, face, external sketch curve, external sketch contour, set of edges, or set of external sketch curves.

Specifying true for the Chain argument offsets the selected entity and any other entities that belong to the same contour or chain (contiguous, geometric entities like edges).

NOTE: If the selected geometry is a sketch item, it must be an external sketch curve (for example, it cannot be an item in the active sketch). To offset sketch segments within the active sketch, use [IModelDoc2::SketchOffset2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchOffset2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SketchOffsetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEdges.html)
[ISketchManager::SketchUseEdge2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge2.html)
[IModelDocExtension::SketchOffsetOnSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SketchOffsetOnSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
