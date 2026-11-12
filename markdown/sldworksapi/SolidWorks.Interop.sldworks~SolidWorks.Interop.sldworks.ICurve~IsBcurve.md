---
title: "IsBcurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IsBcurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html"
---

# IsBcurve Method (ICurve)

Gets whether the curve is a b-spline curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsBcurve() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Boolean

value = instance.IsBcurve()
```

### C#

```csharp
System.bool IsBcurve()
```

### C++/CLI

```cpp
System.bool IsBcurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if curve is a b-spline curve, false if other curve type

## VBA Syntax

See [Curve::IsBcurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~IsBcurve.html).

## Remarks

This method returns True if the curve is an intersection curve, ellipse, trimming curve, or a surface parametric curve. Because intersection and trimming curves can be lines or circles, it is advisable to first determine whether the curve is a circle or line before recognizing it as a b-curve.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.html)
[ICurve::GetSplinePts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetSplinePts.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)
[ICurve::IGetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.html)
[ICurve::IGetBCurveParamsSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize2.html)
[ICurve::IGetSplinePts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePts.html)
[ICurve::IGetSplinePtsSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePtsSize.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.html)
