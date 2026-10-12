---
title: "SketchOffset2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchOffset2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffset2.html"
---

# SketchOffset2 Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::SketchOffset](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~SketchOffset.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchOffset2( _
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

value = instance.SketchOffset2(Offset, BothDirections, Chain)
```

### C#

```csharp
System.bool SketchOffset2(
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain
)
```

### C++/CLI

```cpp
System.bool SketchOffset2(
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Offset`: Offset value; negative value offsets in opposite direction
- `BothDirections`: True to offset in both directions, false to not
- `Chain`: True if you want the entire chain of entities offset, false if you want only the selected sketch entities offset (see **Remarks**)

### Return Value

True if the offset is successful, false if not

## VBA Syntax

See [ModelDoc2::SketchOffset2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchOffset2.html).

## Remarks

Specifying true for the Chain argument offsets the selected entity and any other entities that belong to the same contour or chain (contiguous, geometric entities like edges).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SketchOffsetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEdges.html)
[IModelDoc2::SketchOffsetEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
