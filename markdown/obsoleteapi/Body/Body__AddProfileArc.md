---
title: "Body::AddProfileArc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__AddProfileArc.htm"
---

# Body::AddProfileArc

This method is obsolete and has been superseded by [Body2::AddProfileArc](sldworksAPI.chm::/Body2/Body2__AddProfileArc.htm).

Description

This method creates an arc profile curve and returns a pointer to that curve. This method always creates a full circle.

Syntax (OLE Automation)

retval = Body.AddProfileArc ( center, axis, radius, startPoint, endPoint )

| Input: | (VARIANT) center | VARIANT of type SafeArray of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (VARIANT) axis | VARIANT of type SafeArray of 3 doubles (x,y,z) |
| Input: | (double) radius | Desired radius |
| Input: | (VARIANT) startPoint | VARIANT of type SafeArray of 3 doubles (x,y,z) |
| Input: | (VARIANT) endPoint | VARIANT of type SafeArray of 3 doubles (x,y,z) |
| Return: | (LPDISPATCH) retval | Pointer to Dispatch object, the arc profile curve |

Syntax (COM)

status = Body->IAddProfileArcDLL ( center, axis, radius, startPoint, endPoint, &retval )

| Input: | (double*) center | Pointer to an array of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (double*) axis | Pointer to an array of 3 doubles (x,y,z) |
| Input: | (double) radius | Desired radius |
| Input: | (double*) startPoint | Pointer to an array of 3 doubles (x,y,z) |
| Input: | (double*) endPoint | Pointer to an array of 3 doubles (x,y,z) |
| Output: | (LPCURVE) retval | Pointer to the arc profile curve |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can use this method in conjunction with Body::CreateRevolutionSurface to generate spherical or toroidal surfaces of revolution, or with Body::CreateExtrusionSurface to generate a tabulated cylinder.
