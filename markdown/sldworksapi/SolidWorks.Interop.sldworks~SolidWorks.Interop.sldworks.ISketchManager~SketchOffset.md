---
title: "SketchOffset Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "SketchOffset"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset.html"
---

# SketchOffset Method (ISketchManager)

Obsolete. Superseded by [ISketchManager::SketchOffset2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchOffset( _
   ByVal Offset As System.Double, _
   ByVal BothDirections As System.Boolean, _
   ByVal Chain As System.Boolean, _
   ByVal CapEnds As System.Boolean, _
   ByVal MakeConstruction As System.Boolean, _
   ByVal AddDimensions As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim Offset As System.Double
Dim BothDirections As System.Boolean
Dim Chain As System.Boolean
Dim CapEnds As System.Boolean
Dim MakeConstruction As System.Boolean
Dim AddDimensions As System.Boolean
Dim value As System.Boolean

value = instance.SketchOffset(Offset, BothDirections, Chain, CapEnds, MakeConstruction, AddDimensions)
```

### C#

```csharp
System.bool SketchOffset(
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain,
   System.bool CapEnds,
   System.bool MakeConstruction,
   System.bool AddDimensions
)
```

### C++/CLI

```cpp
System.bool SketchOffset(
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain,
   System.bool CapEnds,
   System.bool MakeConstruction,
   System.bool AddDimensions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Offset`: Offset value; negative value offsets in opposite direction
- `BothDirections`: True to offset the sketch entities in both directions, false to not
- `Chain`: True to offset the chain of sketch entities, false if you want only the selected sketch entities offset (see **Remarks**)
- `CapEnds`: True to cap the bidirectional offset with arcs, false to not
- `MakeConstruction`: True to make the sketch entities construction geometry after offsetting, false to not
- `AddDimensions`: True to include the offset distance in the sketch, false to not

### Return Value

True if the sketch entities are offset, false if not

## VBA Syntax

See [SketchManager::SketchOffset](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~SketchOffset.html).

## Remarks

Specifying true to the Chain argument offsets the selected entity and any other entities that belong to the same contour or chain (contiguous geometric entities like edges).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
