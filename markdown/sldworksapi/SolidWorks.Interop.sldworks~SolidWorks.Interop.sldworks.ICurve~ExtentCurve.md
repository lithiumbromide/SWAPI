---
title: "ExtentCurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "ExtentCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ExtentCurve.html"
---

# ExtentCurve Method (ICurve)

Extends a b-spline curve by the specified length.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExtentCurve( _
   ByVal AtStart As System.Boolean, _
   ByVal Length As System.Double, _
   ByVal LinearExt As System.Boolean _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim AtStart As System.Boolean
Dim Length As System.Double
Dim LinearExt As System.Boolean
Dim value As Curve

value = instance.ExtentCurve(AtStart, Length, LinearExt)
```

### C#

```csharp
Curve ExtentCurve(
   System.bool AtStart,
   System.double Length,
   System.bool LinearExt
)
```

### C++/CLI

```cpp
Curve^ ExtentCurve(
   System.bool AtStart,
   System.double Length,
   System.bool LinearExt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtStart`: True to extend b-spline curve from start point, false to extend b-spline curve from end point
- `Length`: Length by which to extend b-spline curve
- `LinearExt`: True if the extension is linear, false if not

### Return Value

Pointer to newly extended [ICurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) object

## VBA Syntax

See [Curve::ExtentCurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~ExtentCurve.html).

## Remarks

This method only affects b-spline curves. For all other types of curves, this method does nothing.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::CreateTrimmedCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.html)
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.html)
[ICurve::IJoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IJoinCurves.html)
[ICurve::JoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves.html)
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.html)
[ICurve::ReverseCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseCurve.html)
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
