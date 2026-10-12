---
title: "MacroFeatureData::GetSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MacroFeatureData/MacroFeatureData__GetSelections.htm"
---

# MacroFeatureData::GetSelections

This method is obsolete and has been superseded by [MacroFeatureData::GetSelections2](MacroFeatureData__GetSelections2.htm).

Description

This method gets the selected objects for this macro feature.

Syntax (OLE Automation)

void = MacroFeatureData.GetSelections ( objects, objectTypes, selMarks )

| Output: | (VARIANT) *objects | Array of selected object names |
| --- | --- | --- |
| Output: | (VARIANT) *objectTypes | Array of object types of the selections as defined in swSelectType_e |
| Output: | (VARIANT) *selMarks | Array of marks associated with the selections |

Syntax (COM)

status = MacroFeatureData->IGetSelections ( selCount, objects, objectTypes, selMarks )

| Input: | (long) selCount | Number of selected objects |
| --- | --- | --- |
| Output: | (LPDISPATCH) *objects | Array of size selCount containing selected object names |
| Output: | (long) *objectTypes | Array of size selCount containing object types of the selections as defined in swSelectType_e |
| Output: | (long) *selMarks | Array of size selCount containing marks associated with the selections |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
