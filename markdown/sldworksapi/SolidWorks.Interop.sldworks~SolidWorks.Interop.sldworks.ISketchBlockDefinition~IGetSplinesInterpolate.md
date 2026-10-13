---
title: "IGetSplinesInterpolate Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "IGetSplinesInterpolate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplinesInterpolate.html"
---

# IGetSplinesInterpolate Method (ISketchBlockDefinition)

Gets all of the parameers of the splines by interpolation instead of by tessellation as is done by [ISketch::GetSplines2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetSplines2.html) and [ISketch::IGetSplines2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSplinesInterpolate( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim ArraySize As System.Integer
Dim value As System.Double

value = instance.IGetSplinesInterpolate(ArraySize)
```

### C#

```csharp
System.double IGetSplinesInterpolate(
   System.int ArraySize
)
```

### C++/CLI

```cpp
System.double IGetSplinesInterpolate(
   System.int ArraySize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArraySize`: Number of elements in the return array

## VBA Syntax

See [SketchBlockDefinition::IGetSplinesInterpolate](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~IGetSplinesInterpolate.html).

## Remarks

Call [ISketchBlockDefinition::GetSplineInterpolateCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetSplineInterpolateCount.html) before calling this method to get the value for ArraySize.

The return value is an array of doubles formatted as:

[ [NumSplinePoints, [x, y, z] ], ]

This complete set of data repeats itself for each spline found in the sketch block definition. For each spline, the array returned contains the number of spline points in the spline, and the X,Y,Z value for each of those points.

The [x,y,z] parameter is an array of NumSplinePoints. For example, if your sketch block definition has two splines and each spline has three points, then the data would be in the following format:

[ 3, x1_1, y1_1, z1_1, x2_1, y2_1, z2_1, x3_1, y3_1, z3_1, 3, x1_2, y1_2, z1_2, x2_2, y2_2, z2_2, x3_2, y3_2, z3_2 ]

The [x,y,z] points for each spline are the same points used to generate the spline.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplinesInterpolate.html)
[ISketchBlockDefinition::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineCount.html)
[ISketchBlockDefinition::GetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParams.html)
[ISketchBlockDefinition::IGetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplineParams.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
