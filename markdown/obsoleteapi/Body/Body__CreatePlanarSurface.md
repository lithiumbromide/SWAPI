---
title: "Body::CreatePlanarSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreatePlanarSurface.htm"
---

# Body::CreatePlanarSurface

This method is obsolete and has been superseded by [Body2::CreatePlanarSurface](sldworksAPI.chm::/Body2/Body2__CreatePlanarSurface.htm).

Description

This method creates a new infinite planar surface.

Syntax (OLE Automation)

retval = Body.CreatePlanarSurface ( vRootPoint, vNormal)

| Input: | (VARIANT) vRootPoint | VARIANT of type SafeArray of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (VARIANT) vNormal | VARIANT of type SafeArray of 3 doubles (x,y,z) |
| Return: | (LPDISPATCH) retval | Dispatch pointer to dispatch object, a new planar surface |

Syntax (COM)

status = Body->ICreatePlanarSurfaceDLL ( vRootPoint, vNormal, &retval )

| Input: | (double*) vRootPoint | Pointer to an array of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (double*) vNormal | Pointer to an array of 3 doubles (x,y,z) |
| Output: | (LPSURFACE) retval | Pointer to the new planar surface |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can use this method with:

- A set of related functions that construct a body from trimmed surfaces.
- Trimming curve creation routines (for example, Surface::AddTrimmingLoop) to construct a trimmed surface.

Also. see Body::ICreatePlanarTrimSurfaceDLL, which allows you to create a planar trimmed surface directly from the vertex points.
