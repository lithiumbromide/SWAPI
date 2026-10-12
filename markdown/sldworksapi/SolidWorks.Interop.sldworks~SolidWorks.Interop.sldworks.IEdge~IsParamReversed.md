---
title: "IsParamReversed Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "IsParamReversed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IsParamReversed.html"
---

# IsParamReversed Method (IEdge)

Gets whether the edge and its underlying curve have the same parameterization or if the direction is reversed.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsParamReversed() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As System.Boolean

value = instance.IsParamReversed()
```

### C#

```csharp
System.bool IsParamReversed()
```

### C++/CLI

```cpp
System.bool IsParamReversed();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the curve direction and edge direction are different, false if not

## VBA Syntax

See [Edge::IsParamReversed](ms-its:sldworksapivb6.chm::/sldworks~Edge~IsParamReversed.html).

## Remarks

If this method returns True, then the curve direction and edge direction are different. As the parameter increases, the corresponding point on the edge moves from the end of the edge to the start.

If this method returns false, then the curve direction and edge direction are the same.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.html)
[IEdge::IGetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
