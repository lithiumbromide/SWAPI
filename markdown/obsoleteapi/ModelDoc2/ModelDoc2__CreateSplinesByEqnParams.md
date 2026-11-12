---
title: "ModelDoc2::CreateSplinesByEqnParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateSplinesByEqnParams.htm"
---

# ModelDoc2::CreateSplinesByEqnParams

This method is obsolete and has been superseded by [SketchManager::CreateSplinesByEqnParams](sldworksAPI.chm::/SketchManager/SketchManager__CreateSplinesByEqnParams.htm).

Description

This method creates one or more spline segments using the B-curve parameters provided.

Syntax (OLE Automation)

retval = ModelDoc2.CreateSplinesByEqnParams ( paramsIn )

| Input: | (VARIANT) paramsIn | SafeArray containing an array of doubles to use in creating the spline (see Remarks ) |
| --- | --- | --- |
| Return: | (VARIANT) retval | SafeArray containing an array of Dispatch objects of the newly created splines |

Syntax (COM)

status = ModelDoc2->CreateSplinesByEqnParams ( propArray, knotsArray, cntrlPntCoordArray, &retval )

| Input: | (int*) propArray | Array of dimension, order, number of control points, periodicity (see Remarks ) |
| --- | --- | --- |
| Input: | (double*) knotsArray | knot1, knot2, and so on (see Remarks) |
| Input: | (double*) cntrlPntCoordArray | controlpoint1[dimension], controlpoint2[dimension], and so on (see Remarks) |
| Output: | (LPENUMSKETCHSEGMENTS) retval | Pointer to the enumerated list of newly created splines (see Remarks) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The propArray array contains four integers (placed in the first four doubles in the SafeArray):

- Dimension
- Order
- Number of Control Points
- Periodicity ( TRUE or FALSE )

The knotsArray contains doubles with (Number of Control Points + Order) elements.

The size of the cntrlPntCoordArray array is based upon the curve dimension.

- Dimension = 2 then each Control Point is an array of 2 doubles ( x, y )
- Dimension = 3 then each Control Point is an array of 3 doubles ( x, y, z)
- Dimension = 4 then each Control Point is an array of 4 doubles ( x, y, z, w ) where w = weight

The parameters are provided as three arrays, which for OLE automation are packed into a single SafeArray, which is packed as follows:

[ Dimension, Order, Number of control Points, Periodicity, knot1, knot2,...,ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

Pass the control point coordinates to this routine in sketch space. The Z value is interpreted as 0. In certain situations, you must transform your B-curve parameters to sketch space using Sketch::ModelToSketchTransform.

NOTE: If the spline being generated is a closed spline, then it must be flagged as periodic. If the data passed to this method does not generate a G1 continuous spline, then it creates multiple G1 continuous spline segments.

For the OLE interface, use the returned the object pointer directly, to call any APIs on the SketchSpline interface, or its base class, SketchSegment. For the COM interface, use the returned object pointer to manipulate a list of SketchSegments to call any APIs on the SketchSegment interface, or call QueryInterface to obtain the pointer to the SketchSpline and any APIs on the SketchSpline interface.

This method does not work with the ModelDoc2::SetAddToDB or ModelDoc2::SetDisplayWhenAdded. It always adds the spline directly to the database (as if ModelDoc2::SetAddToDB(True) is in effect), and you must redraw your document window see the entities that you added (as if ModelDoc2::SetDisplayWhenAdded(False) is in effect).

To create 3D splines, see ModelDoc2::InsertCurveFilePoint and related functions.
