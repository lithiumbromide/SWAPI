---
title: "SelectionMgr::DeSelect"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__DeSelect.htm"
---

# SelectionMgr::DeSelect

This method is obsolete and has been superseded by [SelectionMgr::DeSelect2](sldworksAPI.chm::/SelectionMgr/SelectionMgr__DeSelect2.htm).

Description

This method deselects the specified selections.

Syntax (OLE Automation)

retval = SelectionMgr.DeSelect ( AtIndex )

| Input: | (VARIANT) AtIndex | VARIANT of type SafeArray of index positions within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (long) retval | TRUE if the deselection is successful, FALSE if not |

Syntax (COM)

status = SelectionMgr->IDeSelect ( AtIndex, &retval )

| Input: | (long) Count | Number of objects to deselect |
| --- | --- | --- |
|  | (long*) AtIndex | Array of indices for Count objects |
| Output: | (long) retval | TRUE if the deselection is successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks
