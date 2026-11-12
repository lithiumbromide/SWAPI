---
title: "Body::GetFirstFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetFirstFace.htm"
---

# Body::GetFirstFace

This method is obsolete and has been superseded by [Body2::GetFirstFace](sldworksAPI.chm::/Body2/Body2__GetFirstFace.htm).

Description

This method finds the first face in a body and returns a pointer to the dispatch object or a pointer to the face.

Syntax (OLE Automation)

retval = Body.GetFirstFace ()

| Return: | (LPDISPATCH) retval | Pointer to dispatch object, the first face in a body |
| --- | --- | --- |

Syntax (COM)

status = Body->IGetFirstFace ( &retval )

| Output: | (LPFACE) retval | Pointer to the first face in a body |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
