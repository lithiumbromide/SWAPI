---
title: "IGetBCurveParamsSize2 Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IGetBCurveParamsSize2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize2.html"
---

# IGetBCurveParamsSize2 Method (ICurve)

Obsolete. Superseded by [ICurve::IGetBCurveParamsSize3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetBCurveParamsSize3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBCurveParamsSize2( _
   ByVal WantCubic As System.Boolean, _
   ByVal WantNRational As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim WantCubic As System.Boolean
Dim WantNRational As System.Boolean
Dim value As System.Integer

value = instance.IGetBCurveParamsSize2(WantCubic, WantNRational)
```

### C#

```csharp
System.int IGetBCurveParamsSize2(
   System.bool WantCubic,
   System.bool WantNRational
)
```

### C++/CLI

```cpp
System.int IGetBCurveParamsSize2(
   System.bool WantCubic,
   System.bool WantNRational
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubic`: True for cubic curves, false if not
- `WantNRational`: True for non-rational curves, false if not

### Return Value

Size of the data set returned by [ICurve::IGetBCurveParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetBCurveParams.html).

## VBA Syntax

See [Curve::IGetBCurveParamsSize2](ms-its:sldworksapivb6.chm::/sldworks~Curve~IGetBCurveParamsSize2.html).

## Examples

[Get Curve Spline Points (C++)](Get_Curve_Spline_Points_Example_CPlusPlus_COM.htm)

## Remarks

Use this method to control the type of information returned in the subsequent call to [ICurve::IGetBCurveParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetBCurveParams.html).

To control the accuracy of the curve data, use [IModeler::SetToleranceValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~SetToleranceValue.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.html)
[ICurve::IGetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.html)
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.html)
