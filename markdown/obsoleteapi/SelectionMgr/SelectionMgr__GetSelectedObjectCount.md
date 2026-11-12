---
title: "SelectionMgr::GetSelectedObjectCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectedObjectCount.htm"
---

# SelectionMgr::GetSelectedObjectCount

This method is obsolete and has been superseded by [SelectionMgr::GetSelectedObjectCount2](sldworksAPI.chm::/SelectionMgr/SelectionMgr__GetSelectedObjectCount2.htm).

Description

This method gets the number of selected objects. This method can be used to determine if the user has a made a valid selection.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectedObjectCount ()

| Return: | (long) retval | Number of currently selected objects |
| --- | --- | --- |

Syntax (COM)

status = SelectionMgr->GetSelectedObjectCount ( &retval )

| Output: | (long) retval | Number of currently selected objects |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
