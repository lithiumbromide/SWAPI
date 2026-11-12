---
title: "GetSplineCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSplineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.html"
---

# GetSplineCount Method (ISketch)

Gets the number of splines in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplineCount( _
   ByRef PointCount As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim PointCount As System.Integer
Dim value As System.Integer

value = instance.GetSplineCount(PointCount)
```

### C#

```csharp
System.int GetSplineCount(
   ref System.int PointCount
)
```

### C++/CLI

```cpp
System.int GetSplineCount(
   System.int% PointCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointCount`: Number of points in this sketch

### Return Value

Number of splines in the sketch

## VBA Syntax

See [Sketch::GetSplineCount](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSplineCount.html).

## Examples

[Get Each Spline's Parameters (C#)](Get_Each_Splines_Parameters_Example_CSharp.htm)
[Get Each Spline's Parameters (VB.NET)](Get_Each_Splines_Parameters_Example_VBNET.htm)
[Get Each Spline's Parameters (VBA)](Get_Each_Splines_Parameters_Example_VB.htm)

## Remarks

Call this method before calling [ISketch::IGetSplines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSplines.html) to get the size of the array for that method.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.html)
[ISketch::GetSplineParamsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount2.html)
[ISketch::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.html)
[ISketch::GetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams2.html)
[ISketch::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.html)
[ISketch::IGetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplineParams2.html)
[ISketch::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.html)
