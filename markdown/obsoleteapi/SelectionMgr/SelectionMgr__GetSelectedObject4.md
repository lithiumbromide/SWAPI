---
title: "SelectionMgr::GetSelectedObject4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectedObject4.htm"
---

# SelectionMgr::GetSelectedObject4

This method is obsolete and has been superseded by [SelectionMgr::GetSelectedObject5](SelectionMgr__GetSelectedObject5.htm).

Description

This method gets the selected object.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectedObject4 ( AtIndex )

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | ( LPDISPATCH ) retval | Pointer to the Dispatch object as defined in swSelType_e; NULL may be returned if type is not supported or if nothing is selected |

Syntax (COM)

status = SelectionMgr->IGetSelectedObject4 ( AtIndex, &retval )

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | ( LPUNKNOWN ) retval | Pointer to the Dispatch object as defined in swSelType_e; NULL may be returned if type is not supported or if nothing is selected |
| Return: | ( HRESULT ) status | S_OK if successful |

Remarks
