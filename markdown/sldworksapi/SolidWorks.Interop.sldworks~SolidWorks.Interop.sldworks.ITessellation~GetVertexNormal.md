---
title: "GetVertexNormal Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetVertexNormal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexNormal.html"
---

# GetVertexNormal Method (ITessellation)

Gets the information that describes the normal direction corresponding to vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVertexNormal( _
   ByVal VertexId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim VertexId As System.Integer
Dim value As System.Object

value = instance.GetVertexNormal(VertexId)
```

### C#

```csharp
System.object GetVertexNormal(
   System.int VertexId
)
```

### C++/CLI

```cpp
System.Object^ GetVertexNormal(
   System.int VertexId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VertexId`: ID of the vertex from which you want to return the normal information

### Return Value

Array of 3 doubles describing the normal vector direction of this vertex corresponding to the face to which it belongs

## VBA Syntax

See [Tessellation::GetVertexNormal](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetVertexNormal.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::IGetVertexNormal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetVertexNormal.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
