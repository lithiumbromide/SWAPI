---
title: "InsertCosmeticWeldBead2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertCosmeticWeldBead2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead2.html"
---

# InsertCosmeticWeldBead2 Method (IFeatureManager)

Inserts a cosmetic weld bead using either weld geometry or a weld path.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCosmeticWeldBead2( _
   ByVal WeldMode As System.Integer, _
   ByVal WeldFromFaceOrEdgeSet As System.Object, _
   ByVal WeldToFaceOrEdgeSet As System.Object, _
   ByVal WeldSize As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim WeldMode As System.Integer
Dim WeldFromFaceOrEdgeSet As System.Object
Dim WeldToFaceOrEdgeSet As System.Object
Dim WeldSize As System.Double
Dim value As System.Object

value = instance.InsertCosmeticWeldBead2(WeldMode, WeldFromFaceOrEdgeSet, WeldToFaceOrEdgeSet, WeldSize)
```

### C#

```csharp
System.object InsertCosmeticWeldBead2(
   System.int WeldMode,
   System.object WeldFromFaceOrEdgeSet,
   System.object WeldToFaceOrEdgeSet,
   System.double WeldSize
)
```

### C++/CLI

```cpp
System.Object^ InsertCosmeticWeldBead2(
   System.int WeldMode,
   System.Object^ WeldFromFaceOrEdgeSet,
   System.Object^ WeldToFaceOrEdgeSet,
   System.double WeldSize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WeldMode`: Weld mode as defined in[swCosmeticWeldBeadMode_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCosmeticWeldBeadMode_e.html)
- `WeldFromFaceOrEdgeSet`: Array of weld-from entities (see **Remarks**)
- `WeldToFaceOrEdgeSet`: Array of weld-to entities or Nothing or null (see **Remarks**)
- `WeldSize`: Size of weld bead

### Return Value

Array of weld bead [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertCosmeticWeldBead2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertCosmeticWeldBead2.html).

## Examples

[Insert Cosmetic Weld Bead Using Geometric Entities (C#)](Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_CSharp.htm)
[Insert Cosmetic Weld Bead Using Geometric Entities (VB.NET)](Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_VBNET.htm)
[Insert Cosmetic Weld Bead Using Geometric Entities (VBA)](Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_VB.htm)

## Remarks

| WeldMode | Selected entities | Selection marks |
| --- | --- | --- |
| swCosmeticWeldBeadMode_e.swCosmeticWeldBeadMode_WeldGeometry | Either faces or edges as weld-from and weld-to entities NOTE : Both weld-to and weld-from entities must all be the same type of entities; e.g., all faces or all edges. | 4 for each weld-from entity in WeldFromFaceOrEdgeSet 8 for each weld-to entity in WeldToFaceOrEdgeSet |
| swCosmeticWeldBeadMode_e.swCosmeticWeldBeadMode_WeldPath | Edges, sketches , or a combination of edges and sketches are selected as weld-from entities | 0 for each weld-from entity in WeldFromFaceOrEdgeSet Nothing or null for WeldToFaceOrEdgeSet |

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
