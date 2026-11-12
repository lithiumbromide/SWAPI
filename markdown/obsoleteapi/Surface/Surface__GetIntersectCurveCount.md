---
title: "Surface::GetIntersectCurveCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Surface/Surface__GetIntersectCurveCount.htm"
---

# Surface::GetIntersectCurveCount

This method is obsolete and has been superseded by [Surface::GetIntersectCurveCount2](sldworksAPI.chm::/Surface/Surface__GetIntersectCurveCount2.htm).

Description

This method gets a point count for a surface-curve intersection.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Surface->GetIntersectCurveCount ( otherCurve, curveBound, &count )

| Input: | (LPCURVE) otherCurve | Pointer to curve |
| --- | --- | --- |
| Input: | (double*) curveBound | Array of 6 doubles representing the start and end points of the curve |
| Output: | (long) count | Number of points |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Visual Basic and C++ Dispatch applications should use Surface::IntersectCurve instead of this method.
