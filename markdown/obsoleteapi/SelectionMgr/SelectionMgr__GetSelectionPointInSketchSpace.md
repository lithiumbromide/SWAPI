---
title: "SelectionMgr::GetSelectionPointInSketchSpace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectionPointInSketchSpace.htm"
---

# SelectionMgr::GetSelectionPointInSketchSpace

This method is obsolete and has been superseded by [SelectionMgr::GetSelectionPointInSketchSpace2](sldworksAPI.chm::/SelectionMgr/SelectionMgr__GetSelectionPointInSketchSpace2.htm).

Description

This method gets the selection point projected onto the active sketch and returned in sketch space. The selection point is projected onto the currently active sketch, resulting in a Z value, which is always 0.00.

Syntax (OLE Automation)

retval = SelectionMgr.GetSelectionPointInSketchSpace ( AtIndex)

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z) |

Syntax (COM)

status = SelectionMgr->IGetSelectionPointInSketchSpace ( AtIndex, retval )

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles, the X,Y,Z selection point |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If a sketch is not currently active, then the return value is the same as that returned by SelectionMgr::GetSelectionPoint. You can determine if a sketch is active by checking for a NULL return value from ModelDoc2::GetActiveSketch2. In Visual Basic, check for Nothing. For example:

```vb
If (Part.GetActiveSketch Is Nothing) Then
swApp.SendMsgToUser "No Active sketch" ' No sketch is active
End If
```
