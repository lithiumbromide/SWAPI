---
title: "IEdgeInFaceSense2 Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "IEdgeInFaceSense2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEdgeInFaceSense2.html"
---

# IEdgeInFaceSense2 Method (IEdge)

Checks whether the edge and the loop lying on the specified face have the same direction (sense).

## Syntax

### Visual Basic (Declaration)

```vb
Function IEdgeInFaceSense2( _
   ByVal Facedisp As Face2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim Facedisp As Face2
Dim value As System.Boolean

value = instance.IEdgeInFaceSense2(Facedisp)
```

### C#

```csharp
System.bool IEdgeInFaceSense2(
   Face2 Facedisp
)
```

### C++/CLI

```cpp
System.bool IEdgeInFaceSense2(
   Face2^ Facedisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Facedisp`: Pointer to the [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that the edge is on

### Return Value

True for same direction as the loop, false for opposite

## VBA Syntax

See [Edge::IEdgeInFaceSense2](ms-its:sldworksapivb6.chm::/sldworks~Edge~IEdgeInFaceSense2.html).

## Remarks

If this edge does not belong to the face that is passed as an argument, unpredictable results can occur.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::EdgeInFaceSense Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~EdgeInFaceSense.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
