---
title: "SelectionMgr::GetSelectionPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectionPoint.htm"
---

# SelectionMgr::GetSelectionPoint

This method is obsolete and has been superseded by [SelectionMgr::GetSelectionPoint2](sldworksAPI.chm::/SelectionMgr/SelectionMgr__GetSelectionPoint2.htm).

Description

This method gets the selected point in model space coordinates from the currently selected object.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectionPoint ( AtIndex)

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z) |

Syntax (COM)

status = SelectionMgr->IGetSelectionPoint (AtIndex, retval )

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles, the x,y,z selection point |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The point returned from this method cannot lie on the object that was selected. For example, the end-user can select an edge when the edge is within the pick radius of their mouse cursor.

However, for face, edge, and vertex selection, you can get a point that is on the object by using that object's GetClosestPointOn method. To do this, get the Face2, Edge, or Vertex object using the SelectionMgr::GetSelectedObject5 method, and then use that object to call GetClosestPointOn. Pass the X,Y,Z values returned from SelectionMgr::GetSelectionPoint, and the GetClosestPointOn method will return the closest X,Y,Z point that is on the face, edge, or vertex.

If the selected object is sketch geometry, then the coordinates returned are in sketch space. The coordinates are 2D and related to the origin of the sketch that owns the selected geometry.

NOTE: The index starts at 1, even when using C++.
