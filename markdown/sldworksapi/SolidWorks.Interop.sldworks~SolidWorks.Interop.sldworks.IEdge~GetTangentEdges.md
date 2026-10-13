---
title: "GetTangentEdges Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "GetTangentEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdges.html"
---

# GetTangentEdges Method (IEdge)

Gets all of the edges tangent to this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTangentEdges() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As System.Object

value = instance.GetTangentEdges()
```

### C#

```csharp
System.object GetTangentEdges()
```

### C++/CLI

```cpp
System.Object^ GetTangentEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of tangent edges

## VBA Syntax

See [Edge::GetTangentEdges](ms-its:sldworksapivb6.chm::/sldworks~Edge~GetTangentEdges.html).

## Examples

[Select Tangent Edges Topologically (VBA)](Select_Tangent_Edges_Topologically_Example_VB.htm)

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::IGetTangentEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTangentEdges.html)
[IEdge::GetTangentEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdgesCount.html)
[IModelDoc2::SelectTangency Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectTangency.html)

## Availability

SOLIDWORKS 2001Pus SP1, Revision Number 10.1
