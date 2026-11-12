---
title: "GetAdjacentFaces Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "GetAdjacentFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetAdjacentFaces.html"
---

# GetAdjacentFaces Method (IVertex)

Gets the faces adjacent to this vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAdjacentFaces() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim value As System.Object

value = instance.GetAdjacentFaces()
```

### C#

```csharp
System.object GetAdjacentFaces()
```

### C++/CLI

```cpp
System.Object^ GetAdjacentFaces();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) adjacent to this vertex

## VBA Syntax

See [Vertex::GetAdjacentFaces](ms-its:sldworksapivb6.chm::/sldworks~Vertex~GetAdjacentFaces.html).

## Examples

[Get Faces Adjacent to Vertex (VBA)](Get_Faces_Adjacent_to_Vertex_Example_VB.htm)

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::IGetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFaces.html)
[IVertex::IGetAdjacentFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFacesCount.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12.2
