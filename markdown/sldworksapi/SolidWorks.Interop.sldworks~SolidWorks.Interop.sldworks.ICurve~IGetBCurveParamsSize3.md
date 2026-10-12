---
title: "IGetBCurveParamsSize3 Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IGetBCurveParamsSize3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize3.html"
---

# IGetBCurveParamsSize3 Method (ICurve)

Gets the b-curve size.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBCurveParamsSize3( _
   ByVal WantCubicIn As System.Boolean, _
   ByVal WantNRational As System.Boolean, _
   ByVal ForceNonPeriodic As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim WantCubicIn As System.Boolean
Dim WantNRational As System.Boolean
Dim ForceNonPeriodic As System.Boolean
Dim value As System.Integer

value = instance.IGetBCurveParamsSize3(WantCubicIn, WantNRational, ForceNonPeriodic)
```

### C#

```csharp
System.int IGetBCurveParamsSize3(
   System.bool WantCubicIn,
   System.bool WantNRational,
   System.bool ForceNonPeriodic
)
```

### C++/CLI

```cpp
System.int IGetBCurveParamsSize3(
   System.bool WantCubicIn,
   System.bool WantNRational,
   System.bool ForceNonPeriodic
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubicIn`: True for cubic curves, false if not
- `WantNRational`: True for non-rational curves, false if not
- `ForceNonPeriodic`: True converts the curve to nonperiodic and returns parameters, false does not

### Return Value

Size of the data set returned by [ICurve::IGetBCurveParams3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetBCurveParams3.html)

## VBA Syntax

See [Curve::IGetBCurveParamsSize3](ms-its:sldworksapivb6.chm::/sldworks~Curve~IGetBCurveParamsSize3.html).

## Remarks

Use this method to control the type of information returned in the subsequent call to [ICurve::IGetBCurveParams3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetBCurveParams3.html).

To control the accuracy of the curve data, see [IModeler::SetToleranceValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~SetToleranceValue.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::GetBCurveParams3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams3.html)

## Availability

SOLIDWORKS 2007 SP5, Revision Number 15.5
