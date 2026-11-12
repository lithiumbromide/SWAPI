---
title: "ModelDoc::CreateSplineByEqnParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateSplineByEqnParams.htm"
---

# ModelDoc::CreateSplineByEqnParams

This method is obsolete and has been superseded by [ModelDoc2::CreateSplineByEqnParams](../ModelDoc2/ModelDoc2__CreateSplineByEqnParams.htm).

Description

This method creates a spline using the specified Bcurve parameters.

Syntax (OLE Automation)

retval = ModelDoc.CreateSplineByEqnParams ( paramsIn )

| Input: | (VARIANT) paramsIn | SafeArray containing an array of doubles to use in creating the spline |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to the Dispatch object of the spline that was created |

Syntax (COM)

status = ModelDoc->ICreateSplineByEqnParams ( propArray, knotsArray, cntrlPntCoordArray, &retval )

| Input: | (int*) propArray | Includes dimension, order, number of control points, and periodicity |
| --- | --- | --- |
| Input: | (double*) knotsArray | knot1, knot2, and so on |
| Input: | (double*) cntrlPntCoordArray | controlpoint1[dimension], controlpoint2[dimension], and so on |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the spline that was created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The propArray argument contains 4 integers (placed in the first four doubles in the SafeArray):

- Dimension
- Order
- Number of Control Points
- Periodicity ( TRUE or FALSE )

The knotsArray argument is an array of doubles with (Number of Control Points + Order) elements.

The size of the cntrlPntCoordArray array is based upon the curve dimension.

- Dimension = 2 then each Control Point is an array of 2 doubles ( x, y )
- Dimension = 3 then each Control Point is an array of 3 doubles ( x, y, z)
- Dimension = 4 then each Control Point is an array of 4 doubles ( x, y, z, w ) where w = weight

The parameters are provided as 3 arrays, which for OLE automation are packed into a single SafeArray, which is packed as follows:

[ Dimension, Order, Number of control Points, Periodicity, knot1, knot2,...,ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

Pass control point coordinates to this routine in sketch space. The Z value is interpreted as 0. In certain situations, you must transform your Bcurve parameters to sketch space with the help of Sketch::ModelToSketchXform.

NOTE If the spline generated is a closed spline, then it must be flagged as periodic. Additionally, splines generated in sketches must be G1 continuous. If the data passed to this method does not generate a G1 continuous spline, then it is rejected and a spline is not created. If your data is not G1 continuous, then you must split the spline into multiple G1 segments and call this method for each segment.

For the OLE interface, the object pointer returned can be used directly to call any of the SketchSpline functions, or its base class, SketchSegment. For the COM interface, the object pointer that is returned can be used directly to call any of the SketchSegment funcitons or use a QueryInterface to obtain the pointer to SketchSpline, and call any of the functions of the SketchSpline interface.

This method does not work with the ModelDoc::SetAddToDB or ModelDoc::SetDisplayWhenAdded. It always adds the spline directly to the database as if ModelDoc::SetAddToDB(True) was in effect. You must redraw your document window see the entities that you added , as if ModelDoc::SetDisplayWhenAdded(False) was in effect.

To create 3D splines, use ModelDoc::InsertCurveFilePoint and related functions.
