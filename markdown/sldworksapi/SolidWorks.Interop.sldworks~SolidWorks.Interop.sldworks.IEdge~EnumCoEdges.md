---
title: "EnumCoEdges Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "EnumCoEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~EnumCoEdges.html"
---

# EnumCoEdges Method (IEdge)

Lists the coedges that reference this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumCoEdges() As EnumCoEdges
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As EnumCoEdges

value = instance.EnumCoEdges()
```

### C#

```csharp
EnumCoEdges EnumCoEdges()
```

### C++/CLI

```cpp
EnumCoEdges^ EnumCoEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [enumerated list of coedges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumCoEdges.html)

## VBA Syntax

See [Edge::EnumCoEdges](ms-its:sldworksapivb6.chm::/sldworks~Edge~EnumCoEdges.html).

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEnumCoEdges::Next Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges~Next.html)
