---
title: "Body::GetIntersectionEdges"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetIntersectionEdges.htm"
---

# Body::GetIntersectionEdges

This method is obsolete and has been superseded by [Body2::GetIntersectionEdges](sldworksAPI.chm::/Body2/Body2__GetIntersectionEdges.htm).

Description

This method gets the intersection edges between two temporary bodies.

Syntax (OLE Automation)

retval = Body.GetIntersectionEdges ( toolBodyIn)

| Input: | (LPDISPATCH) toolBodyIn | Pointer to dispatch object, the temporary body object that is used to perform the intersection |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of an array of pointers to dispatch objects |

Syntax (COM)

status = Body->IGetIntersectionEdges ( toolBodyIn, &EdgeListOut )

| Input: | (LPBODY) toolBodyIn | Pointer to dispatch object, the temporary body object that is used to perform the intersection |
| --- | --- | --- |
| Output: | (LPEDGE*) EdgeListOut | Pointer to an array of edge objects |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method imprints a set of edges on both of the specified temporary bodies. Then, this function returns the edges in an alternating list. The total number of edges contained in this array is two times the value returned from Body::IGetIntersectionEdgeCount:

[Edge1imprintedOnTarget, Edge1imprintedOnTool, Edge2imprintedOnTarget, Edge2imprintedOnTool]

where the target body is the body object used to call this method and the tool body is passed into this function as the first argument.

This method returns an unordered list of edges that might or might not form continuous closed loops. In the case of a tangency condition (for example, a planar face contacting the cylindrical face of a cylinder), this method returns a single edge along the tangency.

You could also use Body::Operations to provide an adequate solution. Body::Operations is similar to this method and allows you to intersect a sheet body with your target body.
