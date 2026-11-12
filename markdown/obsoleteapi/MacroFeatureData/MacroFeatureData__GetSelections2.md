---
title: "MacroFeatureData::GetSelections2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MacroFeatureData/MacroFeatureData__GetSelections2.htm"
---

# MacroFeatureData::GetSelections2

This method is obsolete and has been superseded by [MacroFeatureData::GetSelections3](sldworksAPI.chm::/MacroFeatureData/MacroFeatureData__GetSelections3.htm).

Description

This method gets the selected objects for the macro feature.

Syntax (OLE Automation)

void = MacroFeatureData.GetSelections2 ( objects, objectTypes, selMarks, drViews )

| Output: | (VARIANT) *objects | Array of selected objects |
| --- | --- | --- |
| Output: | (VARIANT) *objectTypes | Array of selected object types as defined in swSelectType |
| Output: | (VARIANT) *selMarks | Array of marks for the selected objects |
| Output: | (VARIANT) *drViews | Array of drawing views |

Syntax (COM)

status = MacroFeatureData->IGetSelections2 ( selCount, objects, objectTypes, selMarks, drViews )

| Input: | (long) selCount | Number of selected objects |
| --- | --- | --- |
| Output: | (LPDISPATCH) *objects | Array of selected object of size selCount |
| Output: | (long) *objectTypes | Array of the selected object types as defined in swSelectType_e of size selCount |
| Output: | (long) *selMarks | Array of marks associated with the selected objects of size selCount |
| Output: | (LPVIEW) *drViews | Array of drawing views of size selCount |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See Accessing Selections that Define Features for details on using this method.
