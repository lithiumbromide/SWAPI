---
title: "Body::CreateTrimmedSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateTrimmedSurface.htm"
---

# Body::CreateTrimmedSurface

This method is obsolete and has been superseded by [Body2::CreateTrimmedSurface](sldworksAPI.chm::/Body2/Body2__CreateTrimmedSurface.htm).

Description

This method creates a trimmed surface from a base surface and a list of existing trimming curves assumed to have been already created.

Syntax (OLE Automation)

retval = Body.CreateTrimmedSurface ()

| Return: | (BOOL) retval | TRUE if the trimmed surface was created, FALSE if it was not |
| --- | --- | --- |

Syntax (COM)

status = Body->CreateTrimmedSurface ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the trimmed surface was created, FALSE if it was not |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is the final call in a set of related functions that are designed to construct a trimmed surface from a base surface (possibly infinite) and a set of trimming curves. Before you use this method, you must call one of the base surface creation methods (such as Body::CreatePlanarSurface) and the trimming-curve creation method Surface::AddTrimmingLoop.

If you want to construct a solid body from trimmed surfaces, then you must first call PartDoc::CreateNewBody, which arranges for a place-holder for this trimmed surface.
