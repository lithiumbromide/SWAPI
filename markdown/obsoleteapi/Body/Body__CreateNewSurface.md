---
title: "Body::CreateNewSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateNewSurface.htm"
---

# Body::CreateNewSurface

This method is obsolete and has been superseded by [Body2::CreateNewSurface](sldworksAPI.chm::/Body2/Body2__CreateNewSurface.htm).

Description

This method creates a handle for a new surface to be used as geometry for a face to be added to the body.

Syntax (OLE Automation)

retval = Body.CreateNewSurface ()

| Return: | (LPDISPATCH) retval | Pointer to dispatch object, a new surface |
| --- | --- | --- |

Syntax (COM)

status = Body->ICreateNewSurface ( &retval )

| Output: | (LPSURFACE) retval | Pointer to the new surface |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is the first in a set of related functions that construct a body from trimmed surfaces.

Internally, this method also creates a list that serves as a place-holder for trimming curves when trimming the surface.
