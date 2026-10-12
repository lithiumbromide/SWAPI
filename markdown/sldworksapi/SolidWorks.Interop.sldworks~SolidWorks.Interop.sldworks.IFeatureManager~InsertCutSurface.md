---
title: "InsertCutSurface Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertCutSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutSurface.html"
---

# InsertCutSurface Method (IFeatureManager)

Inserts a surface-cut feature using the preselected surface or plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCutSurface( _
   ByVal Flip As System.Boolean, _
   ByVal KeepPieceIndex As System.Integer, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean, _
   ByVal Bodies As System.Object, _
   ByRef Error As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Flip As System.Boolean
Dim KeepPieceIndex As System.Integer
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim Bodies As System.Object
Dim Error As System.Integer
Dim value As Feature

value = instance.InsertCutSurface(Flip, KeepPieceIndex, UseFeatScope, UseAutoSelect, Bodies, Error)
```

### C#

```csharp
Feature InsertCutSurface(
   System.bool Flip,
   System.int KeepPieceIndex,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.object Bodies,
   out System.int Error
)
```

### C++/CLI

```cpp
Feature^ InsertCutSurface(
   System.bool Flip,
   System.int KeepPieceIndex,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.Object^ Bodies,
   [Out] System.int Error
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Flip`: True to flip the direction of the cut, false to not
- `KeepPieceIndex`: Piece to keep if there is ambiguity (see **Remarks**)
- `UseFeatScope`: True to cut only the bodies passed to Bodies that intersect with the cut, false to cut all bodies that intersect with the cut
- `UseAutoSelect`: True to automatically cut all bodies that intersect with the cut, false to cut only the bodies passed to Bodies that intersect with the cut
- `Bodies`: - Array of specific [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) that intersect with the cut

    - UseFeatScope = true
    - UseAutoSelect = false

  - or -

  - Empty array indicating to cut all bodies that intersect with the cut

    - UseFeatScope = false
    - UseAutoSelect = true
- `Error`: Status of the cut as defined in [swSurfaceCutFeatureError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSurfaceCutFeatureError_e.html)

### Return Value

Surface-cut [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertCutSurface](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertCutSurface.html).

## Examples

[Insert Surface-cut Feature (C#)](Insert_Surface-cut_Feature_Example_CSharp.htm)
[Insert Surface-cut Feature (VB.NET)](Insert_Surface-cut_Feature_Example_VBNET.htm)
[Insert Surface-cut Feature (VBA)](Insert_Surface-cut_Feature_Example_VB.htm)

## Remarks

When there is ambiguity in the result of a cut, KeepPieceIndex is used to resolve which of the possible results is used. This can be set to -1 if there is no ambiguity; otherwise, it should be the index of the result, starting from 0 (up to one less than the possible number of outcomes).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.html)

## Availability

SOLIDWORKS 2013 SP1, Revision Number 21.1
