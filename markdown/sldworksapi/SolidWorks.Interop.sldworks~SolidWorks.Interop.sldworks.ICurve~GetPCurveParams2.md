---
title: "GetPCurveParams2 Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "GetPCurveParams2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams2.html"
---

# GetPCurveParams2 Method (ICurve)

Gets the piecewise polynomial parameterization data for this curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPCurveParams2() As SplineParamData
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As SplineParamData

value = instance.GetPCurveParams2()
```

### C#

```csharp
SplineParamData GetPCurveParams2()
```

### C++/CLI

```cpp
SplineParamData^ GetPCurveParams2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

An [ISplineParamData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData.html) object

## VBA Syntax

See [Curve::GetPCurveParam2](ms-its:sldworksapivb6.chm::/sldworks~Curve~GetPCurveParams2.html).

## Examples

[Get P-Spline Parameterization Data (C#)](Get_P-Spline_Parameterization_Data_Example_CSharp.htm)
[Get P-Spline Parameterization Data (VB.NET)](Get_P-Spline_Parameterization_Data_Example_VBNET.htm)
[Get P-Spline Parameterization Data (VBA)](Get_P-Spline_Parameterization_Data_Example_VB.htm)

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)
[ICurve::IGetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParams.html)
[ICurve::IGetPCurveParamsSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParamsSize.html)
[ICurve::GetBCurveParams5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams5.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
