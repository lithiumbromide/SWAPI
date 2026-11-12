---
title: "Body::GetProcessedBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetProcessedBody.htm"
---

# Body::GetProcessedBody

This method is obsolete and has been superseded by [Body2::GetProcessedBody2](sldworksAPI.chm::/Body2/Body2__GetProcessedBody2.htm).

Description

This method pre-processes the geometry of a body so that:

- Closed periodic faces (for example, the lateral face of a cylinder) are split into two faces.
- Faces that straddle the seam, if any, of the underlying surface are split into two faces.

Syntax (OLE Automation)

retval = Body.GetProcessedBody ( )

| Return: | (LPDISPATCH) retval | Pointer to Dispatch object, a body; this body is a copy of the body for this part, processed as previously described |
| --- | --- | --- |

Syntax (COM)

status = Body->IGetProcessedBody ( &retval )

| Output: | (LPBODY) retval | Pointer to the body; this body is a copy of the body for this part, processed as previously described |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Such pre-processing is sometimes necessary (for example, IGES), for exporting into systems that have difficulty with periodic conditions.
