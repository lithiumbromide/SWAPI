---
title: "GetSplinePts Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "GetSplinePts"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetSplinePts.html"
---

# GetSplinePts Method (ICurve)

Gets the spline points for this curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplinePts( _
   ByVal ParamsArrayIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim ParamsArrayIn As System.Object
Dim value As System.Object

value = instance.GetSplinePts(ParamsArrayIn)
```

### C#

```csharp
System.object GetSplinePts(
   System.object ParamsArrayIn
)
```

### C++/CLI

```cpp
System.Object^ GetSplinePts(
   System.Object^ ParamsArrayIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParamsArrayIn`: Array containing the definition of the spline

### Return Value

Array containing the spline points

## VBA Syntax

See [Curve::GetSplinePts](ms-its:sldworksapivb6.chm::/sldworks~Curve~GetSplinePts.html).

## Examples

[Get Curve Spline Points (VBA)](Get_Curve_Spline_Points_Example_VB.htm)
[Get Length of Spline or Elliptical Edge (VBA)](Get_Length_of_Spline_or_Elliptical_Edge_Example_VB.htm)
[Get Parameters and Spline Points for Curve (VBA)](Get_Parameters_and_Spline_Points_for_Curve_Example_VB.htm)

## Remarks

For OLE Automation applications, the ParamsIn argument contains an array defining the spline. This array contains the values for propArray, knotsArray and cntrlPntCoordArray, all packed into a single array (propArray is packed as four integers into the first two elements of the array.) The contents of these arrays is described in [ICurve::IGetSplinePtsSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetSplinePtsSize.html).

The array returned contains the x, y, z location of the spline points:

**[** `x1, y1, z1, x2, y2, z2`,....**]**

Data passed into this method must satisfy the following requirements:

- If the curve is periodic, it must not have any repeated knots.
- If the curve is non-periodic, it must only have repeated knots at its ends.
- The curve must be cubic or lower degree, non-rational, and have continuous first
  and second derivatives.

**NOTE:** For a linear or quadratic curve to satisfy these continuity requirements, it must consist of a single segment.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::IGetSplinePts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePts.html)
