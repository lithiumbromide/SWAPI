---
title: "Color Property (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "Color"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Color.html"
---

# Color Property (ISplineParamData)

Gets the color used to draw the spline.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Color As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim value As System.Integer

value = instance.Color
```

### C#

```csharp
System.int Color {get;}
```

### C++/CLI

```cpp
property System.int Color {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

COLORREF value; -1 if not defined

## VBA Syntax

See [SplineParamData::Color](ms-its:sldworksapivb6.chm::/sldworks~SplineParamData~Color.html).

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

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html)
[ISplineParamData::LayerOverride Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~LayerOverride.html)
[ISplineParamData::LineStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~LineStyle.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
