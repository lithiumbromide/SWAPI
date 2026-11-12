---
title: "Body2::DeleteBlends"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__DeleteBlends.htm"
---

# Body2::DeleteBlends

This method is obsolete and has been superseded by [Body2::DeleteBlends2](sldworksAPI.chm::/Body2/Body2__DeleteBlends2.htm)

Description

This method removes a set of fillet faces from a temporary body and heals the body. The body itself is modified.

Syntax (OLE Automation)

retval = Body2.DeleteBlends ( VARIANT faceList )

| Input: | (VARIANT) faceList | SafeArray of blend faces to delete |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = Body2->DeleteBlends ( long numOfFaces, LPFACE* faceList, VARIANT_BOOL &retval )

| Input: | (long) numOfFaces | Number of faces in array |
| --- | --- | --- |
| Input: | (LPFACE*) faceList | List of faces of size numOfFaces to delete |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
