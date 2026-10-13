---
title: "Body2::MatchedBoolean3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__MatchedBoolean3.htm"
---

# Body2::MatchedBoolean3

This method is obsolete and has been superseded by [Body2::MatchedBoolean4](sldworksAPI.chm::/Body2/Body2__MatchedBoolean4.htm).

Description

This method performs a matched boolean on the specified bodies and supports an optional list of faces that match exactly.

Syntax (OLE Automation)

retval = Body2.MatchedBoolean3 ( operationType, toolBody, numOfMatchingFaces, faceList1, faceList2, errorCode )

| Input: | (int) operationType | One of the following operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (VARIANT) toolBody | Array of bodies |
| Input: | (long) numOfMatchingFaces | Number of matching faces |
| Input: | (VARIANT) faceList1 | First face list (see Remarks ) |
| Input: | (VARIANT) faceList2 | Second face list (see Remarks ) |
| Output: | (long) errorCode | Error indicator as defined in swBodyOperationError_e |
| Output: | (VARIANT) retval | Array of bodies formed by the operation |

Syntax (COM)

status = Body2->IMatchedBoolean3 ( operationType, toolBodyCount, toolBodyArr, numOfMatchingFaces, faceList1, faceList2, &errorCode, &retval )

| Input: | (int) operationType | One of these operation types: SWBODYADD SWBODYCUT SWCODYINTERSECT |
| --- | --- | --- |
| Input: | (long) toolBodyCount | Number of bodies |
| Input: | (LPBODY2*) toolBodyArr | Array of bodies of size toolBodyCount |
| Input: | (long) numOfMatchingFaces | Number of matching faces |
| Input: | (LPFACE2*) faceList1 | First face list (see Remarks ) |
| Input: | (LPFACE2*) faceList2 | Second face list (see Remarks ) |
| Output: | (long) errorCode | Error indicated as defined in swBodyOperationError_e |
| Output: | (LPENUMBODIES2) retval | Pointer to the EnumBodies2 object for a list of matches |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The concept of match means that the caller tells the boolean operator beforehand which faces can be considered to coincide. Basically, the caller performs part of the boolean operation.

Sometimes the application knows that two faces match because of the way the bodies are constructed; i.e., the application knows which faces are intended to match.

Having a list of matching face pairs may allow the matched boolean operator to resolve other geometric operations that otherwise it would not be able to work out. In general, providing matched faces speeds up the boolean operation and makes results more reliable.

The arguments faceList1 and faceList2 arguments can be empty lists. If matching face pairs are passed in, these faces must match such that:

- the surface geometry is coinciding.
- for each edge in a face, there is an edge in the other face that coincides.

This method supports multibody parts.
