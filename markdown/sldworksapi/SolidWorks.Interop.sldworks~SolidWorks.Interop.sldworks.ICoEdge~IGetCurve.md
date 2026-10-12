---
title: "IGetCurve Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "IGetCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurve.html"
---

# IGetCurve Method (ICoEdge)

Gets the underlying curve of this coedge if the coedge is a result of imprecisely sewing two surfaces together.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCurve() As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
Dim value As Curve

value = instance.IGetCurve()
```

### C#

```csharp
Curve IGetCurve()
```

### C++/CLI

```cpp
Curve^ IGetCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the curve that is attached to this coedge (see **Remarks**)

## VBA Syntax

See [CoEdge::IGetCurve](ms-its:sldworksapivb6.chm::/sldworks~CoEdge~IGetCurve.html).

## Remarks

This method may return NULL if no geometry is attached to the coedge. The edge may still be accurate, and you can obtain the geometry from the edge using:

- [ICoEdge::IGetEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~IGetEdge.html)
- [IEdge::IGetCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetCurve.html)

## See Also

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[ICoEdge::GetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurve.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
