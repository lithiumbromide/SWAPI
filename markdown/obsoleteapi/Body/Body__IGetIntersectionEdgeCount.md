---
title: "Body::IGetIntersectionEdgeCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__IGetIntersectionEdgeCount.htm"
---

# Body::IGetIntersectionEdgeCount

This method is obsolete and has been superseded by [Body2::IGetIntersectionEdgeCount](sldworksAPI.chm::/Body2/Body2__IGetIntersectionEdgeCount.htm).

Description

This method gets the number of intersection edges between this body and the specified tool body.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Body->IGetIntersectionEdgeCount ( toolBodyIn, &retval )

| Input: | (LPBODY) toolBodyIn | Pointer to the temporary body object used to perform the intersection |
| --- | --- | --- |
| Output: | (long) retval | Number of edges generated when these two bodies intersect |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can use the return value from this method with [Body::GetIntersectionEdges](Body__GetIntersectionEdges.htm).
