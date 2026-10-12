---
title: "GetControlPoints Method (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "GetControlPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetControlPoints.html"
---

# GetControlPoints Method (ISplineParamData)

Gets the coordinates of all of the control points of the spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetControlPoints( _
   ByRef ControlPoints As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim ControlPoints As System.Object
Dim value As System.Boolean

value = instance.GetControlPoints(ControlPoints)
```

### C#

```csharp
System.bool GetControlPoints(
   out System.object ControlPoints
)
```

### C++/CLI

```cpp
System.bool GetControlPoints(
   [Out] System.Object^ ControlPoints
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ControlPoints`: One-dimensional array of doubles (**see Remarks**)

### Return Value

True if successful, false if not

## VBA Syntax

See [SplineParamData::GetControlPoints](ms-its:sldworksapivb6.chm::/sldworks~SplineParamData~GetControlPoints.html).

## Examples

[Get BCurve Spline Points (C#)](Get_BCurve_Spline_Points_Example_CSharp.htm)
[Get BCurve Spline Points (VB.NET)](Get_BCurve_Spline_Points_Example_VBNET.htm)
[Get BCurve Spline Points (VBA)](Get_BCurve_Spline_Points_Example_VB.htm)
[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

## Remarks

Control points determine the shape of a spline or curve. Starting with a set of control points, all other points of a spline can be calculated. A given point on the spline is calculated using the polynomial basis functions of its nearest control points. The [knot vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~GetKnotPoints.html) determines which control point basis functions are in force for calculating each point along a curve.

The size of the ControlPoints array is based on the curve dimension:

- if [dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Dimension.html) = 2, then each control point has 2 doubles ( x, y )
- if [dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Dimension.html) = 3, then each control point has 3 doubles ( x, y, z )
- if [dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Dimension.html) = 4, and the curve is closed or periodic, then each control point has 4 doubles ( x, y, z, w ), where w = weight
- if [dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Dimension.html) = 4, and the curve is open or non-periodic, then each control point has 4 doubles ( w*x, w*y, w*z, w ), where w = weight

Size of ControlPoints array = [control points count](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~ControlPointsCount.html) * [dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~Dimension.html)

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html)
[ISplineParamData::IGetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetControlPoints.html)
[ISplineParamData::SetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~SetControlPoints.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
