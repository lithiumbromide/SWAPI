---
title: "ModifyKnot Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "ModifyKnot"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ModifyKnot.html"
---

# ModifyKnot Method (ISketchSpline)

Modifies the specified interior knot of this sketch spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function ModifyKnot( _
   ByVal Index As System.Integer, _
   ByVal DKnot As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim Index As System.Integer
Dim DKnot As System.Double
Dim value As System.Boolean

value = instance.ModifyKnot(Index, DKnot)
```

### C#

```csharp
System.bool ModifyKnot(
   System.int Index,
   System.double DKnot
)
```

### C++/CLI

```cpp
System.bool ModifyKnot(
   System.int Index,
   System.double DKnot
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 1-based index of the interior knot to modify (see **Remarks**)
- `DKnot`: Knot value

### Return Value

True if knot successfully modifed, false if not

## VBA Syntax

See [SketchSpline::ModifyKnot](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~ModifyKnot.html).

## Examples

[Edit Spline (VBA)](Edit_Spline_Example_VB.htm)

## Remarks

Interior knots occur after the first set of 0s and before the last set of 1s in the knot array. If the knot array is [ 0 0 0 0 0.279240779943874 0.55 0.720759220056126 1 1 1 1 ], then the interior knots are 0.279240779943874, 0.55, and 0.720759220056126.

Before calling this method, call [ISplineParamData::GetKnotPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetKnotPoints.html) and [ISplineParamData::KnotPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~KnotPointsCount.html) to help specify Index and the new knot value.

After calling this method, you must call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html) to update the sketch.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::ModifyControlPoint Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ModifyControlPoint.html)
[ISplineParamData::SetKnotPoints Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~SetKnotPoints.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
