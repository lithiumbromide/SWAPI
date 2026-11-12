---
title: "DrawingDoc::SetupSheet2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__SetupSheet2.htm"
---

# DrawingDoc::SetupSheet2

This method is obsolete and has been superseded by [DrawingDoc::SetupSheet3](DrawingDoc__SetupSheet3.htm).

Description

This method changes the settings for the current sheet on this drawing document.

Syntax (OLE Automation)

void DrawingDoc.SetupSheet2 ( name, paperSize, templateIn, scale1, scale2, skPointsFlag)

| Input: | (BSTR) name | Name for the sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |
| Input: | (long) skPointsFlag | Display of user points as defined in swSkInternalPntOpts_e |

Syntax (COM)

status = DrawingDoc->SetupSheet2 ( name, paperSize, templateIn, scale1, scale2, skPointsFlag )

| Input: | (BSTR) name | Name for the sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |
| Input: | (long) skPointsFlag | Display of user points as defined in swSkInternalPntOpts_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can also use Sheet::SetProperties, Sheet::SetName and Sheet::SetTemplateName.

The templateIn value overrides paperSize if they do not match.

The skPointsFlag is not available through the SolidWorks user interface on a per-document level. This overrides the global user option setting for the display of entity points.
