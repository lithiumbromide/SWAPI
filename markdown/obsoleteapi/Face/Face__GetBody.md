---
title: "Face::GetBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetBody.htm"
---

# Face::GetBody

This method is obsolete and has been superseded by [Face2::GetBody](sldworksAPI.chm::/Face2/Face2__GetBody.htm).

Description

This method gets the body containing this face.

Syntax (OLE Automation)

retval = Face.GetBody ()

| Return: | (LPDISPATCH) retval | Dispatch pointer to the body |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetBody ( &Body )

| Output: | (LPBODY) Body | Pointer to the body |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |
