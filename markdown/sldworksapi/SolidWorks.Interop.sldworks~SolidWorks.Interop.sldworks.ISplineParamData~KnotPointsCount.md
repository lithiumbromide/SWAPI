---
title: "KnotPointsCount Property (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "KnotPointsCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~KnotPointsCount.html"
---

# KnotPointsCount Property (ISplineParamData)

Gets the number of knots in the spline.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property KnotPointsCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim value As System.Integer

value = instance.KnotPointsCount
```

### C#

```csharp
System.int KnotPointsCount {get;}
```

### C++/CLI

```cpp
property System.int KnotPointsCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of knots.

## VBA Syntax

See [SplineParamData::KnotPointsCount](ms-its:sldworksapivb6.chm::/sldworks~SplineParamData~KnotPointsCount.html).

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

The number of knots depends on the periodicity of the spline:

| If... | Then this method returns... |
| --- | --- |
| periodic =1 | control points count + 1 |
| periodic =0 | control points count + order |

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html)
[ISplineParamData::GetKnotPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetKnotPoints.html)
[ISplineParamData::IGetKnotPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetKnotPoints.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
