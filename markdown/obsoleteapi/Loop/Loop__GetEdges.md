---
title: "Loop::GetEdges"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Loop/Loop__GetEdges.htm"
---

# Loop::GetEdges

This method is obsolete and has been superseded by [Loop2::GetEdges](sldworksAPI.chm::/Loop2/Loop2__GetEdges.htm).

Description

This method returns all of the edges in the loop.

Syntax (OLE Automation)

retval = Loop.GetEdges ()

| Return: | (VARIANT) retval | SafeArray of dispatch pointers to all the edges that make up the loop |
| --- | --- | --- |

Syntax (COM)

status = Loop->IGetEdges ( &EdgeList )

| Output: | (LPEDGE*) EdgeList | Pointer to the list of edges which make up the loop |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The edge objects are returned in a CW or CCW manner based on the direction of the loop.

The loop direction is determined as follows: if a loop is viewed along its direction, with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, see [Loop::IsOuter](Loop__IsOuter.htm).

Because an edge is shared by multiple loops, the edge direction may be opposite to the direction of the loop. To check this, see Edge::EdgeInFaceSense.
