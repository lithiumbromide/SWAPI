---
title: "IImprintingFacesCount Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "IImprintingFacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFacesCount.html"
---

# IImprintingFacesCount Method (IModeler)

Obsolete. Superseded by [IModeler::IImprintingFacesCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~IImprintingFacesCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IImprintingFacesCount( _
   ByVal NTargetFaces As System.Integer, _
   ByRef TargetFaceArray As Face, _
   ByVal NToolFaces As System.Integer, _
   ByRef ToolFaceArray As Face, _
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
Dim TargetFaceArray As Face
Dim NToolFaces As System.Integer
Dim ToolFaceArray As Face
Dim Options As System.Integer
Dim NTargetEdges As System.Integer
Dim NtoolEdges As System.Integer
Dim NtargetVertices As System.Integer
Dim ToolVertices As System.Integer
Dim value As System.Boolean

value = instance.IImprintingFacesCount(NTargetFaces, TargetFaceArray, NToolFaces, ToolFaceArray, Options, NTargetEdges, NtoolEdges, NtargetVertices, ToolVertices)
```

### C#

```csharp
System.bool IImprintingFacesCount(
   System.int NTargetFaces,
   ref Face TargetFaceArray,
   System.int NToolFaces,
   ref Face ToolFaceArray,
   System.int Options,
   out System.int NTargetEdges,
   out System.int NtoolEdges,
   out System.int NtargetVertices,
   out System.int ToolVertices
)
```

### C++/CLI

```cpp
System.bool IImprintingFacesCount(
   System.int NTargetFaces,
   Face^% TargetFaceArray,
   System.int NToolFaces,
   Face^% ToolFaceArray,
   System.int Options,
   [Out] System.int NTargetEdges,
   [Out] System.int NtoolEdges,
   [Out] System.int NtargetVertices,
   [Out] System.int ToolVertices
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NTargetFaces`:
- `TargetFaceArray`:
- `NToolFaces`:
- `ToolFaceArray`:
- `Options`:
- `NTargetEdges`:
- `NtoolEdges`:
- `NtargetVertices`:
- `ToolVertices`:

## VBA Syntax

See [Modeler::IImprintingFacesCount](ms-its:sldworksapivb6.chm::/sldworks~Modeler~IImprintingFacesCount.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
