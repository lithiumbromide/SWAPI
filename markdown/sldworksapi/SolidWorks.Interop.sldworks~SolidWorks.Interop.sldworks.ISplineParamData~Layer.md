---
title: "Layer Property (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "Layer"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Layer.html"
---

# Layer Property (ISplineParamData)

Gets the index of the layer in which this spline is drawn.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Layer As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim value As System.Integer

value = instance.Layer
```

### C#

```csharp
System.int Layer {get;}
```

### C++/CLI

```cpp
property System.int Layer {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Index of layer of spline, -1 if layer not defined

## VBA Syntax

See [SplineParamData::Layer](ms-its:sldworksapivb6.chm::/sldworks~SplineParamData~Layer.html).

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

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
