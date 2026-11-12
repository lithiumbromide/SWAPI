---
title: "Face::RemoveFaceID"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__RemoveFaceID.htm"
---

# Face::RemoveFaceID

This method is obsolete and has been superseded by [Face2::RemoveFaceID](sldworksAPI.chm::/Face2/Face2__RemoveFaceID.htm).

Description

This method removes the face ID on an imported body.

Syntax (OLE Automation)

(void) Face.RemoveFaceID (int idIn)

| Return: | (int) idIn | Face ID |
| --- | --- | --- |

Syntax (COM)

status = Face-> RemoveFaceID ( idIn)

| Output: | (int) idIn | Face ID |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use [Face::SetFaceID](Face__SetFaceId.htm) to set the face ID.
