---
title: "SelectionMgr::IsInEditTarget"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__IsInEditTarget.htm"
---

# SelectionMgr::IsInEditTarget

This method is obsolete and has been superseded by [SelectionMgr::IsInEditTarget2](sldworksAPI.chm::/SelectionMgr/SelectionMgr__IsInEditTarget2.htm).

Description

This method determines if the selected object is in the edit target. This is necessary in assemblies when the end-user performs in-context editing of a part. This method allows you to determine if a selected item belongs to the model that is the current edit target.

Syntax (OLE Automation)

retval = SelectionMgr.IsInEditTarget ( atIndex)

| Input: | (long) atIndex | Position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the selected item specified by AtIndex belongs to a model which is the current edit target, FALSE if not |

Syntax (COM)

status = SelectionMgr->IsInEditTarget ( atIndex, &retval )

| Input: | (long) atIndex | Position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the selected item specified by AtIndex belongs to a model which is the current edit target, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
