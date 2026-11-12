---
title: "Body2::DraftBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__DraftBody.htm"
---

# Body2::DraftBody

This body is obsolete and has been superseded by [Body2::DraftBody2](sldworksAPI.chm::/Body2/Body2__DraftBody2.htm).

Description

This method adds a draft angle to a set of faces on a temporary body. This method modifies the body.

Syntax (OLE Automation)

retval = Body2.DraftBody ( numOfEnts, faceList, edgeList, draftAngle, dir )

| Input: | (long) numOfEnts | Number of faces to draft |
| --- | --- | --- |
| Input: | (VARIANT) faceList | List of pointers to the faces |
| Input: | (VARIANT) edgeList | List of pointers to the reference edges, one for each face, along which the draft is applied |
| Input: | (double) draftAngle | Draft angle |
| Input: | (VARIANT) dir | VARIANT of type SafeArray of 3 doubles (x,y,z), a vector which specifies the direction of the draft |
| Return: | (BOOL) retval | TRUE if draft successfully applied, FALSE if not |

Syntax (COM)

status = Body2->IDraftBody ( numOfEnts, faceList, edgeList, draftAngle, dir, &retval )

| Input: | (long) numOfEnts | Number of faces to draft |
| --- | --- | --- |
| Input: | (LPFACE*) faceList | List of pointers to the faces |
| Input: | (LPEDGE*) edgeList | List of pointers to the reference edges, one for each face, along which the draft is applied |
| Input: | (double) draftAngle | Draft angle |
| Input: | (double*) dir | Pointer to an array of 3 doubles (x,y,z), a vector which specifies the direction of the draft |
| Output: | (VARIANT_BOOL) retval | TRUE if draft successfully applied, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
