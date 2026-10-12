---
title: "GetTwoAdjacentFaces2 Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "GetTwoAdjacentFaces2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetTwoAdjacentFaces2.html"
---

# GetTwoAdjacentFaces2 Method (IEdge)

Gets the two faces adjacent to an edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTwoAdjacentFaces2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As System.Object

value = instance.GetTwoAdjacentFaces2()
```

### C#

```csharp
System.object GetTwoAdjacentFaces2()
```

### C++/CLI

```cpp
System.Object^ GetTwoAdjacentFaces2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing two adjacent [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [Edge::GetTwoAdjacentFaces2](ms-its:sldworksapivb6.chm::/sldworks~Edge~GetTwoAdjacentFaces2.html).

## Examples

[Get Angle of Hole Not Normal to a Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)

## Remarks

This method is designed to be used with body-related edges, not reference curve or reference sketch edges. This method supports both solid and sheet bodies.

| If... | Then the values returned are... |
| --- | --- |
| Two valid faces exist | Two faces |
| Only one valid face exists | One face and NULL |

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::IGetTwoAdjacentFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetTwoAdjacentFaces2.html)
[IVertex::GetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetAdjacentFaces.html)
[IVertex::IGetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
