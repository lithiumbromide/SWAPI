---
title: "Body::CreateBodyFromSurfaces"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateBodyFromSurfaces.htm"
---

# Body::CreateBodyFromSurfaces

This method is obsolete and has been superseded by [Body2::CreateBodyFromSurfaces](sldworksAPI.chm::/Body2/Body2__CreateBodyFromSurfaces.htm).

Description

This method creates a body from a list of trimmed surfaces assumed to have been already created.

Syntax (OLE Automation)

retval = Body.CreateBodyFromSurfaces ()

| Return: | (BOOL) retval | TRUE if body creation is successful, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = Body->CreateBodyFromSurfaces ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if body creation is successful, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is the final call to a set of related functions that are designed to construct a body from trimmed surfaces. The first call in this process is to PartDoc::CreateNewBody, which arranges for a place-holder for all the trimmed surfaces.
