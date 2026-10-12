---
title: "IGetAdjacentFacesCount Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "IGetAdjacentFacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFacesCount.html"
---

# IGetAdjacentFacesCount Method (IVertex)

Gets the number of faces adjacent to this vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAdjacentFacesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim value As System.Integer

value = instance.IGetAdjacentFacesCount()
```

### C#

```csharp
System.int IGetAdjacentFacesCount()
```

### C++/CLI

```cpp
System.int IGetAdjacentFacesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces adjacent to this vertex

## VBA Syntax

See [Vertex::IGetAdjacentFacesCount](ms-its:sldworksapivb6.chm::/sldworks~Vertex~IGetAdjacentFacesCount.html).

## Remarks

Call this method before calling [IVertex::IGetAdjacentFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex~IGetAdjacentFaces.html).

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::GetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetAdjacentFaces.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
