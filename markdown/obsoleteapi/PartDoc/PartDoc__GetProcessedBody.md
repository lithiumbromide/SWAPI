---
title: "PartDoc::GetProcessedBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__GetProcessedBody.htm"
---

# PartDoc::GetProcessedBody

The OLE version of this method is obsolete and has been superseded by [Body2::GetProcessedBody](../Body2/Body2__GetProcessedBody.htm).

The COM version of this method is obsolete and has been superseded by [PartDoc::IGetProcessedBody2](sldworksAPI.chm::/PartDoc/PartDoc__IGetProcessedBody2.htm).

Description

This method preprocesses the geometry of a body so that:

- Closed periodic faces are split into two faces (for example, the lateral face of a cylinder).
- Any faces that straddle the seam of the underlying surface are split into two faces.

Syntax (OLE Automation)

retval = PartDoc.GetProcessedBody ()

| Return: | (LPDISPATCH) retval | Pointer to dispatch object, a body, which is a copy of the body for this part |
| --- | --- | --- |

Syntax (COM)

status = PartDoc->IGetProcessedBody ( &retval )

| Output: | (LPBODY) retval | Pointer to the body, which is a copy of the body for this part |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This type of preprocessing is sometimes necessary (for example, IGES) for exporting to systems that have difficulty with periodic conditions .
