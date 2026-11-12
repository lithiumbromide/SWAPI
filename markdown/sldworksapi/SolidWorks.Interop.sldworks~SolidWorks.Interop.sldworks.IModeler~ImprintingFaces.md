---
title: "ImprintingFaces Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ImprintingFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ImprintingFaces.html"
---

# ImprintingFaces Method (IModeler)

Imprints the specified tool faces onto the specified target faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function ImprintingFaces( _
   ByVal TargetFaceArray As System.Object, _
   ByVal ToolFaceArray As System.Object, _
   ByVal Options As System.Integer, _
   ByRef TargetEdges As System.Object, _
   ByRef ToolEdges As System.Object, _
   ByRef TargetVertices As System.Object, _
   ByRef ToolVertices As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim TargetFaceArray As System.Object
Dim ToolFaceArray As System.Object
Dim Options As System.Integer
Dim TargetEdges As System.Object
Dim ToolEdges As System.Object
Dim TargetVertices As System.Object
Dim ToolVertices As System.Object
Dim value As System.Boolean

value = instance.ImprintingFaces(TargetFaceArray, ToolFaceArray, Options, TargetEdges, ToolEdges, TargetVertices, ToolVertices)
```

### C#

```csharp
System.bool ImprintingFaces(
   System.object TargetFaceArray,
   System.object ToolFaceArray,
   System.int Options,
   out System.object TargetEdges,
   out System.object ToolEdges,
   out System.object TargetVertices,
   out System.object ToolVertices
)
```

### C++/CLI

```cpp
System.bool ImprintingFaces(
   System.Object^ TargetFaceArray,
   System.Object^ ToolFaceArray,
   System.int Options,
   [Out] System.Object^ TargetEdges,
   [Out] System.Object^ ToolEdges,
   [Out] System.Object^ TargetVertices,
   [Out] System.Object^ ToolVertices
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TargetFaceArray`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that describe the target body
- `ToolFaceArray`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that describe the tool body
- `Options`: Options for this operation as defined in [swImprintingFacesOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImprintingFacesOpts_e.html)
- `TargetEdges`: Array target [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
- `ToolEdges`: Array of tool [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
- `TargetVertices`: Array of target [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)
- `ToolVertices`: Array of tool [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

### Return Value

True if the operation was successful, false if not

## VBA Syntax

See [Modeler::ImprintingFaces](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ImprintingFaces.html).

## Remarks

The target and tool faces must:

- belong to different bodies.
- intersect each other.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::IImprintingFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFaces.html)
[IModeler::IImprintingFacesCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFacesCount2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
