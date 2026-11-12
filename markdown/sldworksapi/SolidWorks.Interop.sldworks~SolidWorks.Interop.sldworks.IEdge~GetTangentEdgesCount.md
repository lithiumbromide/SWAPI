---
title: "GetTangentEdgesCount Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "GetTangentEdgesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdgesCount.html"
---

# GetTangentEdgesCount Method (IEdge)

Gets the number of edges tangent to this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTangentEdgesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As System.Integer

value = instance.GetTangentEdgesCount()
```

### C#

```csharp
System.int GetTangentEdgesCount()
```

### C++/CLI

```cpp
System.int GetTangentEdgesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of tangent edges

## VBA Syntax

See [Edge::GetTangentEdgesCount](ms-its:sldworksapivb6.chm::/sldworks~Edge~GetTangentEdgesCount.html).

## Remarks

Call this method before calling [IEdge::IGetTangentEdges.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetTangentEdges.html)

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::GetTangentEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdges.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
