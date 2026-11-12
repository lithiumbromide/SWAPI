---
title: "IGetFacetFace2 Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetFacetFace2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFace2.html"
---

# IGetFacetFace2 Method (ITessellation)

Gets a face that corresponds to a facet.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFacetFace2( _
   ByVal FacetId As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FacetId As System.Integer
Dim value As Face2

value = instance.IGetFacetFace2(FacetId)
```

### C#

```csharp
Face2 IGetFacetFace2(
   System.int FacetId
)
```

### C++/CLI

```cpp
Face2^ IGetFacetFace2(
   System.int FacetId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FacetId`: Facet ID of the facet from which you want to return the face pointer

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to which this facet belongs

## VBA Syntax

See [Tessellation::IGetFacetFace2](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~IGetFacetFace2.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::GetFacetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetFace.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
