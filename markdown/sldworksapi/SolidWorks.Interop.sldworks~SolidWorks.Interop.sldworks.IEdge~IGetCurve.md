---
title: "IGetCurve Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "IGetCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurve.html"
---

# IGetCurve Method (IEdge)

Gets the underlying curve for this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCurve() As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
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

Pointer to the underlying [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) for this edge

## VBA Syntax

See [Edge::IGetCurve](ms-its:sldworksapivb6.chm::/sldworks~Edge~IGetCurve.html).

## Examples

[Get Circular Holes in Face (C++)](Get_Circular_Holes_In_Face_Example_CPlusPlus_COM.htm)

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::GetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurve.html)
[ICoEdge::GetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurve.html)
[ICoEdge::IGetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurve.html)
[ICoEdge::GetEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetEdge.html)
[ICoEdge::IGetEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetEdge.html)
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.html)
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.html)
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.html)
[IEdge::IGetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.html)
