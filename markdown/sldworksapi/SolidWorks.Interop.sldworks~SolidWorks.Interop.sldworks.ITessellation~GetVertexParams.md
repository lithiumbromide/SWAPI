---
title: "GetVertexParams Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetVertexParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexParams.html"
---

# GetVertexParams Method (ITessellation)

Gets the parameters corresponding to a tessellation vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVertexParams( _
   ByVal VertexId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim VertexId As System.Integer
Dim value As System.Object

value = instance.GetVertexParams(VertexId)
```

### C#

```csharp
System.object GetVertexParams(
   System.int VertexId
)
```

### C++/CLI

```cpp
System.Object^ GetVertexParams(
   System.int VertexId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VertexId`: ID of the tessellation vertex for which you want to the parameters

### Return Value

Array of 17 doubles (see **Remarks**)

## VBA Syntax

See [Tessellation::GetVertexParams](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetVertexParams.html).

## Remarks

The following parameters returned from this method are formatted as an array of 17 doubles:

- u, v - location of the vertex on the face (return value position [0-1])
- du - tangent vector at u (return value [2-4])
- dv - tangent vector at v (return value [5-7])
- d2u, dudv, d2v - curvature vectors for u and v (return value [8-16])

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::IGetVertexParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetVertexParams.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
