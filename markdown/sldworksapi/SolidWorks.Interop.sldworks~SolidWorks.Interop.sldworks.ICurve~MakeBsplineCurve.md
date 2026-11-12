---
title: "MakeBsplineCurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "MakeBsplineCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.html"
---

# MakeBsplineCurve Method (ICurve)

Obsolete. Superseded by [ICurve::MakeBsplineCurve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~MakeBsplineCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeBsplineCurve() As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As Curve

value = instance.MakeBsplineCurve()
```

### C#

```csharp
Curve MakeBsplineCurve()
```

### C++/CLI

```cpp
Curve^ MakeBsplineCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [arc or line](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Curve::MakeBsplineCurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~MakeBsplineCurve.html).

## Remarks

To convert the arc or line to a b-spline curve, use any of these methods:

- [ICurve::ConvertArcToBcurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~ConvertArcToBcurve.html)
- [ICurve::ConvertLineToBcurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~ConvertLineToBcurve.html)
- [ICurve::GetBCurveParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetBCurveParams.html) or [ICurve::IGetBCurveParmas](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetBCurveParams.html)

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
