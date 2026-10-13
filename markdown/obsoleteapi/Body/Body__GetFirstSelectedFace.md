---
title: "Body::GetFirstSelectedFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetFirstSelectedFace.htm"
---

# Body::GetFirstSelectedFace

This method is obsolete and has been superseded by [Body2::GetFirstSelectedFace.](sldworksAPI.chm::/Body2/Body2__GetFirstSelectedFace.htm)

Description

This method is used in combination with Body::GetProcessedBodyWithSelFace and is intended for IGES type routines.

Syntax (OLE Automation)

retval = Body.GetFirstSelectedFace ()

| Return: | (LPDISPATCH) retval | Pointer to dispatch object, the first selected face |
| --- | --- | --- |

Syntax (COM)

status = Body->IGetFirstSelectedFace ( &retval )

| Output: | (LPFACE) retval | Pointer to the first selected face |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Do not use this method for general selection handling. To handle items selected by the user or items selected with ModelDoc2::SelectByID, use SelectionMgr::GetSelectedObject2.
