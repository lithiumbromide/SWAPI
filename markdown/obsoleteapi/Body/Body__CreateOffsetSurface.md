---
title: "Body::CreateOffsetSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateOffsetSurface.htm"
---

# Body::CreateOffsetSurface

This method is obsolete and has been superseded by [Body2::CreateOffsetSurface](sldworksAPI.chm::/Body2/Body2__CreateOffsetSurface.htm).

Description

This method creates a new surface which is offset from an existing surface object.

Syntax (OLE Automation)

retval = Body.CreateOffsetSurface ( surfaceIn, distance)

| Input: | (LPDISPATCH) surfaceIn | Pointer to a dispatch object, the surface from which you want to offset |
| --- | --- | --- |
| Input: | (double) distance | Offset distance |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created surface |

Syntax (COM)

status = Body->ICreateOffsetSurface ( surfaceIn, distance, &retval )

| Input: | (LPSURFACE) surfaceIn | Pointer to a dispatch object, the surface from which you want to offset |
| --- | --- | --- |
| Input: | (double) distance | Offset distance |
| Output: | (LPSURFACE) retval | Pointer to the newly created surface |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
