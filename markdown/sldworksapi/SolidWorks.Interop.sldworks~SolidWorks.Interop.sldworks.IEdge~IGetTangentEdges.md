---
title: "IGetTangentEdges Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "IGetTangentEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTangentEdges.html"
---

# IGetTangentEdges Method (IEdge)

Gets all of the edges tangent to this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTangentEdges( _
   ByVal Count As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim Count As System.Integer
Dim value As Edge

value = instance.IGetTangentEdges(Count)
```

### C#

```csharp
Edge IGetTangentEdges(
   System.int Count
)
```

### C++/CLI

```cpp
Edge^ IGetTangentEdges(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of tangent edges

### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IEdge::GetTangentEdgesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetTangentEdgesCount.html) before this method.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::GetTangentEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTangentEdges.html)
[IModelDoc2::SelectTangency Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectTangency.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
