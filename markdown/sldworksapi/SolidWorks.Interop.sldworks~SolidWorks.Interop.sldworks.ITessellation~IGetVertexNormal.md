---
title: "IGetVertexNormal Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetVertexNormal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetVertexNormal.html"
---

# IGetVertexNormal Method (ITessellation)

Gets the information that describes the normal direction corresponding to vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVertexNormal( _
   ByVal VertexId As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim VertexId As System.Integer
Dim value As System.Double

value = instance.IGetVertexNormal(VertexId)
```

### C#

```csharp
System.double IGetVertexNormal(
   System.int VertexId
)
```

### C++/CLI

```cpp
System.double IGetVertexNormal(
   System.int VertexId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VertexId`: ID of the vertex from which you want to return the normal information

### Return Value

Array of 3 doubles describing the normal vector direction of this vertex corresponding to the face to which it belongs

## VBA Syntax

See [Tessellation::IGetVertexNormal](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~IGetVertexNormal.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellate::GetVertexNormal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexNormal.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
