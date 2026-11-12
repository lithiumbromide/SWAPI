---
title: "Order Property (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "Order"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Order.html"
---

# Order Property (ISplineParamData)

Gets and sets the number of nearby control points that influence any given point on the curve.

## Syntax

### Visual Basic (Declaration)

```vb
Property Order As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim value As System.Integer

instance.Order = value

value = instance.Order
```

### C#

```csharp
System.int Order {get; set;}
```

### C++/CLI

```cpp
property System.int Order {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

The degree of the spline polynomial + 1

## VBA Syntax

See [SplineParamData::Order](ms-its:sldworksapivb6.chm::/sldworks~SplineParamData~Order.html).

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

| A spline of order... | is represented by a ... | of degree... |
| --- | --- | --- |
| 2 | linear polynomial | 1 |
| 3 | quadratic polynomial | 2 |
| 4 | cubic polynomial | 3 |

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html)
[ISplineParamData::GetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetSegments.html)
[ISplineParamData::IGetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetSegments.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
