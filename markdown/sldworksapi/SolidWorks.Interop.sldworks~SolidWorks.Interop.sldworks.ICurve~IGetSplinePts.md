---
title: "IGetSplinePts Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IGetSplinePts"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetSplinePts.html"
---

# IGetSplinePts Method (ICurve)

Gets the spline points for this curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSplinePts() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Double

value = instance.IGetSplinePts()
```

### C#

```csharp
System.double IGetSplinePts()
```

### C++/CLI

```cpp
System.double IGetSplinePts();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array containing the spline points

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Examples

[Get Curve Spline Points (C++)](Get_Curve_Spline_Points_Example_CPlusPlus_COM.htm)

## Remarks

[ICurve::IGetSplinePtsSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~IGetSplinePtsSize.html) defines the spline and determines the size of the array returned.

The array returned contains the x, y, z location of the spline points:

**[** `x1, y1, z1, x2, y2, z2`,....**]**

Data passed into ICurve::IGetSplinePtsSize must satisfy the following requirements:

- If the curve is periodic, it must not have any repeated knots.
- If the curve is non-periodic, it must only have repeated knots at its ends.
- The curve must be cubic or lower degree, non-rational, and have continuous first
  and second derivatives.

**NOTE:** For a linear or quadratic curve to satisfy these continuity requirements, it must consist of a single segment.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::GetSplinePts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetSplinePts.html)
