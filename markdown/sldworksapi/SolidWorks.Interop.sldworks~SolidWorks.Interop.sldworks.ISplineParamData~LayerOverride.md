---
title: "LayerOverride Property (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "LayerOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~LayerOverride.html"
---

# LayerOverride Property (ISplineParamData)

Gets the spline's properties that override the default properties of the layer.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LayerOverride As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim value As System.Integer

value = instance.LayerOverride
```

### C#

```csharp
System.int LayerOverride {get;}
```

### C++/CLI

```cpp
property System.int LayerOverride {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Properties that have been overridden or should be overridden as defined in [swLayerOverride_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLayerOverride_e.html) (see Remarks)

## VBA Syntax

See [SplineParamData::LayerOverride](ms-its:sldworksapivb6.chm::/sldworks~SplineParamData~LayerOverride.html).

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

Layers are only supported in drawing documents.

Splines can be created on a layer that has specific visual properties. By default, the spline takes on the visual properties defined by the layer. However, for a specific spline, these visual properties can be overridden (see [ISplineParamData::Color](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Color.html), [ISplineParamData::LineStyle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~LineStyle.html), and [ISplineParamData::LineWidth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~LineWidth.html)). This property gets or sets whether the default visual properties of the layer are used by this spline.

When the spline is not on any layer, the value this property returns is undefined. You can use the [ISplineParamData::Layer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Layer.html) property to determine the name of the layer, if any, that this spline is on. If an empty string is returned by the ISplineParamData::Layer property, then this property is not used.

When you get this property, the returned bit value indicates which property or properties have been overridden. The bit indicators are:

Therefore, if the value was returned as 3, you know color and style have been specifically set for this item and might not match the default values associated with this item's layer.

When you set this property, the input bit value indicates which property or properties should maintain their current override values. Therefore, if the value is passed as 0x4, we know width should keep its current override value, and that color and style should be reset to use the color and style settings for the item's layer. If you pass 0, all visual properties are reset to use the default settings of the item's layer.

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html)
[ISplineParamData::Layer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Layer.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
