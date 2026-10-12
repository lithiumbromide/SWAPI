---
title: "SketchPoint::GetFramePointTangent"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchPoint/SketchPoint__GetFramePointTangent.htm"
---

# SketchPoint::GetFramePointTangent

This method is obsolete and was not superseded.

Description

This method gets the frame control point tangent vector for this sketch point.

Syntax (OLE Automation)

vector = SketchPoint.GetFramePointTangent ( retval )

| Output: | (BOOL) retval | TRUE if the tangent vector is returned successfully, FALSE otherwise |
| --- | --- | --- |
| Return: | (VARIANT) vector | VARIANT of type SafeArray of 3 doubles defining the (x,y,z) components of the frame control point tangent vector of the sketch point |

Syntax (COM)

status = SketchPoint->IGetFramePointTangent ( &retval, vector )

| Output: | (VARIANT_BOOL) retval | TRUE if the tangent vector is returned successfully, FALSE otherwise |
| --- | --- | --- |
| Output: | (double) *vector | An array of 3 doubles defining the (x,y,z) components of the frame control point tangent vector of the sketch point |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The sketch that the sketch point is on must be active while calling this method.

This method applies to sketch points that are sketch spline frame points or sketch spline moving frames only.
