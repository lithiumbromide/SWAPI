---
title: "Body::GetSelectedFaceCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetSelectedFaceCount.htm"
---

# Body::GetSelectedFaceCount

This method is obsolete and has been superseded by [Body2::GetSelectedFaceCount](sldworksAPI.chm::/Body2/Body2__GetSelectedFaceCount.htm).

Description

This method gets the number of selected faces.

Syntax (OLE Automation)

retval = Body.GetSelectedFaceCount ()

| Return: | (long) retval | Number of selected faces |
| --- | --- | --- |

Syntax (COM)

status = Body->GetSelectedFaceCount ( &retval )

| Output: | (long) retval | Number of selected faces |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is used iwith [Body::GetProcessedBodyWithSelFace](Body__GetProcessedBodyWithSelFace.htm) and is intended for IGES routines.

Do not use this method for general selection handling. If you want to get items selected by the user or items selected with [ModelDoc::SelectByID](../ModelDoc/ModelDoc__SelectByID.htm), use SelectionMgr::GetSelectedObjectCount.
