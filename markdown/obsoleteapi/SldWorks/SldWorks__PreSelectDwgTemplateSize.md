---
title: "SldWorks::PreSelectDwgTemplateSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__PreSelectDwgTemplateSize.htm"
---

# SldWorks::PreSelectDwgTemplateSize

This method is obsolete and has been superseded by [SldWorks::PresetNewDrawingParameters](sldworksAPI.chm::/SldWorks/SldWorks__PresetNewDrawingParameters.htm) and [SldWorks::ResetPresetDrawingParameters](sldworksAPI.chm::/SldWorks/SldWorks__ResetPresetDrawingParameters.htm).

Description

This method establishes which template to use when creating a drawing. By calling this method and specifying a template size, no dialog appears when the end-user interactively selects File, New, Drawing.

Syntax (OLE Automation)

void SldWorks.PreSelectDwgTemplateSize ( templateToUse, templateName)

| Input: | (long) templateToUse | Type of template to use as defined in swDwgTemplates_e |
| --- | --- | --- |
| Input: | (BSTR) templateName | Reserved for future use; use NULL |

Syntax (COM)

status = SldWorks->PreSelectDwgTemplateSize ( templateToUse, templateName )

| Input: | (long) templateToUse | Type of template to use as defined in swDwgTemplates_e |
| --- | --- | --- |
| Input: | (BSTR) templateName | Reserved for future use; use NULL |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
