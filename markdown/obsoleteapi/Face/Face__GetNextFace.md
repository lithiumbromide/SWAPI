---
title: "Face::GetNextFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetNextFace.htm"
---

# Face::GetNextFace

This method is obsolete and has been superseded by [Face2::GetNextFace](sldworksAPI.chm::/Face2/Face2__GetNextFace.htm).

Description

This method finds the next face in a body.

Syntax (OLE Automation)

retval = Face.GetNextFace ()

| Return: | (LPDISPATCH) retval | Dispatch pointer to the next face in a body |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetNextFace ( &retval )

| Output: | (LPFACE) retval | Pointer to the next face in a body |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |
