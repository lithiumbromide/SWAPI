---
title: "Body::MatchedBoolean"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__MatchedBoolean.htm"
---

# Body::MatchedBoolean

This method is obsolete and has been superseded by [Body2::MatchedBoolean](../Body2/Body2__MatchedBoolean.htm).

Description

This method performs a matched boolean on the specified faces.

Syntax (OLE Automation)

retval = Body.MatchedBoolean ( operationType, toolBody, numOfMatchingFaces, faceList1, faceList2, errorCode )

| Input: | (int) operationType | One of the following operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (LPDISPATCH) toolBody | Pointer to the tool body |
| Input: | (long) numOfMatchingFaces | Number of matching faces |
| Input: | (VARIANT) faceList1 | First face list |
| Input: | (VARIANT) faceList2 | Second face list |
| Output: | (long) errorCode | Error indicator as defined in swBodyOperationError_e |
| Output: | (VARIANT) retval | SafeArray containing a set of pointers for the resulting matches |

Syntax (COM)

status = Body->IMatchedBoolean ( operationType, toolBody, numOfMatchingFaces, faceList1, faceList2, &errorCode, &retval )

| Input: | (int) operationType | One of the following operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (LPBODY) toolBody | Pointer to the tool body |
| Input: | (long) numOfMatchingFaces | Number of matching faces |
| Input: | (LPFACE*) faceList1 | First face list |
| Input: | (LPFACE*) faceList2 | Second face list |
| Output: | (long) errorCode | Error indicator as defined in swBodyOperationError_e |
| Output: | (LPENUMBODIES) retval | Pointer to an EnumBodies2 object for the resulting matches |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
