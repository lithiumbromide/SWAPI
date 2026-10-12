---
title: "IGetVertexPoint Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetVertexPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetVertexPoint.html"
---

# IGetVertexPoint Method (ITessellation)

Gets the X, Y and Z values that describe a tessellation vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVertexPoint( _
   ByVal VertexId As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim VertexId As System.Integer
Dim value As System.Double

value = instance.IGetVertexPoint(VertexId)
```

### C#

```csharp
System.double IGetVertexPoint(
   System.int VertexId
)
```

### C++/CLI

```cpp
System.double IGetVertexPoint(
   System.int VertexId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VertexId`: Tessellation vertex ID of the vertex for which you want to get the X Y Z position values

### Return Value

Array of 3 doubles that describe the tessellation vertex's X, Y, and Z position

## VBA Syntax

See [Tessellation::IGetVertexPoint](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~IGetVertexPoint.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellate::GetVertexParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexParams.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
