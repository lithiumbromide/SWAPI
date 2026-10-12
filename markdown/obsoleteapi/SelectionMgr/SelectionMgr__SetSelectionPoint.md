---
title: "SelectionMgr::SetSelectionPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__SetSelectionPoint.htm"
---

# SelectionMgr::SetSelectionPoint

This method is obsolete and has been superseded by [SelectionMgr::SetSelectionPoint2](sldworksAPI.chm::/SelectionMgr/SelectionMgr__SetSelectionPoint2.htm).

Description

This method sets the selection point in model space.

Syntax (OLE Automation)

retval = SelectionMgr.SetSelectionPoint ( AtIndex, x, y, z )

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount. |
| --- | --- | --- |
| Input: | (double) x | x location of the selection point |
| Input: | (double) y | y location of the selection point |
| Input: | (double) z | z location of the selection point |
| Output: | (VARIANT_BOOL) retval | TRUE if the position of the selection point is set, FALSE if not |

Syntax (COM)

status = SelectionMgr->SetSelectionPoint ( AtIndex, x, y, z, &retval )

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount. |
| --- | --- | --- |
| Input: | (double) x | x location of the selection point |
| Input: | (double) y | y location of the selection point |
| Input: | (double) z | z location of the selection point |
| Output: | (VARIANT_BOOL) retval | TRUE if the position of the selection point is set, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method allows an application to provide an XYZ position to a selected object at the given index in the SelectionMgr. This XYZ position represents a world-coordinate location in the context of that SelectionMgr.
