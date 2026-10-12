---
title: "Face::GetFirstLoop"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetFirstLoop.htm"
---

# Face::GetFirstLoop

This method is obsolete and has been superseded by [Face2::GetFirstLoop](sldworksAPI.chm::/Face2/Face2__GetFirstLoop.htm).

Description

This method returns the first loop in the face.

Syntax (OLE Automation)

retval = Face.GetFirstLoop ()

| Return: | (LPDISPATCH) retval | Dispatch pointer to the first loop |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetFirstLoop ( &retval )

| Output: | (LPLOOP) retval | Pointer to the first loop |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The first loop in the face is not necessarily the outer loop.
