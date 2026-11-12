---
title: "ModelDoc2::SketchSplineByEqnParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchSplineByEqnParams.htm"
---

# ModelDoc2::SketchSplineByEqnParams

This method is obsolete and has been superseded by [SketchManager::CreateSplineByEqnParams](sldworksAPI.chm::/SketchManager/SketchManager__CreateSplineByEqnParams.htm).

Description

This method creates a spline on the active 2D sketch using the specified b-curve parameters.

Syntax (OLE Automation)

Not available. See ModelDoc2::SketchSplineByEqnParams2.

Syntax (COM)

status = ModelDoc2->ISketchSplineByEqnParams ( propArray, knotsArray, cntrlPntCoordArray, &retval )

| Input: | (int*) propArray | Includes dimension, order, number of control points, and periodicity |
| --- | --- | --- |
| Input: | (double*) knotsArray | knot1, knot2, and so on |
| Input: | (double*) cntrlPntCoordArray | controlpoint1[dimension], controlpoint2[dimension], and so on |
| Output: | (BOOL) retval | TRUE if created successfully, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The propArray argument contains 4 integers packed into the first two doubles in the SafeArray:

- Dimension
- Order
- Number of Control Points
- Periodicity ( TRUE or FALSE )

The knotsArray argument is an array of doubles with (Number of Control Points + Order) elements.

The size of the cntrlPntCoordArray array is based upon the curve dimension:

- Dimension = 2 then each control point is an array of 2 doubles ( x, y )
- Dimension = 3 then each control point is an array of 3 doubles ( x, y, z)
- Dimension = 4 then each control point is an array of 4 doubles ( x, y, z, w ) where w = weight

The parameters are provided as 3 arrays, which for COM applications are passed separately.

Pass control point coordinates to this method in sketch space. The Z value is interpreted as 0. In certain situations, you must transform your b-curve parameters to sketch space with the help of Sketch::ModelToSketchTransform.

NOTE: If the spline being generated is a closed spline, then it must be flagged as periodic. In addition, splines generated in sketches must be G1 continuous. If the data passed to this method does not generate a G1 continuous spline, then it is rejected and a spline is not created.
