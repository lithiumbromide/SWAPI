---
title: "DrawingDoc::NewSheet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__NewSheet.htm"
---

# DrawingDoc::NewSheet

This method is obsolete and has been superseded by [DrawingDoc::NewSheet2](DrawingDoc__NewSheet2.htm).

Description

This method creates a new sheet for the selected drawing.

Syntax (OLE Automation)

void DrawingDoc.NewSheet ( name, paperSize, templateIn, scale1, scale2)

| Input: | (BSTR) name | Name for the sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |

Syntax (COM)

status = DrawingDoc->NewSheet ( name, paperSize, templateIn, scale1, scale2 )

| Input: | (BSTR) name | Name for the sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method does not support paperSize = swDwgPapersUserDefined or templateIn = swDwgTemplateCustom.
