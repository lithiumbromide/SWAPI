---
title: "MakeBsplineCurve2 Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "MakeBsplineCurve2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve2.html"
---

# MakeBsplineCurve2 Method (ICurve)

Creates a b-spline curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeBsplineCurve2() As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As Curve

value = instance.MakeBsplineCurve2()
```

### C#

```csharp
Curve MakeBsplineCurve2()
```

### C++/CLI

```cpp
Curve^ MakeBsplineCurve2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

B-spline [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Curve::MakeBsplineCurve2](ms-its:sldworksapivb6.chm::/sldworks~Curve~MakeBsplineCurve2.html).

## Remarks

This method uses the input curve as it is and allows lines and arcs.

To convert the arc or line to a b-spline, use any of these methods:

- [ICurve::ConvertArcToBcurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~ConvertArcToBcurve.html)
- [ICurve::ConvertLineToBcurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~ConvertLineToBcurve.html)
- [ICurve::GetBCurveParams3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetBCurveParams3.html) and [ICurve::IGetBCurveParams3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetBCurveParams3.html)

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::CreateTrimmedCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.html)
[ICurve::ExtentCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ExtentCurve.html)
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.html)
[ICurve::IJoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IJoinCurves.html)
[ICurve::JoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves.html)
[ICurve::IReverseCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IReverseCurve.html)
[ICurve::ReverseCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseCurve.html)
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
