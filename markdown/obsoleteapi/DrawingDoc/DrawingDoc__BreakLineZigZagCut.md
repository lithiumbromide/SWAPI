---
title: "DrawingDoc::BreakLineZigZagCut"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__BreakLineZigZagCut.htm"
---

# DrawingDoc::BreakLineZigZagCut

This method is obsolete and has been superseded by [BreakLine::Style](sldworksAPI.chm::/BreakLine/BreakLine__Style.htm).

Description

This method toggles the break line style to zig-zag or changes the selected break line to zig-zag style.

Syntax (OLE Automation)

void DrawingDoc.BreakLineZigZagCut ()

Syntax (COM)

status = DrawingDoc->BreakLineZigZagCut ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

To insert break lines to a drawing view, use DrawingDoc::InsertBreakHorizontal or DrawingDoc::InsertBreakVertical. You can then customize the break by dragging and repositioning the break lines. Use the DrawingDoc::BreakView method to actually create the broken drawing view.
