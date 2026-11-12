---
title: "Body::AddProfileLine"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__AddProfileLine.htm"
---

# Body::AddProfileLine

This method is obsolete and has been superseded by [Body2::AddProfileLine](sldworksAPI.chm::/Body2/Body2__AddProfileLine.htm).

Description

This method creates a line profile curve and returns a pointer to that curve.

Syntax (OLE Automation)

retval = Body.AddProfileLine ( rootPoint, direction)

| Input: | (VARIANT) rootPoint | VARIANT of type SafeArray of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (VARIANT) direction | VARIANT of type SafeArray of 3 doubles (x,y,z) |
| Return: | (LPDISPATCH) retval | Pointer to dispatch object, the line profile curve |

Syntax (COM)

status = Body->IAddProfileLineDLL ( rootPoint, direction, &retval )

| Input: | (double*) rootPoint | Pointer to an array of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (double*) direction | Pointer to an array of 3 doubles (x,y,z) |
| Output: | (LPCURVE) retval | Pointer to the line profile curve. |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can use this method with Body::CreateRevolutionSurface to generate a cylindrical surface of revolution or with Body::CreateExtrusionSurface to generate a tabulated cylinder.
