---
title: "Body::CreateTempBodyFromSurfaces"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateTempBodyFromSurfaces.htm"
---

# Body::CreateTempBodyFromSurfaces

This method is obsolete and has been superseded by [Body2::CreateTempBodyFromSurfaces](sldworksAPI.chm::/Body2/Body2__CreateTempBodyFromSurfaces.htm).

Description

This method creates a body from a list of existing trimmed surfaces.

Syntax (OLE Automation)

retval = Body.CreateTempBodyFromSurfaces ( )

| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the body |
| --- | --- | --- |

Syntax (COM)

status = Body->ICreateTempBodyFromSurfaces ( &retval )

| Output: | (LPBODY) retval | Pointer to the temporary body |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is the last in a set of related methods (like Body::CreateBodyFromSurfaces) that construct a temporary body from trimmed surfaces. The first method you need to call in this process is PartDoc::CreateNewBody, which arranges for a place-holder for all the trimmed surfaces.
