---
title: "Body::GetNextSelectedFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetNextSelectedFace.htm"
---

# Body::GetNextSelectedFace

This method is obsolete and has been superseded by [Body2::GetNextSelectedFace](sldworksAPI.chm::/Body2/Body2__GetNextSelectedFace.htm).

Description

This method gets the next selected face and is used with Body::GetProcessedBodyWithSelFace. This method is intended for IGES routines.

Syntax (OLE Automation)

retval = Body.GetNextSelectedFace ()

| Return: | (LPDISPATCH) retval | Pointer to dispatch object, the selected face |
| --- | --- | --- |

Syntax (COM)

status = Body->IGetNextSelectedFace ( &retval )

| Output: | (LPFACE*) retval | Pointer to the selected face |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Do not use this method for general selection handling. If you want to get items selected by the user or items selected with [ModelDoc2::SelectByID](../ModelDoc2/ModelDoc2__SelectByID.htm), use [SelectionMgr::GetSelectedObject2](../SelectionMgr/SelectionMgr__GetSelectedObject2.htm).
