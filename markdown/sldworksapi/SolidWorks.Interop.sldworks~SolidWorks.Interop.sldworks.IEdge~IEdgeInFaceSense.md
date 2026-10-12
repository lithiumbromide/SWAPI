---
title: "IEdgeInFaceSense Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "IEdgeInFaceSense"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEdgeInFaceSense.html"
---

# IEdgeInFaceSense Method (IEdge)

Obsolete. Superseded by [IEdge::IEdgeInFaceSense2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IEdgeInFaceSense2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IEdgeInFaceSense( _
   ByVal Facedisp As Face _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim Facedisp As Face
Dim value As System.Boolean

value = instance.IEdgeInFaceSense(Facedisp)
```

### C#

```csharp
System.bool IEdgeInFaceSense(
   Face Facedisp
)
```

### C++/CLI

```cpp
System.bool IEdgeInFaceSense(
   Face^ Facedisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Facedisp`:

## VBA Syntax

See [Edge::IEdgeInFaceSense](ms-its:sldworksapivb6.chm::/sldworks~Edge~IEdgeInFaceSense.html).

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
