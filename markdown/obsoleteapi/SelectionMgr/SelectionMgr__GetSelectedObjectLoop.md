---
title: "SelectionMgr::GetSelectedObjectLoop"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectedObjectLoop.htm"
---

# SelectionMgr::GetSelectedObjectLoop

This method is obsolete and has been superseded by [SelectionMgr::GetSelectedObjectLoop2](sldworksAPI.chm::/SelectionMgr/SelectionMgr__GetSelectedObjectLoop2.htm).

Description

This method gets the loop, if selected, for the selected edge.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectedObjectLoop ( AtIndex)

| Input: | (long) AtIndex | Index position within the current list of selected items, where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPLOOP2) retval | Pointer to the Loop2 object |

Syntax (COM)

status = SelectionMgr->GetSelectedObjectLoop ( AtIndex, &retval)

| Input: | (long) AtIndex | Index position within the current list of selected items, where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPLOOP2) retval | Pointer to the Loop2 object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If a loop is not associated with an edge, then this method returns NULL.

NOTE: Use this method to find out if the selected edge has an associated loop. ModelDoc2::SelectLoop does not add an item to the SelectionMgr.
