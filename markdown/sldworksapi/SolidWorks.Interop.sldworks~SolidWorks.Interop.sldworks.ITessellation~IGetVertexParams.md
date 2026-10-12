---
title: "IGetVertexParams Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetVertexParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetVertexParams.html"
---

# IGetVertexParams Method (ITessellation)

Gets the parameters corresponding to a tessellation vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVertexParams( _
   ByVal VertexId As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim VertexId As System.Integer
Dim value As System.Double

value = instance.IGetVertexParams(VertexId)
```

### C#

```csharp
System.double IGetVertexParams(
   System.int VertexId
)
```

### C++/CLI

```cpp
System.double IGetVertexParams(
   System.int VertexId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VertexId`: ID of the tessellation vertex for which you want to the parameters

### Return Value

- in-process, unmanaged C++: Pointer to an array of contains 17 doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The following parameters returned from this method are formatted as an array of 17 doubles:

- u, v - location of the vertex on the face (return value position [0-1])
- du - tangent vector at u (return value [2-4])
- dv - tangent vector at v (return value [5-7])
- d2u, dudv, d2v - curvature vectors for u and v (return value [8-16])

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellate::GetVertexParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexParams.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
