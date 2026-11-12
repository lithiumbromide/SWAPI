---
title: "Curve::CreateTrimmedCurve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve_CreateTrimmedCurve.htm"
---

# Curve::CreateTrimmedCurve

This method is obsolete and has been superseded by [Curve::CreateTrimmedCurve2](sldworksAPI.chm::/Curve/Curve__CreateTrimmedCurve2.htm).

Description

This method creates a trimmed curve using the specified 3D points.

Syntax (OLE Automation)

retval = Curve.CreateTrimmedCurve ( x1, y1, z1, x2, y2, z2 )

| Input: | (double) x1 | X start point |
| --- | --- | --- |
| Input: | (double) y1 | Y start point |
| Input: | (double) z1 | Z start point |
| Input: | (double) x2 | X end point |
| Input: | (double) y2 | Y end point |
| Input: | (double) z2 | Z end point |
| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created curve or NULL if the operation fails |

Syntax (COM)

status = Curve->ICreateTrimmedCurve ( startPt, endPt, &retval )

| Input: | (double*) startPt | Pointer to an array of 3 doubles, the x, y, z startpoint |
| --- | --- | --- |
| Input: | (double*) endPt | Pointer to an array of 3 doubles, the x, y, z endpoint |
| Output: | (LPCURVE) retval | Pointer to the newly created curve or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use the resulting curve for surface trimming operations (for example, Surface::CreateTrimmedSheet).
