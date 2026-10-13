---
title: "GetCurve Method (ICoEdge)"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: "GetCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurve.html"
---

# GetCurve Method (ICoEdge)

Gets the underlying curve of this coedge if the coedge is a result of imprecisely sewing two surfaces together.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
Dim value As System.Object

value = instance.GetCurve()
```

### C#

```csharp
System.object GetCurve()
```

### C++/CLI

```cpp
System.Object^ GetCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Curve that is attached to this coedge (see **Remarks**)

## VBA Syntax

See [CoEdge::GetCurve](ms-its:sldworksapivb6.chm::/sldworks~CoEdge~GetCurve.html).

## Remarks

This method may return Nothing if no geometry is attached to the coedge. The edge may still be accurate, and you can obtain the geometry from the edge using:

- [ICoEdge::GetEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~GetEdge.html)
- [IEdge::GetCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetCurve.html)

## See Also

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[ICoEdge::IGetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurve.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
