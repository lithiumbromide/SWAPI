---
title: "IGetAdjacentFaces Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "IGetAdjacentFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetAdjacentFaces.html"
---

# IGetAdjacentFaces Method (IVertex)

Gets the faces adjacent to this vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAdjacentFaces( _
   ByVal NFaceCount As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim NFaceCount As System.Integer
Dim value As Face2

value = instance.IGetAdjacentFaces(NFaceCount)
```

### C#

```csharp
Face2 IGetAdjacentFaces(
   System.int NFaceCount
)
```

### C++/CLI

```cpp
Face2^ IGetAdjacentFaces(
   System.int NFaceCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NFaceCount`: Number of adjacent faces

### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) adjacent to this vertex

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IVertex::IGetAdjacentFacesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex~IGetAdjacentFacesCount.html) to get the number of faces adjacent to this vertex.

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::GetAdjacentFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetAdjacentFaces.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12.2
