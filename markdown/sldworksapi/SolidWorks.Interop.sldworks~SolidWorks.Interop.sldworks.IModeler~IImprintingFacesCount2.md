---
title: "IImprintingFacesCount2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "IImprintingFacesCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFacesCount2.html"
---

# IImprintingFacesCount2 Method (IModeler)

Gets the number of imprinted edges and vertices in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IImprintingFacesCount2( _
   ByVal NTargetFaces As System.Integer, _
   ByRef TargetFaceArray As Face2, _
   ByVal NToolFaces As System.Integer, _
   ByRef ToolFaceArray As Face2, _
   ByVal Options As System.Integer, _
   ByRef NTargetEdges As System.Integer, _
   ByRef NtoolEdges As System.Integer, _
   ByRef NtargetVertices As System.Integer, _
   ByRef ToolVertices As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NTargetFaces As System.Integer
Dim TargetFaceArray As Face2
Dim NToolFaces As System.Integer
Dim ToolFaceArray As Face2
Dim Options As System.Integer
Dim NTargetEdges As System.Integer
Dim NtoolEdges As System.Integer
Dim NtargetVertices As System.Integer
Dim ToolVertices As System.Integer
Dim value As System.Boolean

value = instance.IImprintingFacesCount2(NTargetFaces, TargetFaceArray, NToolFaces, ToolFaceArray, Options, NTargetEdges, NtoolEdges, NtargetVertices, ToolVertices)
```

### C#

```csharp
System.bool IImprintingFacesCount2(
   System.int NTargetFaces,
   ref Face2 TargetFaceArray,
   System.int NToolFaces,
   ref Face2 ToolFaceArray,
   System.int Options,
   out System.int NTargetEdges,
   out System.int NtoolEdges,
   out System.int NtargetVertices,
   out System.int ToolVertices
)
```

### C++/CLI

```cpp
System.bool IImprintingFacesCount2(
   System.int NTargetFaces,
   Face2^% TargetFaceArray,
   System.int NToolFaces,
   Face2^% ToolFaceArray,
   System.int Options,
   [Out] System.int NTargetEdges,
   [Out] System.int NtoolEdges,
   [Out] System.int NtargetVertices,
   [Out] System.int ToolVertices
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NTargetFaces`: Number of faces in the target body
- `TargetFaceArray`: Array of the [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that describe the target body
- `NToolFaces`: Number of faces in the tool body
- `ToolFaceArray`: Array of the [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that describe the tool body
- `Options`: Options for this operation as defined in [swImprintingFacesOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImprintingFacesOpts_e.html)
- `NTargetEdges`: Number of edges returned from this operation
- `NtoolEdges`: Number of tool edges returned from this operation
- `NtargetVertices`: Number of target vertices returned from this operation
- `ToolVertices`: Number of tool vertices returned from this operation

### Return Value

True if the operation is successful, false if not

## VBA Syntax

See [Modeler::IImprintingFacesCount2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~IImprintingFacesCount2.html).

## Remarks

Call this method before calling [IModeler::IImprintingFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~IImprintingFaces.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::ImprintingFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ImprintingFaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
