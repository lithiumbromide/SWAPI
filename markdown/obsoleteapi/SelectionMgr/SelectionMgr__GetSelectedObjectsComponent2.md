---
title: "SelectionMgr::GetSelectedObjectsComponent2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectedObjectsComponent2.htm"
---

# SelectionMgr::GetSelectedObjectsComponent2

This method is obsolete and has been superseded by [SelectionMgr::GetSelectedObjectsComponent3](sldworksAPI.chm::/SelectionMgr/SelectionMgr__GetSelectedObjectsComponent3.htm).

Description

This method gets the component of the selected object in assembly mode.

Syntax (OLE Automation)

component = SelectionMgr.GetSelectedObjectsComponent2 ( atIndex )

| Input: | (long) atIndex | Index position with in the current list of selected items, where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPDISPATCH) component | Pointer to the Dispatch object for the selected object (see Remarks ) |

Syntax (COM)

status = SelectionMgr->IGetSelectedObjectsComponent2 ( atIndex, &component )

| Input: | (long) atIndex | Index position with in the current list of selected items, where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (LPCOMPONENT2) component | Pointer to the selected object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

| If SelectionMgr object obtained from... | Then this method returns... |
| --- | --- |
| Assembly document | Component2 object For example, if a face on a component in the assembly is selected, then the component that contains that face is returned. |
| Drawing document | Selected DrawingComponent object |
| Part document | NULL |

NOTE: The index starts a 1, even when using C++.
