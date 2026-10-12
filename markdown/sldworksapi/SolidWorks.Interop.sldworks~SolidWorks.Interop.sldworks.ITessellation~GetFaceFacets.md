---
title: "GetFaceFacets Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetFaceFacets"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFaceFacets.html"
---

# GetFaceFacets Method (ITessellation)

Gets the facets IDs that correspond to a SOLIDWORKS face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceFacets( _
   ByVal Facedisp As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim Facedisp As System.Object
Dim value As System.Object

value = instance.GetFaceFacets(Facedisp)
```

### C#

```csharp
System.object GetFaceFacets(
   System.object Facedisp
)
```

### C++/CLI

```cpp
System.Object^ GetFaceFacets(
   System.Object^ Facedisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Facedisp`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) from which to return the corresponding facet IDs

### Return Value

Array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) that describe the facet IDs that correspond to the face

## VBA Syntax

See [Tessellation::GetFaceFacets](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetFaceFacets.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

## Remarks

[ITessellation::NeedFaceFacetMap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~NeedFaceFacetMap.html) must be set to true to return results.

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::IGetFaceFacets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacets2.html)
[ITessellation::IGetFaceFacetsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacetsCount2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
