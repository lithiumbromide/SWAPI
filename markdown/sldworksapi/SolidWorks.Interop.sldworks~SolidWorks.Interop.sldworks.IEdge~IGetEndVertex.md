---
title: "IGetEndVertex Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "IGetEndVertex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetEndVertex.html"
---

# IGetEndVertex Method (IEdge)

Gets the ending vertex for this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEndVertex() As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As Vertex

value = instance.IGetEndVertex()
```

### C#

```csharp
Vertex IGetEndVertex()
```

### C++/CLI

```cpp
Vertex^ IGetEndVertex();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [Edge::IGetEndVertex](ms-its:sldworksapivb6.chm::/sldworks~Edge~IGetEndVertex.html).

## Remarks

If no vertex exists for this edge (such as the edge of a newly created cylinder), then this method returns NULL.

This method and [IEdge::GetStartVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetStartVertex.html) or [IEdge::IGetStartVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetStartVertex.html) return distinct vertices, unless the edge is closed. Because edges have no natural direction, you cannot necessarily predict which of the two points you will get first and which last.

Use [ICoEdge::GetCurveParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~GetCurveParams.html) or [ICoEdge::IGetCurveParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~IGetCurveParams.html) to get consistent start and end positions.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::GetEndVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetEndVertex.html)
[IEdge::GetStartVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetStartVertex.html)
[IEdge::IGetStartVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetStartVertex.html)
