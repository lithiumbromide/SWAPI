---
title: "GetVertexPoint Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetVertexPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetVertexPoint.html"
---

# GetVertexPoint Method (ITessellation)

Gets the X, Y and Z values that describe a tessellation vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVertexPoint( _
   ByVal VertexId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim VertexId As System.Integer
Dim value As System.Object

value = instance.GetVertexPoint(VertexId)
```

### C#

```csharp
System.object GetVertexPoint(
   System.int VertexId
)
```

### C++/CLI

```cpp
System.Object^ GetVertexPoint(
   System.int VertexId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VertexId`: Tessellation vertex ID of the vertex for which you want to get the X Y Z position values

### Return Value

Array of 3 doubles that describe the tessellation vertex's X, Y, and Z position

## VBA Syntax

See [Tessellation::GetVertexPoint](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetVertexPoint.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
