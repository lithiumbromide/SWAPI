---
title: "DrawingDoc::BreakLineSplineCut"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__BreakLineSplineCut.htm"
---

# DrawingDoc::BreakLineSplineCut

This method is obsolete and has been superseded by [BreakLine::Style](sldworksAPI.chm::/BreakLine/BreakLine__Style.htm).

Description

This method toggles the break line style to spline or changes the selected break line to spline style.

Syntax (OLE Automation)

void DrawingDoc.BreakLineSplineCut ()

Syntax (COM)

status = DrawingDoc->BreakLineSplineCut ( )

| Return: | (HRESULT)status | S_OK if successful |
| --- | --- | --- |

Remarks

Use DrawingDoc::InsertBreakHorizontal or DrawingDoc::InsertBreakVertical to insert break lines into a drawing view. Then, you can drag and reposition the break lines to customize the break. Use DrawingDoc::BreakView to create the broken drawing view.
