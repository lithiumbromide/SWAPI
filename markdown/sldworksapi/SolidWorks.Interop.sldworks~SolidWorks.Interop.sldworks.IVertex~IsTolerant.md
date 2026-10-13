---
title: "IsTolerant Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "IsTolerant"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IsTolerant.html"
---

# IsTolerant Method (IVertex)

Gets whether a vertex is tolerant and its tolerance value.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsTolerant( _
   ByRef Tolerance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim Tolerance As System.Double
Dim value As System.Boolean

value = instance.IsTolerant(Tolerance)
```

### C#

```csharp
System.bool IsTolerant(
   out System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool IsTolerant(
   [Out] System.double Tolerance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Tolerance`: Vertex tolerance or gap in meters

### Return Value

True if tolerant, false if not tolerant

## VBA Syntax

See [Vertex::IsTolerant](ms-its:sldworksapivb6.chm::/sldworks~Vertex~IsTolerant.html)

## Examples

[Get Maximum Edge and Vertex Gaps (VBA)](Get_Maximum_Edge_and_Vertex_Gaps_Example_VB.htm)
[Get Maximum Edge and Vertex Gaps (VB.NET)](Get_Maximum_Edge_and_Vertex_Gaps_Example_VBNET.htm)
[Get Maximum Edge and Vertex Gaps (C#)](Get_Maximum_Edge_and_Vertex_Gaps_Example_CSharp.htm)

## Remarks

If the tolerance (or gap) between common vertices in a part:

- is greater than 1/2 of the session precision (i.e., > 5.0E-9 mm), then each vertex is tolerant, and this method returns true.
- is less than or equal to 1/2 of the session precision (i.e., <= 5.0E-9 mm), then each vertex is exact and not tolerant, and this method returns false.

Traverse part body vertices and use this method to find the maximum vertex gap (tolerance) in a part, which can also be found using the **Tools > Check** dialog in the SOLIDWORKS Design user interface.

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IEdge::IsTolerant](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IsTolerant.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2.0
