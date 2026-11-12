---
title: "IGetBCurveParams Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IGetBCurveParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.html"
---

# IGetBCurveParams Method (ICurve)

Obsolete. Superseded by [ICurve::IGetBCurveParams3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetBCurveParams3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBCurveParams() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Double

value = instance.IGetBCurveParams()
```

### C#

```csharp
System.double IGetBCurveParams()
```

### C++/CLI

```cpp
System.double IGetBCurveParams();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to an array of doubles describing the parameters of the curve (see **Remarks**)

## VBA Syntax

See [Curve::IGetBCurveParams](ms-its:sldworksapivb6.chm::/sldworks~Curve~IGetBCurveParams.html).

## Examples

[Get Curve Spline Points (C++)](Get_Curve_Spline_Points_Example_CPlusPlus_COM.htm)

## Remarks

Call [ICurve::IGetBCurveParamsSize2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetBCurveParamsSize2.html) to determine the size of the array returned and whether the curve data returned by ICurve::IGetBCurveParams is cubic rational or not.

To control the accuracy of the curve data, see [IModeler::SetToleranceValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~SetToleranceValue.html).

The return value is an array of doubles. The array size is ( 2 + numKnots + numControlPointDoubles) where numKnots is (numControlPoints + order). The array is as follows:

**[** `packedDouble1, packedDouble2, knot1, knot2,..., ControlPoint1[Dimension], ControlPoint2[Dimension],...` **]**

where:

- `packedDouble1` is an integer pair containing the `Dimension` and `Order`
- `packedDouble2` is an integer pair containing the `NumControlPoints` and `Periodicity`
- `knot1`
- `knot2`

...

- `ControlPoint1[dimension]`
- `ControlPoint2[dimension]`

...

The size of the control point array is based on the curve dimension:

- If `Dimension` = 3, then `ControlPoint` is an array of 3 doubles ( x, y, z )
- If `Dimension` = 4, then `ControlPoint` is an array of 4 doubles ( x, y, z, w ) where
  w = weight

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.html)
[ICurve::ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.html)
[ICurve::ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.html)
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)
[ICurve::IConvertArcToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertArcToBcurveSize.html)
[ICurve::IConvertLineToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertLineToBcurveSize.html)
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.html)
