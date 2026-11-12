---
title: "SetKnotPoints Method (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "SetKnotPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~SetKnotPoints.html"
---

# SetKnotPoints Method (ISplineParamData)

Sets the knot vector for a spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetKnotPoints( _
   ByVal KnotPoints As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim KnotPoints As System.Object
Dim value As System.Boolean

value = instance.SetKnotPoints(KnotPoints)
```

### C#

```csharp
System.bool SetKnotPoints(
   System.object KnotPoints
)
```

### C++/CLI

```cpp
System.bool SetKnotPoints(
   System.Object^ KnotPoints
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `KnotPoints`: Array of doubles between 0 and 1, inclusive

### Return Value

True if successful, false if not

## VBA Syntax

See [SplineParamData::SetKnotPoints](ms-its:sldworksapivb6.chm::/sldworks~SplineParamData~SetKnotPoints.html).

## Examples

[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

## Remarks

Together with [control points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData~GetControlPoints.html) knots determine the shape and smoothness of a spline. The knot vector divides the parametric space into intervals or knot spans. These intervals may be uniform or non-uniform. Each interval governs a different control point.

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html)
[ISplineParamData::GetKnotPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetKnotPoints.html)
[ISplineParamData::IGetKnotPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetKnotPoints.html)
[ISplineParamData::KnotPointsCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~KnotPointsCount.html)
[ISketchSpline::ModifyKnot Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ModifyKnot.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
