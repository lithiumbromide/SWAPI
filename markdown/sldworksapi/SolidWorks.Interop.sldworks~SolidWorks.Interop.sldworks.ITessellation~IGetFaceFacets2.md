---
title: "IGetFaceFacets2 Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetFaceFacets2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacets2.html"
---

# IGetFaceFacets2 Method (ITessellation)

Gets the facets IDs that correspond to a face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaceFacets2( _
   ByVal FaceObj As Face2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FaceObj As Face2
Dim value As System.Integer

value = instance.IGetFaceFacets2(FaceObj)
```

### C#

```csharp
System.int IGetFaceFacets2(
   Face2 FaceObj
)
```

### C++/CLI

```cpp
System.int IGetFaceFacets2(
   Face2^ FaceObj
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceObj`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) from which you want to return the corresponding facet IDs

### Return Value

- in-process, unmanaged C++: Pointer to an array of longs or integers that describe the facet IDs that correspond to the face

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

[ITessellation::NeedFaceFacetMap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~NeedFaceFacetMap.html) must be set to true to return results.

Before calling this method, call [ITessellation::IGetFaceFacetsCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~IGetFaceFacetsCount2.html) to fetch the raw facet data. ITessellation::IGetFaceFacets2 clears the cache of raw facet data.

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::GetFaceFacets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFaceFacets.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
