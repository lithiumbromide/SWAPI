---
title: "ModelDoc::CreateClippedSplines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateClippedSplines.htm"
---

# ModelDoc::CreateClippedSplines

This method is obsolete and has been superseded by [ModelDoc2::CreateClippedSplines](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateClippedSplines.htm).

Description

This function creates one or more SketchSpline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D Sketch.

Syntax (OLE Automation)

retval = ModelDoc.CreateClippedSplines ( paramsIn, x1, y1, x2, y2 )

| Input: | (VARIANT) paramsIn | See Remarks |
| --- | --- | --- |
| Input: | (double) x1 | x component of the lower corner of the clipping rectangle |
| Input: | (double) y1 | y component of the lower corner of the clipping rectangle |
| Input: | (double) x2 | x component of the upper corner of the clipping rectangle |
| Input: | (double) y2 | y component of the upper corner of the clipping rectangle |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of SketchSegments |

Syntax (COM)

status = ModelDoc->ICreateClippedSplines ( propArray, knotsArray, cntrlPntCoordArray, x1, y1, x2, y2, &retval )

| Input: | (int*) propArray | See Remarks |
| --- | --- | --- |
| Input: | (double*) knotsArray | See Remarks |
| Input: | (double*) cntrlPntCoordArray | See Remarks |
| Input: | (double) x1 | x component of the lower corner of the clipping rectangle |
| Input: | (double) y1 | y component of the lower corner of the clipping rectangle |
| Input: | (double) x2 | x component of the upper corner of the clipping rectangle |
| Input: | (double) y2 | y component of the upper corner of the clipping rectangle |
| Output: | (LPENUMSKETCHSEGMENTS) retval | Enumeration of newly created SketchSegments |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The results are undefined for calls made in an active 3D Sketch.

OLE. The paramsIn argument is a SafeArray of size ( 4 + numKnots + numControlPointDoubles ) as follows:

[ Dimension, Order, NumControlPoints, Periodicity, knot1, knot2,..., ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

where:

Dimension, Order, NumControlPoints, and Periodicity are integer values

knot1

knot2

...

ControlPoint1[dimension]

ControlPoint2[dimension]

...

The size of the knotsArray is determined by ( NumControlPoints + Order )

The size of the cntrlPntCoordArray is based upon the curve dimension:

If Dimension = 3 then Control Point is an array of 3 doubles ( x, y, z )

If Dimension = 4 then Control Point is an array of 4 doubles ( x, y, z, w ) where w = weight

COM. The arrays are as follows:

propArray = [ Dimension, Order, NumControlPoints, Periodicity ]

knotsArray = [ NumControlPoints + Order ]

cntrlPntCoordArray = [ NumControlPoints * Dimension ]

If Dimension = 3 then Control Point is an array of 3 doubles ( x, y, z )

If Dimension = 4 then Control Point is an array of 4 doubles ( x, y, z, w ) where w = weight
