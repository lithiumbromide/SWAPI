---
title: "GetFacetFace Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetFacetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetFace.html"
---

# GetFacetFace Method (ITessellation)

Gets a face that corresponds to a facet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacetFace( _
   ByVal FacetId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FacetId As System.Integer
Dim value As System.Object

value = instance.GetFacetFace(FacetId)
```

### C#

```csharp
System.object GetFacetFace(
   System.int FacetId
)
```

### C++/CLI

```cpp
System.Object^ GetFacetFace(
   System.int FacetId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FacetId`: Facet ID of the facet from which to return the face

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to which that this facet belongs

## VBA Syntax

See [Tessellation::GetFacetFace](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetFacetFace.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::IGetFacetFace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFace2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
