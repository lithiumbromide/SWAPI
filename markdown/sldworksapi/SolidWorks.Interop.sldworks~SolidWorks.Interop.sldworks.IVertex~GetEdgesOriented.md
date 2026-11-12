---
title: "GetEdgesOriented Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "GetEdgesOriented"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetEdgesOriented.html"
---

# GetEdgesOriented Method (IVertex)

Gets the enumerated edges and orients them per coedge in the direction corresponding to this vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgesOriented() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim value As System.Object

value = instance.GetEdgesOriented()
```

### C#

```csharp
System.object GetEdgesOriented()
```

### C++/CLI

```cpp
System.Object^ GetEdgesOriented();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumEdges.html) for this vertex

## VBA Syntax

See [Vertex::GetEdgesOriented](ms-its:sldworksapivb6.chm::/sldworks~Vertex~GetEdgesOriented.html).

## Remarks

The order of the edges is counter-clockwise.

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::EnumEdgesOriented Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~EnumEdgesOriented.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12.2
