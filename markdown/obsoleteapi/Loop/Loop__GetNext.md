---
title: "Loop::GetNext"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Loop/Loop__GetNext.htm"
---

# Loop::GetNext

This method is obsolete and has been superseded by [Loop2::GetNext](sldworksAPI.chm::/Loop2/Loop2__GetNext.htm).

Description

This method returns the next loop on the face.

Syntax (OLE Automation)

retval = Loop.GetNext ()

| Return: | (LPDISPATCH) retval | Pointer to the Dispatch object, the next loop, NULL if it is the last loop |
| --- | --- | --- |

Syntax (COM)

status = Loop->IGetNext ( &retval )

| Output: | (LPLOOP) retval | Pointer to next loop, NULL if it is the last loop |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |
