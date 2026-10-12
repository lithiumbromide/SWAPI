---
title: "GetKnotPoints Method (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "GetKnotPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetKnotPoints.html"
---

# GetKnotPoints Method (ISplineParamData)

Gets the knot vector for the spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetKnotPoints( _
   ByRef KnotPoints As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim KnotPoints As System.Object
Dim value As System.Boolean

value = instance.GetKnotPoints(KnotPoints)
```

### C#

```csharp
System.bool GetKnotPoints(
   out System.object KnotPoints
)
```

### C++/CLI

```cpp
System.bool GetKnotPoints(
   [Out] System.Object^ KnotPoints
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `KnotPoints`: Array of double values between 0 and 1, inclusive (**see Remarks**)

### Return Value

True if successful, false if not

## VBA Syntax

See [SplineParamData::GetKnotPoints](ms-its:sldworksapivb6.chm::/sldworks~SplineParamData~GetKnotPoints.html).

## Examples

[Get BCurve Spline Points (C#)](Get_BCurve_Spline_Points_Example_CSharp.htm)
[Get BCurve Spline Points (VB.NET)](Get_BCurve_Spline_Points_Example_VBNET.htm)
[Get BCurve Spline Points (VBA)](Get_BCurve_Spline_Points_Example_VB.htm)
[Get P-Spline Parameterization Data (C#)](Get_P-Spline_Parameterization_Data_Example_CSharp.htm)
[Get P-Spline Parameterization Data (VB.NET)](Get_P-Spline_Parameterization_Data_Example_VBNET.htm)
[Get P-Spline Parameterization Data (VBA)](Get_P-Spline_Parameterization_Data_Example_VB.htm)
[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

## Remarks

Before calling this method, call [ISplineParamData::KnotPointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~KnotPointsCount.html) to get the size of the KnotPoints array.

Together with [control points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~GetControlPoints.html), knots determine the shape and smoothness of a spline. The knot vector divides the parametric space into intervals or knot spans. These intervals may be uniform or non-uniform. Each interval governs a different control point.

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html)
[ISplineParamData::IGetKnotPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetKnotPoints.html)
[ISplineParamData::SetKnotPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~SetKnotPoints.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
