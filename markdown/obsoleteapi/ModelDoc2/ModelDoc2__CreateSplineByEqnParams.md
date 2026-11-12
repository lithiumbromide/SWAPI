---
title: "ModelDoc2::CreateSplineByEqnParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateSplineByEqnParams.htm"
---

# ModelDoc2::CreateSplineByEqnParams

This method is obsolete and has been superseded by [SketchManager::CreateSplineByEqnParams](sldworksAPI.chm::/SketchManager/SketchManager__CreateSplineByEqnParams.htm).

Description

This method creates a B-curve from B-spline data; that is, a set of B-spline vertices (control points) and a knot vector. The curve can be either periodic or non-periodic.

Syntax (OLE Automation)

retval = ModelDoc2.CreateSplineByEqnParams ( paramsIn )

| Input: | (VARIANT) paramsIn | SafeArray containing an array of doubles to use in creating the spline |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to the Dispatch object of the newly created spline |

Syntax (COM)

status = ModelDoc2->ICreateSplineByEqnParams ( propArray, knotsArray, cntrlPntCoordArray, &retval )

| Input: | (int*) propArray | Includes dimension, order, number of control points, periodicity |
| --- | --- | --- |
| Input: | (double*) knotsArray | knot1, knot2, and so on |
| Input: | (double*) cntrlPntCoordArray | controlpoint1[dimension], controlpoint2[dimension], and so on |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the newly created spline |
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

NOTE: If the generated spline is a closed spline, then it must be flagged as periodic. Additionally, splines generated in sketches must be G1 continuous. If the data passed to this method does not generate a G1 continuous spline, then it is rejected and a spline is not created. If your data is not G1 continuous, then you must split the spline into multiple G1 segments and call this method for each segment.

For the OLE interface, you can use the returned object pointer directly to call any APIs on the SketchSpline interface or its base class, SketchSegment. For the COM interface, you can use the returned object pointer directly to call any APIs on the SketchSegment interface, or use QueryInterface to obtain the pointer to the SketchSpline and any APIs on the SketchSpline interface.

This method does not work with ModelDoc2::SetAddToDB or ModelDoc2::SetDisplayWhenAdded. It always adds the spline directly to the database (as if ModelDoc2::SetAddToDB(True) is in effect), and you must redraw your document window to see the entities that you added (as if ModelDoc2::SetDisplayWhenAdded(False) is in effect).

To create 3D splines, see ModelDoc2::InsertCurveFilePoint and related functions.
