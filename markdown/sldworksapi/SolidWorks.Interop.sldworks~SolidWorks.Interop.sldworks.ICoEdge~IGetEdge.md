---
title: "IGetEdge Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "IGetEdge"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetEdge.html"
---

# IGetEdge Method (ICoEdge)

Gets the edge that corresponds to this coedge.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEdge() As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
Dim value As Edge

value = instance.IGetEdge()
```

### C#

```csharp
Edge IGetEdge()
```

### C++/CLI

```cpp
Edge^ IGetEdge();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) that corresponds to this coedge

## VBA Syntax

See [CoEdge::IGetEdge](ms-its:sldworksapivb6.chm::/sldworks~CoEdge~IGetEdge.html).

## See Also

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[ICoEdge::GetEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetEdge.html)
