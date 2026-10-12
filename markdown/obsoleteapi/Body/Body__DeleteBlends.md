---
title: "Body::DeleteBlends"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__DeleteBlends.htm"
---

# Body::DeleteBlends

This method is obsolete and has been superceded by [Body::DeleteBlends2](Body__DeleteBlends2.htm)

Description

This method removes a set of fillet faces from a temporary body and heals the body.

Syntax (OLE Automation)

retval = Body.DeleteBlends ( VARIANT faceList )

| Input: | (VARIANT) faceList | SafeArray of blend faces to delete |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successful, FALSE if error |

Syntax (COM)

status = Body->DeleteBlends ( long numOfFaces, LPFACE* faceList, VARIANT_BOOL &retval )

| Input: | (long) numOfFaces | Number of faces in array |
| --- | --- | --- |
| Input: | (LPFACE*) faceList | List of Face objects to delete |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if error |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The body is modified.
