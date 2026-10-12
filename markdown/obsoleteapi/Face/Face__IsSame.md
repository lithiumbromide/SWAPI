---
title: "Face::IsSame"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__IsSame.htm"
---

# Face::IsSame

This method is obsolete and has been superseded by [Face2::IsSame](sldworksAPI.chm::/Face2/Face2__IsSame.htm).

Description

This method returns TRUE if the two faces are the same.

Syntax (OLE Automation)

retval = Face.IsSame ( faceIn)

| Input: | (LPDISPATCH) faceIn | Dispatch pointer to the face object to be compared |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the two faces are the same, FALSE if they are different |

Syntax (COM)

status = Face->IIsSame ( faceIn, &retval )

| Input: | (LPFACE) faceIn | Pointer to face to be compared |
| --- | --- | --- |
| Output: | (VARIANT_BOOL*) retval | TRUE if the two faces are the same, FALSE if they are different |
| Return: | (HRESULT)status | S_OK if successful |
