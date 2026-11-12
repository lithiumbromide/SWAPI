---
title: "Loop::EnumEdges"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Loop/Loop__EnumEdges.htm"
---

# Loop::EnumEdges

This method is obsolete and has been superseded by [Loop2::EnumEdges](sldworksAPI.chm::/Loop2/Loop2__EnumEdges.htm).

Description

This method enumerates the edges in a face.

Syntax (OLE Automation)

See Loop::GetEdges.

Syntax (COM)

status = Loop->EnumEdges ( &retval )

| Output: | (LPENUMEDGES) retval | Pointer to the enumerated list of edges |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The edge objects are returned in a CW or CCW manner based on the direction of the loop.

The loop direction is determined as follows: if a loop is viewed along its direction with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, see Loop::IsOuter.

Because an edge is shared by multiple loops, the edge direction might be opposite to the direction of the loop. To check this, use Edge::EdgeInFaceSense.
