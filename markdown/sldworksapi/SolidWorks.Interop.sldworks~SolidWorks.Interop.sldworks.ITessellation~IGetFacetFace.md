---
title: "IGetFacetFace Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetFacetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFacetFace.html"
---

# IGetFacetFace Method (ITessellation)

Obsolete. Superseded by [ITessellation::IGetFacetFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~IGetFacetFace2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFacetFace( _
   ByVal FacetId As System.Integer _
) As Face
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FacetId As System.Integer
Dim value As Face

value = instance.IGetFacetFace(FacetId)
```

### C#

```csharp
Face IGetFacetFace(
   System.int FacetId
)
```

### C++/CLI

```cpp
Face^ IGetFacetFace(
   System.int FacetId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FacetId`:

## VBA Syntax

See [Tessellation::IGetFacetFace](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~IGetFacetFace.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
