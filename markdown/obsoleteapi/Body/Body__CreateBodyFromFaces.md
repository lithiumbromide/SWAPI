---
title: "Body::CreateBodyFromFaces"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateBodyFromFaces.htm"
---

# Body::CreateBodyFromFaces

This method is obsolete and has been superseded by [Body2::CreateBodyFromFaces](sldworksAPI.chm::/Body2/Body2__CreateBodyFromFaces.htm).

Description

This method creates a temporary body object from the given faces.

Syntax (OLE Automation)

retval = Body.CreateBodyFromFaces ( NumOfFaces, FaceList)

| Input: | (long) NumOfFaces | Number of faces to use for body creation |
| --- | --- | --- |
| Input: | (VARIANT) FaceList | VARIANT containing the faces to use for body creation |
| Return: | (LPDISPATCH) retval | Pointer to dispatch object, the body |

Syntax (COM)

status = Body->ICreateBodyFromFaces ( NumOfFaces, FaceList, &retval )

| Input: | (long) NumOfFaces | Number of faces to use for body creation |
| --- | --- | --- |
| Input: | (VARIANT) FaceList | VARIANT containing the faces to use for body creation |
| Output: | (LPBODY) retval | Pointer to the body |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
