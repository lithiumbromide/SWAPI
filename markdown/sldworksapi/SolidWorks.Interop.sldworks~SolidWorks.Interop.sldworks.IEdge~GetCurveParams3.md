---
title: "GetCurveParams3 Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "GetCurveParams3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams3.html"
---

# GetCurveParams3 Method (IEdge)

Gets a data object containing the curve parameters for this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurveParams3() As CurveParamData
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As CurveParamData

value = instance.GetCurveParams3()
```

### C#

```csharp
CurveParamData GetCurveParams3()
```

### C++/CLI

```cpp
CurveParamData^ GetCurveParams3();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

An

[ICurveParamData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveParamData.html)

object

## VBA Syntax

See

[Edge::GetCurveParams3](ms-its:sldworksapivb6.chm::/sldworks~Edge~GetCurveParams3.html)

.

## Examples

[Get Edge Curve Parameterization (C#)](Get_Edge_Curve_Parameterization_Example_CSharp.htm)

[Get Edge Curve Parameterization (VB.NET)](Get_Edge_Curve_Parameterization_Example_VBNET.htm)

[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)

## Remarks

Before calling this method, you must call[IEdge::GetCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetCurve.html)togenerate the underlying curve information.

You can use the data returned by this method to determine if a circular edge is a complete circle or an arc.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)

[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)

[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.html)

[IEdge::IsParamReversed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IsParamReversed.html)

[ICurve::GetBCurveParams5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams5.html)

[ICurve::GetPCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams2.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
