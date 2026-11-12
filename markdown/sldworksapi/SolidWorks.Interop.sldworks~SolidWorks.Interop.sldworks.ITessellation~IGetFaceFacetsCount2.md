---
title: "IGetFaceFacetsCount2 Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetFaceFacetsCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacetsCount2.html"
---

# IGetFaceFacetsCount2 Method (ITessellation)

Gets the number of facets corresponding to a face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaceFacetsCount2( _
   ByVal FaceObj As Face2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FaceObj As Face2
Dim value As System.Integer

value = instance.IGetFaceFacetsCount2(FaceObj)
```

### C#

```csharp
System.int IGetFaceFacetsCount2(
   Face2 FaceObj
)
```

### C++/CLI

```cpp
System.int IGetFaceFacetsCount2(
   Face2^ FaceObj
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceObj`: Face on which to count the facets

### Return Value

Number of facets

## VBA Syntax

See [Tessellation::IGetFaceFacetsCount2](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~IGetFaceFacetsCount2.html).

## Remarks

This method caches the raw facet data after determining the number of facets. A subsequent call to [ITessellation::IGetFaceFacets2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~IGetFaceFacets2.html) does not have to fetch the facet data again.

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::GetFaceFacets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFaceFacets.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
