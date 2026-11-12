---
title: "Body::GetProcessedBodyWithSelFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetProcessedBodyWithSelFace.htm"
---

# Body::GetProcessedBodyWithSelFace

This method is obsolete and has been superseded by [Body2::GetProcessedBodyWithSelFace](sldworksAPI.chm::/Body2/Body2__GetProcessedBodyWithSelFace.htm).

Description

This method returns a pointer or dispatch pointer to a processed body.

Syntax (OLE Automation)

retval = Body.GetProcessedBodyWithSelFace ( )

| Return: | (LPDISPATCH) retval | Dispatch object for the body; this body is a copy of the body for this part |
| --- | --- | --- |

Syntax (COM)

status = Body->IGetProcessedBodyWithSelFace ( &retval )

| Output: | (LPBODY)retval | Pointer to the body; this body is a copy of the body for this part |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
