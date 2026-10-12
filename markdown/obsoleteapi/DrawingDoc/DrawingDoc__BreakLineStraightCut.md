---
title: "DrawingDoc::BreakLineStraightCut"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__BreakLineStraightCut.htm"
---

# DrawingDoc::BreakLineStraightCut

This method is obsolete and has been superseded by [BreakLine::Style](sldworksAPI.chm::/BreakLine/BreakLine__Style.htm).

Description

This method switches the break line style to straight or changes the currently selected break line to straight style.

Syntax (OLE Automation)

void DrawingDoc.BreakLineStraightCut ()

Syntax (COM)

status = DrawingDoc->BreakLineStraightCut ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

To insert break lines to a drawing view, use DrawingDoc::InsertBreakHorizontal or DrawingDoc::InsertBreakVertical. You can then customize the break by dragging and repositioning the break lines. Use the DrawingDoc::BreakView method to actually create the broken drawing view.
