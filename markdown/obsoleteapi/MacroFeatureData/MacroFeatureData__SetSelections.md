---
title: "MacroFeatureData::SetSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MacroFeatureData/MacroFeatureData__SetSelections.htm"
---

# MacroFeatureData::SetSelections

This method is obsolete and has been superseded by [MacroFeatureData::SetSelections2](sldworksAPI.chm::/MacroFeatureData/MacroFeatureData__SetSelections2.htm).

Description

This method sets the selected objects for the macro feature.

Syntax (OLE Automation)

void = MacroFeatureData.SetSelections ( objects, selMarks )

| Input: | (VARIANT) objects | Array of object names |
| --- | --- | --- |
| Input: | (VARIANT) selMarks | Array of marks associated with the objects |

Syntax (COM)

status = MacroFeatureData->ISetSelections ( selCount, objects, selMarks )

| Input: | (long) selCount | Number of selected objects |
| --- | --- | --- |
| Input: | (LPDISPATCH*) objects | Array of size selCount containing the object names |
| Input: | (long) *selMarks | Array of size selCount containing the marks associated with the objects |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
