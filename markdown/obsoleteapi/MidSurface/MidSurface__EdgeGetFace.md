---
title: "MidSurface::EdgeGetFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__EdgeGetFace.htm"
---

# MidSurface::EdgeGetFace

This method is obsolete and has been superseded by [MidSurface2::EdgeGetFace](sldworksAPI.chm::/MidSurface2/MidSurface2__EdgeGetFace.htm).

Description

This method takes the specified mid-surface edge and returns the body face on which this edge lies. This condition occurs when a reference surface extends to meet one of the faces on the original part body. If the edge specified does not lie on one of the original part body faces, then a NULL is returned.

Syntax (OLE Automation)

retval = MidSurface2.EdgeGetFace ( edgeInDisp)

| Input: | (LPDISPATCH) edgeInDisp | Pointer to a Dispatch object, a MidSurface edge |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, a face on the original solid body |

Syntax (COM)

status = MidSurface2->IEdgeGetFace ( edgeInDisp, &retval )

| Input: | (LPEDGE) edgeInDisp | Pointer to a MidSurface edge |
| --- | --- | --- |
| Output: | (LPFACE) retval | Pointer to a face on the original solid body |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This edge is not topologically related to the face returned.
