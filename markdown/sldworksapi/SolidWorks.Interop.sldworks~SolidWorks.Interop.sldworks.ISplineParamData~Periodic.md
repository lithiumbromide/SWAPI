---
title: "Periodic Property (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "Periodic"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Periodic.html"
---

# Periodic Property (ISplineParamData)

Gets and sets the periodicity of the spline.

## Syntax

### Visual Basic (Declaration)

```vb
Property Periodic As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim value As System.Integer

instance.Periodic = value

value = instance.Periodic
```

### C#

```csharp
System.int Periodic {get; set;}
```

### C++/CLI

```cpp
property System.int Periodic {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 if an open spline, 1 if a closed spline

## VBA Syntax

See [SplineParamData::Periodic](ms-its:sldworksapivb6.chm::/sldworks~SplineParamData~Periodic.html).

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

The [number of knots](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~KnotPointsCount.html) in the spline depends on the periodicity of the spline:

| If this method returns... | Then the number of knots is... |
| --- | --- |
| 1 | ControlPointsCount + 1 |
| 0 | ControlPointsCount + Order |

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
