---
title: "GetCoEdges Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "GetCoEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCoEdges.html"
---

# GetCoEdges Method (IEdge)

Gets the coedges that reference this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoEdges() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As System.Object

value = instance.GetCoEdges()
```

### C#

```csharp
System.object GetCoEdges()
```

### C++/CLI

```cpp
System.Object^ GetCoEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of coedges that reference the edge

## VBA Syntax

See [Edge::GetCoEdges](ms-its:sldworksapivb6.chm::/sldworks~Edge~GetCoEdges.html).

## Examples

[Select Loop of Edges (VBA)](Select_Loop_of_Edges_Example_VB_.htm)
[Select Tangent Edges Via Iteration (VBA)](Select_Tangent_Edges_Example_VB.htm)

## Remarks

Call this method for body-related edges, not reference curve or sketch edges.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
