---
title: "DrawingDoc::MakeCustomSymbol"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__MakeCustomSymbol.htm"
---

# DrawingDoc::MakeCustomSymbol

This method is obsolete and has been superseded by [DrawingDoc::MakeCustomSymbol2](DrawingDoc__MakeCustomSymbol2.htm).

Description

This method creates a new block in this drawing.

Syntax (OLE Automation)

void DrawingDoc.MakeCustomSymbol ( )

Syntax (COM)

status = DrawingDoc->MakeCustomSymbol ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method depends on something being selected before it is called. If nothing is selected, SolidWorks takes no action and returns NULL.
