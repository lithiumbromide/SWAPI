---
title: "Body::DraftBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__DraftBody.htm"
---

# Body::DraftBody

This method is obsolete and has been superseded by [Body2::DraftBody](../Body2/Body2__DraftBody.htm).

Description

This method adds a draft angle to a set of faces on a temporary body. Note that the body itself is modified.

Syntax (OLE Automation)

retval = Body.DraftBody ( numOfEnts, faceList, edgeList, draftAngle, dir )

| Input: | (long) numOfEnts | Number of faces to draft |
| --- | --- | --- |
| Input: | (VARIANT) faceList | List of pointers to the faces |
| Input: | (VARIANT) edgeList | List of pointers to the reference edges, one for each face, along which the draft is applied |
| Input: | (double) draftAngle | Draft angle |
| Input: | (VARIANT) dir | VARIANT of type SafeArray of 3 doubles (x,y,z), a vector which specifies the direction of the draft |
| Return: | (BOOL) retval | TRUE if draft successfully applied, FALSE if not |

Syntax (COM)

status = Body->IDraftBody ( numOfEnts, faceList, edgeList, draftAngle, dir, &retval )

| Input: | (long) numOfEnts | Number of faces to draft |
| --- | --- | --- |
| Input: | (LPFACE*) faceList | List of pointers to the faces |
| Input: | (LPEDGE*) edgeList | List of pointers to the reference edges, one for each face, along which the draft is applied |
| Input: | (double) draftAngle | Draft angle |
| Input: | (double*) dir | Pointer to an array of 3 doubles (x,y,z), a vector which specifies the direction of the draft |
| Output: | (VARIANT_BOOL) retval | TRUE if draft successfully applied, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
