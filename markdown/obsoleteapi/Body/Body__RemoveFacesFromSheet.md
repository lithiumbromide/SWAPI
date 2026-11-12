---
title: "Body::RemoveFacesFromSheet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__RemoveFacesFromSheet.htm"
---

# Body::RemoveFacesFromSheet

This method is obsolete and has been superseded by [Body2::RemoveFacesFromSheet](sldworksAPI.chm::/Body2/Body2__RemoveFacesFromSheet.htm).

Description

This method removes the specified faces from a sheet body.

Syntax (OLE Automation)

void Body.RemoveFacesFromSheet ( numOfFaces, facesToRemove)

| Input: | (long) numOfFaces | Number of edges generated when these two bodies are intersected |
| --- | --- | --- |
| Input: | (VARIANT) facesToRemove | VARIANT of type SafeArray of dispatch objects, the faces to remove |

Syntax (COM)

status = Body->IRemoveFacesFromSheet ( numOfFaces, facesToRemove )

| Input: | (long) numOfFaces | Number of edges generated when these two bodies are intersected |
| --- | --- | --- |
| Input: | (LPFACE*) facesToRemove | Pointer to an array of the face objects to remove |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
