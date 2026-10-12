---
title: "GetFacetFins Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetFacetFins"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFacetFins.html"
---

# GetFacetFins Method (ITessellation)

Gets all of the fin IDs of the fins that border this facet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacetFins( _
   ByVal FacetId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FacetId As System.Integer
Dim value As System.Object

value = instance.GetFacetFins(FacetId)
```

### C#

```csharp
System.object GetFacetFins(
   System.int FacetId
)
```

### C++/CLI

```cpp
System.Object^ GetFacetFins(
   System.int FacetId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FacetId`: ID of the facet to use to return the fin IDs

### Return Value

Array of long or integer values that describe the fin IDs

## VBA Syntax

See [Tessellation::GetFacetFins](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetFacetFins.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::IGetFacetFins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFins.html)
[ITessellation::IGetFacetFinsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFinsCount.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
