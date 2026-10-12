---
title: "Loop::EnumCoEdges"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Loop/Loop__EnumCoEdges.htm"
---

# Loop::EnumCoEdges

This method is obsolete and has been superseded by [Loop2::EnumCoEdges](sldworksAPI.chm::/Loop2/Loop2__EnumCoEdges.htm).

Description

This method enumerates the coedges in a loop.

Syntax (OLE Automation)

See Loop::GetFirstCoEdge.

Syntax (COM)

status = Loop->EnumCoEdges ( &retval )

| Output: | (LPENUMCOEDGES) retval | Pointer to the enumerated list of coedges |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The CoEdge objects are returned in a CW or CCW manner based on the direction of the loop.

The loop direction is determined as follows: if a loop is viewed along its direction with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, use Loop::IsOuter.

The coedge direction always aligns with the direction of the loop.
