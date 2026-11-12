---
title: "SketchBlockDefinition::GetSplines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchBlockDefintion/SketchBlockDefinition__GetSplines.htm"
---

# SketchBlockDefinition::GetSplines

This method is obsolete and has been superseded by [SketchBlockDefinition::GetSplines2](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__GetSplines2.htm).

Description

This method gets information about all of the splines in this block definition.

Syntax (OLE Automation)

Splines = SketchBlockDefinition.GetSplines ()

| Output: | (VARIANT) Splines | VARIANT of type SafeArray of doubles (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = SketchBlockDefinition->IGetSplines ( ArraySize, Splines)

| Input: | (long) ArraySize | Number of elements in the array (see Remarks ) |
| --- | --- | --- |
| Output: | (double) Splines | Array of doubles (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before using the COM version of this method, use the value returned by SketchBlockDefinition::GetSplineCount's PointCount argument to size the array.

The returned array of doubles has the format:

[ [ Color, LineType, NumSplinePoints, [x,y,z] ] … ]

This complete set of data repeats itself for each spline found in the sketch. For each spline, the array returned contains the color, the line type, the number of spline points in the spline, and the x,y,z value for each of those points. Therefore, the [x,y,z] parameter is an array of NumSplinePoints, which may vary in size from spline to spline.

The [x,y,z] points for each spline are not the same as the points used to generate the spline. This method tessellates the spline based on the display quality and places points along the spline appropriately.

LineType may take one of the values in swLineTypes_e.
