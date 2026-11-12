---
title: "EnumEdges Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "EnumEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~EnumEdges.html"
---

# EnumEdges Method (IVertex)

Gets a list of enumerated edges corresponding to this vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumEdges() As EnumEdges
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim value As EnumEdges

value = instance.EnumEdges()
```

### C#

```csharp
EnumEdges EnumEdges()
```

### C++/CLI

```cpp
EnumEdges^ EnumEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Enumerated edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumEdges.html)

## VBA Syntax

See [Vertex::EnumEdges](ms-its:sldworksapivb6.chm::/sldworks~Vertex~EnumEdges.html).

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::EnumEdgesOriented Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~EnumEdgesOriented.html)
[IVertex::GetEdgesOriented Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetEdgesOriented.html)
[IVertex::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetEdges.html)
