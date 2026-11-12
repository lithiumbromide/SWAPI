---
title: "IConvertLineToBcurveSize Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IConvertLineToBcurveSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertLineToBcurveSize.html"
---

# IConvertLineToBcurveSize Method (ICurve)

Converts the specified line into a b-spline curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function IConvertLineToBcurveSize( _
   ByRef StartPoint As System.Double, _
   ByRef EndPoint As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim StartPoint As System.Double
Dim EndPoint As System.Double
Dim value As System.Integer

value = instance.IConvertLineToBcurveSize(StartPoint, EndPoint)
```

### C#

```csharp
System.int IConvertLineToBcurveSize(
   ref System.double StartPoint,
   ref System.double EndPoint
)
```

### C++/CLI

```cpp
System.int IConvertLineToBcurveSize(
   System.double% StartPoint,
   System.double% EndPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartPoint`: Array values for the coordinates of the start point of the line
- `EndPoint`: Array values for the coordinates of the end point of the line

### Return Value

Array giving the b-spline representation of the line

## VBA Syntax

See [Curve::IConvertLineToBcurveSize](ms-its:sldworksapivb6.chm::/sldworks~Curve~IConvertLineToBcurveSize.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.html)
[ICurve::ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.html)
[ICurve::IsLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.html)
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.html)
[ICurve::IConvertArcToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertArcToBcurveSize.html)
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.html)
[ICurve::GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.html)
[ICurve::ExtentCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ExtentCurve.html)
[ICurve::IGetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.html)
[ICurve::IGetBCurveParamsSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize2.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.html)
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.html)
