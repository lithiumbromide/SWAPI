---
title: "InsertCutSurface Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertCutSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCutSurface.html"
---

# InsertCutSurface Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertCutSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCutSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertCutSurface( _
   ByVal Flip As System.Boolean, _
   ByVal KeepPieceIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Flip As System.Boolean
Dim KeepPieceIndex As System.Integer

instance.InsertCutSurface(Flip, KeepPieceIndex)
```

### C#

```csharp
void InsertCutSurface(
   System.bool Flip,
   System.int KeepPieceIndex
)
```

### C++/CLI

```cpp
void InsertCutSurface(
   System.bool Flip,
   System.int KeepPieceIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Flip`: True to flip the direction, false to not
- `KeepPieceIndex`: Piece to keep if there is ambiguity

## VBA Syntax

See [ModelDoc2::InsertCutSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertCutSurface.html).

## Remarks

When there is ambiguity in the result of a cut, KeepPieceIndex is used to resolve which of the possible results is used. This can be set to -1 if there is no ambiguity; otherwise, it should be the index of the result, starting from 0 (up to one less than the possible number of outcomes).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
