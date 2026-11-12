---
title: "Identity Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "Identity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html"
---

# Identity Method (ICurve)

Gets the type of curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function Identity() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Integer

value = instance.Identity()
```

### C#

```csharp
System.int Identity()
```

### C++/CLI

```cpp
System.int Identity();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of curve as defined in [swCurveTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCurveTypes_e.html)

## VBA Syntax

See [Curve::Identity](ms-its:sldworksapivb6.chm::/sldworks~Curve~Identity.html).

## Examples

[Get Length of Edge (VBA)](Get_Length_of_Edge_Example_VB.htm)
[Get Length of Spline or Elliptical Edge (VBA)](Get_Length_of_Spline_or_Elliptical_Edge_Example_VB.htm)

## Remarks

If the return value is TRIMMED_TYPE, then the original untrimmed curve type may be established by calling [ICurve::IsLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IsLine.html), [ICurve::IsBcurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IsBcurve.html) or [ICurve::IsCircle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IsCircle.html).

To determine if a circular edge is a complete circle or an arc, see [IEdge::GetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetCurveParams2.html) or [IEdge::IGetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetCurveParams2.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::IsEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsEllipse.html)
[ICurve::IsTrimmedCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsTrimmedCurve.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)
[ICurve::IsCircle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsCircle.html)
[ICurve::IsLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.html)
