---
title: "Face::IGetSilhoutteEdgeCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__IGetSilhoutteEdgeCount.htm"
---

# Face::IGetSilhoutteEdgeCount

This method is obsolete and has been superseded by [Face2::IGetSilhoutteEdgeCount](sldworksAPI.chm::/Face2/Face2__IGetSilhoutteEdgeCount.htm).

Description

This method gets the number of silhouette edges for this face.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Face->IGetSilhoutteEdgeCount ( root, normal, &ret )

| Input: | (double*) root | Array of doubles defining the root point |
| --- | --- | --- |
| Input: | (double*) normal | Array of doubles defining the direction vector |
| Output: | (long) ret | Number of silhouette edges |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For a given vector root point (root) and a vector direction (normal), this method calculates the number of edges that returned by [Face::IGetSilhoutteEdges](Face__GetSilhoutteEdges.htm).

The siledgesout array returned by [Face::IGetSilhoutteEdges](Face__GetSilhoutteEdges.htm) contains two elements for each edge: the silhouette edge and an unused parameter. To allocate data to hold the returned information, allocate double the elements returned by this method.
