---
title: "SelectionMgr::GetSelectedObject5"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectedObject5.htm"
---

# SelectionMgr::GetSelectedObject5

This method is obsolete and has been superseded by [SelectionMgr::GetSelectedObject6](sldworksAPI.chm::/SelectionMgr/SelectionMgr__GetSelectedObject6.htm).

Description

This method gets the selected object.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectedObject5 ( AtIndex )

| Input: | (long) AtIndex | Index position within the current list of selected items, where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPDISPATCH) retval | Pointer to the Dispatch object as defined in swSelectType_e; NULL may be returned if type is not supported or if nothing is selected |

Syntax (COM)

status = SelectionMgr->GetSelectedObject5 ( AtIndex, &retval )

| Input: | (long) AtIndex | Index position with in the current list of selected items, where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPDISPATCH) retval | Pointer to the Dispatch object as defined in swSelectType_e; NULL may be returned if type is not supported or if nothing is selected |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

| If... | Then this method returns... |
| --- | --- |
| Reference surfaces are selected in the graphics view | Reference surface faces instead of the entire reference surface feature |
| Dimensions are selected in the graphics view | DisplayDimension object instead of the Dimension object |
| SelectionMgr object obtained from a drawing document | Selected DrawingComponent object |
| SelectionMgr object obtained from a part or assembly document | Component2 object |
