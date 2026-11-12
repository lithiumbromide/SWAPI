---
title: "DrawingDoc::SetupSheet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__SetupSheet.htm"
---

# DrawingDoc::SetupSheet

This method is obsolete and has been superseded by [DrawingDoc::SetupSheet2](DrawingDoc__SetupSheet2.htm).

Description

This method changes the settings for the current sheet on this drawing.

Syntax (OLE Automation)

void DrawingDoc.SetupSheet ( name, paperSize, templateIn, scale1, scale2)

| Input: | (BSTR) name | Name for the sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |

Syntax (COM)

status = DrawingDoc->SetupSheet ( name, paperSize, templateIn, scale1, scale2 )

| Input: | (BSTR) name | Name for the sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can also use Sheet::SetProperties, Sheet::SetName, and Sheet::SetTemplateName.

This method does not support paperSize = swDwgPapersUserDefined or templateIn = swDwgTemplateCustom. See DrawingDoc::SetupSheet2.

The templateIn argument overrides the paperSize argument if they do not match.
