---
title: "Loop::GetFirstCoEdge"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Loop/Loop__GetFirstCoEdge.htm"
---

# Loop::GetFirstCoEdge

This method is obsolete and has been superseded by [Loop2::GetFirstCoEdge](sldworksAPI.chm::/Loop2/Loop2__GetFirstCoEdge.htm).

Description

This method returns the first coedge of the loop.

Syntax (OLE Automation)

retval = Loop.GetFirstCoEdge ()

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the coedge |
| --- | --- | --- |

Syntax (COM)

status = Loop->IGetFirstCoEdge ( &retval )

| Output: | (LPCOEDGE) retval | Pointer to the coedge |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The CoEdge objects are returned in a CW or CCW manner based on the direction of the loop.

The loop direction is determined as follows: if a loop is viewed along its direction, with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, see [Loop::IsOuter](Loop__IsOuter.htm).

The coedge direction always aligns with the direction of the loop.
