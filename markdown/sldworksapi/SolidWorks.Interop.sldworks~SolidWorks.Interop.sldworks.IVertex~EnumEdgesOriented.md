---
title: "EnumEdgesOriented Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "EnumEdgesOriented"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~EnumEdgesOriented.html"
---

# EnumEdgesOriented Method (IVertex)

Gets the enumerated edges and orients them per coedge in the direction corresponding to this vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumEdgesOriented() As EnumEdges
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim value As EnumEdges

value = instance.EnumEdgesOriented()
```

### C#

```csharp
EnumEdges EnumEdgesOriented()
```

### C++/CLI

```cpp
EnumEdges^ EnumEdgesOriented();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Enumerated edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumEdges.html)

## VBA Syntax

See [Vertex::EnumEdgesOriented](ms-its:sldworksapivb6.chm::/sldworks~Vertex~EnumEdgesOriented.html).

## Remarks

The order of the edges is counter-clockwise.

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
