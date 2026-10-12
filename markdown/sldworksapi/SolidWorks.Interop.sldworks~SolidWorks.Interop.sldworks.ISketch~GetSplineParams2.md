---
title: "GetSplineParams2 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSplineParams2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams2.html"
---

# GetSplineParams2 Method (ISketch)

Obsolete. Superseded by [ISketch::GetSplineParams3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSplineParams3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplineParams2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetSplineParams2()
```

### C#

```csharp
System.object GetSplineParams2()
```

### C++/CLI

```cpp
System.Object^ GetSplineParams2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Sketch::GetSplineParams2](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSplineParams2.html).

## Remarks

See [ISketch::GetSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchSegments.html) or [ISketch::IEnumSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IEnumSketchSegments.html) for access to individual [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) and [ISketchSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline.html) objects.

The return value is an array of doubles containing data for all the splines in the sketch:

[ packedDouble1, packedDouble2, ControlPoint1[Dimension elements], ControlPoint2[Dimension elements],... knot1, knot2,..., packedDouble3, packedDouble4, packedDouble5, ]

`packedDouble1 and packedDouble2`

The first two array elements for each spline contain four integer values holding information that describes the rest of the data in that spline's parameters:

| Spline Element | Packed Data |  |
| --- | --- | --- |
| 0 | Dim | Order |
| 1 | nCtrlPoints | Periodic |

where:

- Dim is the number of dimensions in which the spline is defined
- Order is the order of the spline
- nCtrlPoints is the number of control points
- Periodic is 1 for a closed spline or 0 for an open spline

**NOTE:** For information about unpacking double arrays into integer pairs, see:

`ControlPoint#`

The ControlPoint data (in the sketch coordinate system) follows the two packed data elements.

`knots#`

The number of knots depends on whether the spline is periodic or not:

| Periodic: | numKnots = nCtrlPoints + 1 |
| --- | --- |
| Non-Periodic: | numKnots = nCtrlPoints + Order |

**`packedDouble3, packedDouble4, and packedDouble5`**

The last three array elements for each spline contain five integer values holding style and layer information:

| Spline Element | Packed Data |  |
| --- | --- | --- |
| i | Color | lineStyle |
| i+1 | lineWidth | Layer |
| i+2 | layerOverride | Not used |

where:

- i is the index following the last Knot or [2 + numKnots + numControlPointDoubles * Dim]
- Color is the COLORREF value describing the color used for the `ith` spline
- lineStyle is the line style used for the ith spline. Valid values can be found in the [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) enumeration
- lineWidth is line width used for the ith spline. Valid values can be found in the [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html) enumeration
- Layer is an integer index to the layer that the ith spline is on
- layerOverride is integer with bit flags set to determine which properties, if any, have been overridden or should be overridden.

Therefore, the size of the data for each spline is given by:

2 + numKnots + numControlPointDoubles * Dim + 3

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IGetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplineParams2.html)
[ISketch::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.html)
[ISketch::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.html)
[ISketch::GetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.html)
[ISketch::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.html)
[ISketch::IGetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines.html)
[ISketch::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
