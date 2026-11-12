---
title: "DrawingDoc::DropDrawingViewFromPalette"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__DropDrawingViewFromPalette.htm"
---

# DrawingDoc::DropDrawingViewFromPalette

This method is obsolete and has been superseded by [DrawingDoc::DropDrawingViewFromPalette2](sldworksAPI.chm::/DrawingDoc/DrawingDoc__DropDrawingViewFromPalette2.htm).

Description

This method moves a drawing view from the drawing palette to the current drawing sheet.

Syntax (OLE Automation)

Retval = DrawingDoc.DropDrawingViewFromPalette ( Layout, X, Y, Z)

| Input: | (long) Layout | ID of the drawing view to move to the drawing sheet |
| --- | --- | --- |
| Input: | (double) X | x coordinate where to drop the drawing view |
| Input: | (double) Y | y coordinate where to drop the drawing view |
| Input: | (double) Z | z coordinate where to drop the drawing view ; this coordinate is always 0 |
| Output: | (LPVIEW) Retval | View |

Syntax (COM)

status = DrawingDoc->DropDrawingViewFromPalette ( Layout, X, Y, Z, &Retval)

| Input: | (long) Layout | ID of the drawing view to move to the drawing sheet |
| --- | --- | --- |
| Input: | (double) X | x coordinate where to drop the drawing view |
| Input: | (double) Y | y coordinate where to drop the drawing view |
| Input: | (double) Z | z coordinate where to drop the drawing view ; this coordinate is always 0 |
| Output: | (LPVIEW) Retval | View |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
