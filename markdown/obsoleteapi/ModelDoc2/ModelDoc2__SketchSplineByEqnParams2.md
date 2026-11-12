---
title: "ModelDoc2::SketchSplineByEqnParams2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchSplineByEqnParams2.htm"
---

# ModelDoc2::SketchSplineByEqnParams2

This method is obsolete and has been superseded by [SketchManager::CreateSplineByEqnParams](sldworksAPI.chm::/SketchManager/SketchManager__CreateSplineByEqnParams.htm).

Description

This method creates a spline on the active 2D sketch using the specified b-curve parameters.

Syntax (OLE Automation)

retval = ModelDoc2.SketchSplineByEqnParams2 ( paramsIn )

| Input: | (VARIANT) paramsIn | VARIANT of type SafeArray containing an array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (BOOLEAN) retval | TRUE if created successfully, FALSE if not |

Syntax (COM)

Not available. See ModelDoc2::SketchSplineByEqnParams.

Remarks

The parameters are provided as 3 arrays, which for OLE automation are packed into a single SafeArray packed as follows:

[ Dimension, Order, Number of control Points, Periodicity, knot1, knot2,...,ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

Pass control point coordinates to this method in sketch space. The Z value is interpreted as 0. In certain situations, you must transform your b-curve parameters to sketch space with the help of Sketch::ModelToSketchTransform.

NOTE: If the spline being generated is a closed spline, then it must be flagged as periodic. In addition, splines generated in sketches must be G1 continuous. If the data passed to this method does not generate a G1 continuous spline, then it is rejected and a spline is not created. If your data is not G1 continuous, then you must split the spline into multiple G1 segments and call method for each segment.
