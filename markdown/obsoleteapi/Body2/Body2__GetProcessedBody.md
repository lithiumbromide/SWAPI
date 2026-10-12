---
title: "Body2::GetProcessedBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__GetProcessedBody.htm"
---

# Body2::GetProcessedBody

This method is obsolete and has been superseded by [Body2::GetProcessedBody2](sldworksAPI.chm::/Body2/Body2__GetProcessedBody2.htm).

Description

This method pre-processes the geometry of a body so that:

- Closed periodic faces (for example, the lateral face of a cylinder) are split into two faces.
- Faces that straddle the seam, if any, of the underlying surface are split into two faces.

Syntax (OLE Automation)

retval = Body2.GetProcessedBody ( )

| Return: | (LPDISPATCH) retval | Pointer to dispatch object, a body; this body is a processed copy of the body for this part |
| --- | --- | --- |

Syntax (COM)

status = Body2->IGetProcessedBody ( &retval )

| Output: | (LPBODY2) retval | Pointer to the body; this body is a processed copy of the body for this part |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

Pre-processing (for example, IGES) is sometimes necessary for exporting to systems that have difficulty with periodic conditions.
