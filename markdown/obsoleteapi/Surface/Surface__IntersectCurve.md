---
title: "Surface::IntersectCurve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Surface/Surface__IntersectCurve.htm"
---

# Surface::IntersectCurve

This method is obsolete and has been superseded by [Surface::IntersectCurve2](sldworksAPI.chm::/Surface/Surface__IntersectCurve2.htm).

Description

This method gets a surface-curve intersection. The curves must be bounded.

Syntax (OLE Automation)

retval = Surface.IntersectCurve ( otherCurve, curveBound, pointArray, tArray, uvArray, &retval )

| Input: | (LPDISPATCH) otherCurve | Pointer to curve |
| --- | --- | --- |
| Input: | (VARIANT) curveBound | Array of 6 doubles representing the start and end points of the curve |
| Output: | (VARIANT*) pointArray | Array of points |
| Output: | (VARIANT*) tArray | VARIANT of type SafeArray of parameters on curve |
| Output: | (VARIANT*) uvArray | VARIANT of type SafeArray of parameters on surface |
| Output: | (VARIANT_BOOL) retval | TRUE if intersection succeeded, FALSE if not |

Syntax (COM)

status = Surface->IIntersectCurve ( otherCurve, curveBound, pointArray, tArray, uvArray, &retval )

| Input: | (LPCURVE) otherCurve | Pointer to curve |
| --- | --- | --- |
| Input: | (double*) curveBound | Array of 6 doubles representing the start and end points of the curve |
| Input: | (long) pointCount | Number of points |
| Output: | (VARIANT*) pointArray | Array of points of size pointCount*3 |
| Output: | (VARIANT*) tArray | Array of parameters on curve of size pointCount |
| Output: | (VARIANT*) uvArray | Array of size pointCount*2 |
| Output: | (VARIANT_BOOL) retval | TRUE if intersection succeeded, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Visual Basic applications should use this method instead of using Surface::GetIntersectCurveCount.

Users of the COM version of this method should first call Surface::GetIntersectCurveCount to get the number of points for this surface-curve intersection.
