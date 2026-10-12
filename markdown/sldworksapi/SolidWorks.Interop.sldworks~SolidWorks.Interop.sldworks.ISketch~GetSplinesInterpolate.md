---
title: "GetSplinesInterpolate Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSplinesInterpolate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.html"
---

# GetSplinesInterpolate Method (ISketch)

Gets the spline points by interpolation instead of by tessellation as is done by [ISketch::GetSplines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSplines.html) and [ISketch::IGetSplines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSplines.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplinesInterpolate() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetSplinesInterpolate()
```

### C#

```csharp
System.object GetSplinesInterpolate()
```

### C++/CLI

```cpp
System.Object^ GetSplinesInterpolate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Sketch::GetSplinesInterpolate](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSplinesInterpolate.html).

## Examples

[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)

## Remarks

The return value is an array of doubles formatted as:

[ [NumSplinePoints, [x, y, z] ], ]

This complete set of data repeats itself for each spline found in the sketch. For each spline, the array returned contains the number of spline points in the spline, and the X,Y,Z value for each of those points.

The [x,y,z] parameter is an array of NumSplinePoints. For example, if your sketch has two splines and each spline has three points, then the data would be in the following format:

[ 3, x1_1, y1_1, z1_1, x2_1, y2_1, z2_1, x3_1, y3_1, z3_1, 3, x1_2, y1_2, z1_2, x2_2, y2_2, z2_2, x3_2, y3_2, z3_2 ]

The [x,y,z] points for each spline are the same points used to generate the spline.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.html)
[ISketch::GetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams2.html)
[ISketch::GetSplineParamsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount2.html)
[ISketch::IGetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplineParams2.html)
[ISketch::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.html)
[ISketch::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.html)
