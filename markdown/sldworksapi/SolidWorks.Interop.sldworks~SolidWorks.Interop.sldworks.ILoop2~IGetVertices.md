---
title: "IGetVertices Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "IGetVertices"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetVertices.html"
---

# IGetVertices Method (ILoop2)

Gets the vertices in this loop.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetVertices( _
   ByVal NumVertices As System.Integer, _
   ByRef Vertices As Vertex _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim NumVertices As System.Integer
Dim Vertices As Vertex

instance.IGetVertices(NumVertices, Vertices)
```

### C#

```csharp
void IGetVertices(
   System.int NumVertices,
   out Vertex Vertices
)
```

### C++/CLI

```cpp
void IGetVertices(
   System.int NumVertices,
   [Out] Vertex^ Vertices
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumVertices`: Number of vertices in this loop
- `Vertices`: - in-process, unmanaged C++: Pointer to an array of [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) for this loop

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::GetVertexCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetVertexCount.html)
[ILoop2::GetVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetVertices.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number
