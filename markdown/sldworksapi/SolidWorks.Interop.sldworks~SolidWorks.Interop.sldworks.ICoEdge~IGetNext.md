---
title: "IGetNext Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "IGetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetNext.html"
---

# IGetNext Method (ICoEdge)

Gets the next coedge from the current coedge.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNext() As CoEdge
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
Dim value As CoEdge

value = instance.IGetNext()
```

### C#

```csharp
CoEdge IGetNext()
```

### C++/CLI

```cpp
CoEdge^ IGetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [coedge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge.html) from the current coedge

## VBA Syntax

See [CoEdge::IGetNext](ms-its:sldworksapivb6.chm::/sldworks~CoEdge~IGetNext.html).

## Remarks

This method is cyclical; it loops back on itself and does not return NULL.

## See Also

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[ICoEdge::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetNext.html)
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.html)
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.html)
[ILoop2::GetCoEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdgeCount.html)
[ILoop2::GetCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdges.html)
[ILoop2::IGetCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetCoEdges.html)
