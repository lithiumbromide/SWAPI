---
title: "ModifyControlPoint Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "ModifyControlPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ModifyControlPoint.html"
---

# ModifyControlPoint Method (ISketchSpline)

Specifies new coordinates for the specified control point of this sketch spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function ModifyControlPoint( _
   ByVal Index As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim Index As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.ModifyControlPoint(Index, X, Y, Z)
```

### C#

```csharp
System.bool ModifyControlPoint(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool ModifyControlPoint(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 1-based index of the control point to modify
- `X`: X coordinate
- `Y`: Y coordinate
- `Z`: Z coordinate

### Return Value

True if control point successfully modified, false if not

## VBA Syntax

See [SketchSpline::ModifyControlPoint](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~ModifyControlPoint.html).

## Examples

[Edit Spline (VBA)](Edit_Spline_Example_VB.htm)

## Remarks

Before calling this method, call [ISplineParamData::GetControlPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetControlPoints.html) and [ISplineParamData::ControlPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~ControlPointsCount.html) to help specify Index and the new coordinates.

After calling this method, you must call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html) to update the sketch.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::ModifyKnot Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ModifyKnot.html)
[ISplineParamData::SetControlPoints Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~SetControlPoints.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
