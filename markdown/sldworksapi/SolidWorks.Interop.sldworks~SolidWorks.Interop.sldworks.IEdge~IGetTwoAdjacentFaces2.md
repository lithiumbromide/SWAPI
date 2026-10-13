---
title: "IGetTwoAdjacentFaces2 Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "IGetTwoAdjacentFaces2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTwoAdjacentFaces2.html"
---

# IGetTwoAdjacentFaces2 Method (IEdge)

Gets the two faces adjacent to an edge.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetTwoAdjacentFaces2( _
   ByRef Face1 As Face2, _
   ByRef Face2 As Face2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim Face1 As Face2
Dim Face2 As Face2

instance.IGetTwoAdjacentFaces2(Face1, Face2)
```

### C#

```csharp
void IGetTwoAdjacentFaces2(
   out Face2 Face1,
   out Face2 Face2
)
```

### C++/CLI

```cpp
void IGetTwoAdjacentFaces2(
   [Out] Face2^ Face1,
   [Out] Face2^ Face2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Face1`: Pointer to the first adjacent [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)
- `Face2`: Pointer to the second adjacent [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [Edge::IGetTwoAdjacentFaces2](ms-its:sldworksapivb6.chm::/sldworks~Edge~IGetTwoAdjacentFaces2.html).

## Remarks

This method is designed to be used with body-related edges, not reference curve or reference sketch edges. This method supports both solid and sheet bodies.

| If... | Then the values returned are... |
| --- | --- |
| Two valid faces exist | Two faces |
| Only one valid face exists | One face and NULL |

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::GetTwoAdjacentFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTwoAdjacentFaces2.html)
[IVertex::GetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetAdjacentFaces.html)
[IVertex::IGetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
