---
title: "SketchPoint::SetFramePointTangent"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchPoint/SketchPoint__SetFramePointTangent.htm"
---

# SketchPoint::SetFramePointTangent

This method is obsolete and was not superseded.

Description

This method sets the frame control point tangent vector for the sketch point.

Syntax (OLE Automation)

retval = SketchPoint.SetFramePointTangent ( vector )

| Input: | (VARIANT) vector | VARIANT of type SafeArray of 3 doubles defining the (x,y,z) components of the frame control point tangent vector for the sketch point |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the tangent vector is set successfully, FALSE otherwise |
|  |  | S_OK if successful |

Syntax (COM)

status = SketchPoint->ISetFramePointTangent ( vector, &retval )

| Input: | (double) * vector | An array of 3 doubles defining the (x,y,z) components of the frame control point tangent vector for the sketch point |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the tangent vector was set successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method applies to sketch points that are sketch spline frame points or sketch spline moving frames only.
