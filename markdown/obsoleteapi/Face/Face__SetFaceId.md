---
title: "Face::SetFaceId"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__SetFaceId.htm"
---

# Face::SetFaceId

This method is obsolete and has been superseded by [Face2::SetFaceId](sldworksAPI.chm::/Face2/Face2__SetFaceId.htm).

Description

This method sets the face ID on an imported body.

Syntax (OLE Automation)

(void) Face.SetFaceId (int idIn)

| Input: | (int) idIn | Face ID |
| --- | --- | --- |

Syntax (COM)

status = Face-> SetFaceId ( idIn)

| Input: | (int) idIn | Face ID |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

SolidWorks uses this ID to track the specific faces of imported bodies (for example, IGES imports).

The face ID is a persistent and is saved with the document. The face ID can be changed by any third party application. The intent is that you assign an ID to a particular face so that you can refer to that face within your application. Each ID must be unique, so it is best to let SolidWorks assign IDs for you when an imported body or surface is created.

To store data with a face, use the Attribute object.
