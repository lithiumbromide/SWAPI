---
title: "SelectionMgr::GetSelectedObjectType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectedObjectType.htm"
---

# SelectionMgr::GetSelectedObjectType

This method is obsolete and has been superseded by [SelectionMgr::GetSelectedObjectType2](SelectionMgr__GetSelectedObjectType2.htm).

Description

This method gets the type of selected object.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectedObjectType ( AtIndex)

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (long) retval | Type of object as defined in swSelectType_e |

Syntax (COM)

status = SelectionMgr->GetSelectedObjectType ( AtIndex, &retval )

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (long) retval | Type of object as defined in swSelectType_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The index starts at 1, even when using C++.
