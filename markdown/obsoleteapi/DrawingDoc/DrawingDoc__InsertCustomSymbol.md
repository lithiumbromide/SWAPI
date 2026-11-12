---
title: "DrawingDoc::InsertCustomSymbol"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertCustomSymbol.htm"
---

# DrawingDoc::InsertCustomSymbol

This method is obsolete and has been superseded by [DrawingDoc::InsertCustomSymbol2](DrawingDoc__InsertCustomSymbol2.htm).

Description

This method inserts a custom symbol into the document.

Syntax (OLE Automation)

void DrawingDoc.InsertCustomSymbol ( symbolPath )

| Input: | (BSTR) symbolPath | Filename of the custom symbol |
| --- | --- | --- |

Syntax (COM)

status = DrawingDoc->InsertCustomSymbol ( symbolPath )

| Input: | (BSTR) symbolPath | Filename of the custom symbol |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method depends on a selected item. If nothing is selected, SolidWorks takes no action and this method returns NULL.
