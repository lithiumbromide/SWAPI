---
title: "IGetFacetData Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetFacetData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFacetData.html"
---

# IGetFacetData Method (IFace2)

Obsolete. Superseded by [IFace2::GetTessNorms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTessNorms.html), [IFace2::IGetTessNorms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTessNorms.html), [IFace2::GetTessTextures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTessTextures.html)[, IFace2::IGetTessTextures, IFace2::GetTessTriangleCount, IFace2::GetTessTriangles,](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTessTriangles.html) [IFace2::IGetTessTriangles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTessTriangles.html), [IFace2::GetTessTriStripEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTessTriStripEdges.html), [IFace2::IGetTessTriStripEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTessTriStripEdges.html), [IFace::GetTessTriStripNorms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTessTriStripNorms.html), [IFace2::IGetTessTriStripNorms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTessTriStripNorms.html), [IFace2::GetTessTriStrips](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTessTriStrips.html), and [IFace2::IGetTessTriStrips](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTessTriStrips.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetFacetData( _
   ByVal FacetMesh As System.Integer, _
   ByRef NFacets As System.Integer, _
   ByRef NStrips As System.Integer, _
   ByRef StripVertexNums As System.Integer, _
   ByRef VertexCoords As System.Single, _
   ByRef NormalCoords As System.Single _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim FacetMesh As System.Integer
Dim NFacets As System.Integer
Dim NStrips As System.Integer
Dim StripVertexNums As System.Integer
Dim VertexCoords As System.Single
Dim NormalCoords As System.Single

instance.IGetFacetData(FacetMesh, NFacets, NStrips, StripVertexNums, VertexCoords, NormalCoords)
```

### C#

```csharp
void IGetFacetData(
   System.int FacetMesh,
   ref System.int NFacets,
   ref System.int NStrips,
   ref System.int StripVertexNums,
   ref System.float VertexCoords,
   ref System.float NormalCoords
)
```

### C++/CLI

```cpp
void IGetFacetData(
   System.int FacetMesh,
   System.int% NFacets,
   System.int% NStrips,
   System.int% StripVertexNums,
   System.float% VertexCoords,
   System.float% NormalCoords
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FacetMesh`:
- `NFacets`:
- `NStrips`:
- `StripVertexNums`:
- `VertexCoords`:
- `NormalCoords`:

## VBA Syntax

See [Face2::IGetFacetData](ms-its:sldworksapivb6.chm::/sldworks~Face2~IGetFacetData.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
