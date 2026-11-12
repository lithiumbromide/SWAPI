---
title: "IGetFacetFins Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetFacetFins"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFins.html"
---

# IGetFacetFins Method (ITessellation)

Gets all of the fin IDs of the fins that border this facet.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFacetFins( _
   ByVal FacetId As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FacetId As System.Integer
Dim value As System.Integer

value = instance.IGetFacetFins(FacetId)
```

### C#

```csharp
System.int IGetFacetFins(
   System.int FacetId
)
```

### C++/CLI

```cpp
System.int IGetFacetFins(
   System.int FacetId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FacetId`: ID of the facet to use to return the fin IDs

### Return Value

- in-process, unmanaged C++: Pointer to an array of long or integer values that describe the fin IDs

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

A cache is created when you use [ITessellation::IGetFacetFinsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~IGetFacetFinsCount.html). This cache is released when you use ITessellation::IGetFacetFins. If you use ITessellation::IGetFacetFinsCount again, then the cache is refilled. Alternatively, you can use ITessellation::IGetFacetFins repeatedly.

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellate::GetFacetFins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetFins.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
