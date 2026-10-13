---
title: "Sketch::GetSplineParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__GetSplineParams.htm"
---

# Sketch::GetSplineParams

This method is obsolete and is superseded by [Sketch::GetSplineParams2](sldworksAPI.chm::/Sketch/Sketch__GetSplineParams2.htm).

Description

This method returns the parameters of the spline.

Syntax (OLE Automation)

params = Sketch.GetSplineParams ( )

| Return: | (VARIANT) params | VARIANT of type SafeArray containing an array of doubles |
| --- | --- | --- |

Syntax (COM)

status = Sketch->IGetSplineParams ( params )

| Output: | (double*) params | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See Sketch::GetSketchSegments or Sketch::IEnumSketchSegments for access to individual SketchSegment and SketchSpline objects.

For COM implementations, call Sketch::GetSplineParamsCount to determine the size of the array required to hold the data.

The return value is an array of doubles containing data for all the splines in the sketch.

The first two array elements for each spline contain 4 integer values holding information that describes the rest of the data in that splines parameters:

| Spline Element | Packed Data |  |
| --- | --- | --- |
| 0 | Dim | Order |
| 1 | nCtrlPoints | Periodic |

where:

- Dim is the number of dimensions the spline is defined in
- Order is the order of the spline
- nCtrlPoints is the number of control points
- Periodic is 1 for a closed spline or 0 for an open spline

The number of knots depends on whether the spline is periodic or not:

| Periodic: | numKnots = nCtrlPoints + 1 |
| --- | --- |
| Non-Periodic: | numKnots = nCtrlPoints + Order |

Therefore, the size of the data for each spline is given by:

2 + numKnots + numControlPointDoubles * Dim

The ControlPoint data (in the sketch coordinate system) follows the 2 packed data elements, and then the Knot points. Subsequent Splines follow one another in the array.

[ packedDouble1, packedDouble2, ControlPoint1[Dimension elements], ControlPoint2[Dimension elements],... knot1, knot2,..., ]
