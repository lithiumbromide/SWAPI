---
title: "Body::DeleteBlends2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__DeleteBlends2.htm"
---

# Body::DeleteBlends2

This method is obsolete and has been superseded by [Body2::DeleteBlends2](sldworksAPI.chm::/Body2/Body2__DeleteBlends2.htm).

Description

This method deletes blend faces from an API-generated body.

Syntax (OLE Automation)

retval = Body2.DeleteBlends2 ( numOfFaces, faceList, doLocalCheck )

| Input: | (long) numOfFaces | Number of faces to delete |
| --- | --- | --- |
| Input: | (VARIANT) faceList | List of faces to delete |
| Input: | (BOOL) doLocalCheck | TRUE to perform a local check, FALSE to not |
| Return: | (BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = Body2->IDeleteBlends2 ( numOfFaces, faceList, doLocalCheck, &retval )

| Input: | (long) numOfFaces | Number of faces to delete |
| --- | --- | --- |
| Input: | (LPFACE) faceList | List of faces to delete of size numOfFaces |
| Input: | (VARIANT_BOOL) doLocalCheck | TRUE to perform a local check, FALSE if not |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
