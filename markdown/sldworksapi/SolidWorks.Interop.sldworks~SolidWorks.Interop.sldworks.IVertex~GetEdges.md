---
title: "GetEdges Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "GetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetEdges.html"
---

# GetEdges Method (IVertex)

Gets a list of enumerated edges corresponding to this vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdges() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim value As System.Object

value = instance.GetEdges()
```

### C#

```csharp
System.object GetEdges()
```

### C++/CLI

```cpp
System.Object^ GetEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumEdges.html) corresponding to this vertex

## VBA Syntax

See [Vertex::GetEdges](ms-its:sldworksapivb6.chm::/sldworks~Vertex~GetEdges.html).

## Examples

[Get Edges for Vertex (VBA)](Get_Edges_for_Vertex_Example_VB.htm)

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::EnumEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~EnumEdges.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12.2
