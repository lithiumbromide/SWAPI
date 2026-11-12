---
title: "ModelDoc::CreateSplinesByEqnParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateSplinesByEqnParams.htm"
---

# ModelDoc::CreateSplinesByEqnParams

This method is obsolete and has been superseded by [ModelDoc2::CreateSplinesByEqnParams](../ModelDoc2/ModelDoc2__CreateSplinesByEqnParams.htm).

Description

This method creates one or more spline segments using the specifiedBcurve parameters.

Syntax (OLE Automation)

retval = ModelDoc.CreateSplinesByEqnParams ( paramsIn )

| Input: | (VARIANT) paramsIn | SafeArray containing an array of doubles to use in creating the spline |
| --- | --- | --- |
| Return: | (VARIANT) retval | SafeArray containing an array of Dispatch objects of the splines that were created |

Syntax (COM)

status = ModelDoc->CreateSplinesByEqnParams ( propArray, knotsArray, cntrlPntCoordArray, &retval )

| Input: | (int*) propArray | Includes dimension, order, number of control points, and periodicity |
| --- | --- | --- |
| Input: | (double*) knotsArray | knot1, knot2, and so on |
| Input: | (double*) cntrlPntCoordArray | controlpoint1[dimension], controlpoint2[dimension], and so on |
| Output: | (LPENUMSKETCHSEGMENTS) retval | Pointer to the enumerated list of splines that were created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The propArray argument contains 4 integers (placed in the first four doubles in the SafeArray):

- Dimension
- Order
- Number of Control Points
- Periodicity ( TRUE or FALSE )

knotsArray is an array of doubles with (Number of Control Points + Order) elements.

The size of the cntrlPntCoordArray array is based upon the curve dimension.

- Dimension = 2 then each Control Point is an array of 2 doubles ( x, y )
- Dimension = 3 then each Control Point is an array of 3 doubles ( x, y, z)
- Dimension = 4 then each Control Point is an array of 4 doubles ( x, y, z, w ) where w = weight

The parameters are provided as 3 arrays, which for OLE automation are packed into a single SafeArray, which is packed as follows:

[ Dimension, Order, Number of control Points, Periodicity, knot1, knot2,...,ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

Pass control point coordinates to this routine in sketch space. The Z value is interpreted as 0. In certain situations, you must transform your Bcurve parameters to sketch space with the help of Sketch::ModelToSketchXform.

NOTE: If the spline being generated is a closed spline, then it must be flagged as periodic. If the data passed to this method does not generate a G1 continuous spline, then it creates multiple G1 continuous spline segments.

For the OLE interface, the object pointer that is returned can be used directly to call any of the SketchSpline functions or its base class, SketchSegment. For the COM interface, the object pointer that is returned can be used to manipulate a list of SketchSegments, to call any of the SketchSegment functions,. Or, use a QueryInterface call to obtain the pointer to the SketchSpline, and any functions of the SketchSpline interface.

This method does not work with ModelDoc::SetAddToDB or ModelDoc::SetDisplayWhenAdded. It always adds the spline directly to the database, as if ModelDoc::SetAddToDB(True) was in effect. You must redraw your document window see the entities that you added, as if ModelDoc::SetDisplayWhenAdded(False was in effect.

To create 3D, use ModelDoc::InsertCurveFilePoint and related functions.
