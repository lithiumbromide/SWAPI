---
title: "IImprintingFaces Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "IImprintingFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFaces.html"
---

# IImprintingFaces Method (IModeler)

Imprints the specified tool faces onto the specified target faces.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IImprintingFaces( _
   ByRef TargetEdges As Edge, _
   ByRef ToolEdges As Edge, _
   ByRef TargetVertices As Vertex, _
   ByRef ToolVertices As Vertex _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim TargetEdges As Edge
Dim ToolEdges As Edge
Dim TargetVertices As Vertex
Dim ToolVertices As Vertex

instance.IImprintingFaces(TargetEdges, ToolEdges, TargetVertices, ToolVertices)
```

### C#

```csharp
void IImprintingFaces(
   out Edge TargetEdges,
   out Edge ToolEdges,
   out Vertex TargetVertices,
   out Vertex ToolVertices
)
```

### C++/CLI

```cpp
void IImprintingFaces(
   [Out] Edge^ TargetEdges,
   [Out] Edge^ ToolEdges,
   [Out] Vertex^ TargetVertices,
   [Out] Vertex^ ToolVertices
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TargetEdges`: Array of target [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
- `ToolEdges`: Array of tool [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
- `TargetVertices`: Array of target [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)
- `ToolVertices`: Array of tool [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [Modeler::IImprintingFaces](ms-its:sldworksapivb6.chm::/sldworks~Modeler~IImprintingFaces.html).

## Remarks

Call [IModeler::IImprintingFacesCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~IImprintingFacesCount2.html) before calling this method.

The target and tool faces must:

- belong to different bodies.
- intersect each other.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::ImprintingFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ImprintingFaces.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
