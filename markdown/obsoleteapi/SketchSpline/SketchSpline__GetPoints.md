---
title: "SketchSpline::GetPoints"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchSpline/SketchSpline__GetPoints.htm"
---

# SketchSpline::GetPoints

This method is obsolete and has been superseded by [SketchSpline::GetPoints2](sldworksAPI.chm::/SketchSpline/SketchSpline__GetPoints2.htm).

Description

This method gets the points used when creating this sketch spline. The points returned are by interpolation instead of by tessellation as is done by Sketch::GetSplines.

Syntax (OLE Automation)

retval = SketchSpline.GetPoints ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles; these are the x,y,z points used to create the spline |
| --- | --- | --- |

Syntax (COM)

status = SketchSpline->IGetPoints ( retval )

| Output: | (double*) retval | Array of doubles of size (SketchSpline::GetPointCount * 3); these are the x,y,z points used to create the spline |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The [ x,y,z ] points returned for this spline are the same points used to generate the spline. If you want a tessellated representation of the spline, see Sketch::GetSplines.

For COM implementations, you can determine the size of the array by multiplying the SketchSpline::GetPointCount return value by 3.
