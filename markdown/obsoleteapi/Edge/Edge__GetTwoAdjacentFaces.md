---
title: "Edge::GetTwoAdjacentFaces"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Edge/Edge__GetTwoAdjacentFaces.htm"
---

# Edge::GetTwoAdjacentFaces

This method is obsolete and has been superseded by [Edge::GetTwoAdjacentFaces2](sldworksAPI.chm::/Edge/Edge__IGetTwoAdjacentFaces2.htm).

Description

This method returns the two adjacent faces to an edge.

Syntax (OLE Automation)

retval = Edge.GetTwoAdjacentFaces ()

| Return: | (VARIANT) retval | VARIANT containing a SafeArray of two Dispatch pointers to the two faces |
| --- | --- | --- |

Syntax (COM)

status = Edge->IGetTwoAdjacentFaces ( &face1, &face2 )

| Output: | (LPFACE) face1 | Pointer to the first adjacent face |
| --- | --- | --- |
| Output: | (LPFACE) face2 | Pointer to the second adjacent face |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call this method for body-related edges, not reference curve or sketch edges.

This method returns two faces only if the body is a solid body. If it is not, then the Dispatch version returns VT_EMPTY and the COM version returns S_FALSE.
