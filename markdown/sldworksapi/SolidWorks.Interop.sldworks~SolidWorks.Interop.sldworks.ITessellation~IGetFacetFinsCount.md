---
title: "IGetFacetFinsCount Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetFacetFinsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFinsCount.html"
---

# IGetFacetFinsCount Method (ITessellation)

Gets the number of fins corresponding to a facet.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFacetFinsCount( _
   ByVal FacetId As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FacetId As System.Integer
Dim value As System.Integer

value = instance.IGetFacetFinsCount(FacetId)
```

### C#

```csharp
System.int IGetFacetFinsCount(
   System.int FacetId
)
```

### C++/CLI

```cpp
System.int IGetFacetFinsCount(
   System.int FacetId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FacetId`: Facet for which to count fins

### Return Value

Number of fins corresponding to FacetId

## VBA Syntax

See [Tessellation::IGetFacetFinsCount](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~IGetFacetFinsCount.html).

## Remarks

A cache is created when you use this method. This cache is released when you use [ITessellation::IGetFacetFins](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~IGetFacetFins.html). If you use ITessellation::IGetFacetFinsCount again, then the cache is refilled. Alternatively, you can use ITessellation::IGetFacetFins repeatedly.

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::GetFacetFins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetFins.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
