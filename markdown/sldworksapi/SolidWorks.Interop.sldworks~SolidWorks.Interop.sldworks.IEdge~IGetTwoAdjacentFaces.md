---
title: "IGetTwoAdjacentFaces Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "IGetTwoAdjacentFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTwoAdjacentFaces.html"
---

# IGetTwoAdjacentFaces Method (IEdge)

Obsolete. Superseded by [IEdge::IGetTwoAdjacentFaces2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetTwoAdjacentFaces2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetTwoAdjacentFaces( _
   ByRef Face1 As Face, _
   ByRef Face2 As Face _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim Face1 As Face
Dim Face2 As Face

instance.IGetTwoAdjacentFaces(Face1, Face2)
```

### C#

```csharp
void IGetTwoAdjacentFaces(
   out Face Face1,
   out Face Face2
)
```

### C++/CLI

```cpp
void IGetTwoAdjacentFaces(
   [Out] Face^ Face1,
   [Out] Face^ Face2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Face1`:
- `Face2`: v

## VBA Syntax

See [Edge::IGetTwoAdjacentFaces](ms-its:sldworksapivb6.chm::/sldworks~Edge~IGetTwoAdjacentFaces.html).

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
