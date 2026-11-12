---
title: "EdgeInFaceSense Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "EdgeInFaceSense"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~EdgeInFaceSense.html"
---

# EdgeInFaceSense Method (IEdge)

Checks whether the edge and the loop lying on the specified face have the same direction (sense).

## Syntax

### Visual Basic (Declaration)

```vb
Function EdgeInFaceSense( _
   ByVal Facedisp As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim Facedisp As System.Object
Dim value As System.Boolean

value = instance.EdgeInFaceSense(Facedisp)
```

### C#

```csharp
System.bool EdgeInFaceSense(
   System.object Facedisp
)
```

### C++/CLI

```cpp
System.bool EdgeInFaceSense(
   System.Object^ Facedisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Facedisp`: Face that the edge is on

### Return Value

True for the same direction, false for the opposite direction

## VBA Syntax

See [Edge::EdgeInFaceSense](ms-its:sldworksapivb6.chm::/sldworks~Edge~EdgeInFaceSense.html).

## Remarks

If this edge does not belong to the specified face, then this method can cause unpredictable
results.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::IEdgeInFaceSense2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEdgeInFaceSense2.html)
