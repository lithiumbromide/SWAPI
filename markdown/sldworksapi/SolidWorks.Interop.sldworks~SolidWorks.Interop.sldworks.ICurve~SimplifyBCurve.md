---
title: "SimplifyBCurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "SimplifyBCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.html"
---

# SimplifyBCurve Method (ICurve)

Simplifies a b-curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function SimplifyBCurve( _
   ByVal TolIn As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim TolIn As System.Double
Dim value As Curve

value = instance.SimplifyBCurve(TolIn)
```

### C#

```csharp
Curve SimplifyBCurve(
   System.double TolIn
)
```

### C++/CLI

```cpp
Curve^ SimplifyBCurve(
   System.double TolIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TolIn`: Tolerance

### Return Value

Pointer to simplified [b-curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Curve::SimplifyBCurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~SimplifyBCurve.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.html)
[ICurve::ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.html)
[ICurve::ExtentCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ExtentCurve.html)
[ICurve::GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.html)
[ICurve::IConvertArcToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertArcToBcurveSize.html)
[ICurve::IConvertLineToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertLineToBcurveSize.html)
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.html)
[ICurve::IGetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.html)
[ICurve::IGetBCurveParamsSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize2.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)

## Availability

SOLIDWORKS 2006 FCS, revision Number 14.0
