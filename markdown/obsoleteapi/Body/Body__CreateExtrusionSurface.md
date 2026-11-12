---
title: "Body::CreateExtrusionSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateExtrusionSurface.htm"
---

# Body::CreateExtrusionSurface

This method is obsolete and has been superseded by [Body2::CreateExtrusionSurface](sldworksAPI.chm::/Body2/Body2__CreateExtrusionSurface.htm).

Description

This method creates a new extrusion surface (infinitely long tabulated cylinder).

Syntax (OLE Automation)

retval = Body.CreateExtrusionSurface ( profileCurve, axisDirection)

| Input: | (LPDISPATCH) profileCurve | Pointer to Dispatch object, the profile curve |
| --- | --- | --- |
| Input: | (VARIANT) axisDirection | VARIANT of type SafeArray of 3 doubles (x,y,z) |
| Return: | (LPDISPATCH) retval | Pointer to Dispatch object, a new surface of extrusion (tabulated cylinder) |

Syntax (COM)

status = Body->ICreateExtrusionSurfaceDLL( profileCurve, axisDirection, &retval )

| Input: | (LPCURVE) profileCurve | Pointer to the profile curve |
| --- | --- | --- |
| Input: | (double*) axisDirection | Array of 3 doubles (x,y,z) |
| Output: | (LPSURFACE) retval | Pointer to the new surface of extrusion (tabulated cylinder) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is used with a set of related functions that construct a body from trimmed surfaces.

The profileCurve argument is extruded along the direction vector of axisDirection, the new surface being the envelope of the curve. The profile curve must be a line, circle, or B-spline curve.

You can use this method with trimming curve creation routines (for example, Surface::AddTrimmingLoop) to construct a trimmed tabulated cylinder.
