---
title: "DrawingDoc::CreateUnfoldedViewAt2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateUnfoldedViewAt2.htm"
---

# DrawingDoc::CreateUnfoldedViewAt2

This method is obsolete and has been superseded by [DrawingDoc::CreateUnfoldedViewAt3](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateUnfoldedViewAt3.htm).

Description

This method creates an unfolded drawing view from the selected drawing view and places it in the drawing at the specified location.

Syntax (OLE Automation)

retval = DrawingDoc.CreateUnfoldedViewAt2 ( x, y, z, notAligned )

| Input: | (double) x | X position in the drawing sheet space for the center of the drawing view |
| --- | --- | --- |
| Input: | (double) y | Y position in the drawing sheet space for the center of the drawing view |
| Input: | (double) z | Z position in the drawing sheet space for the center of the drawing view |
| Input: | (BOOL) notAligned | TRUE if you want to break the alignment with the parent view, FALSE if you want to keep the view aligned with the parent view |
| Return: | (BOOL) retval | TRUE if successful |

Syntax (COM)

status = DrawingDoc->CreateUnfoldedViewAt2 ( x, y, z, notAligned, &retval )

| Input: | (double) x | X position in the drawing sheet space for the center of the drawing view |
| --- | --- | --- |
| Input: | (double) y | Y position in the drawing sheet space for the center of the drawing view |
| Input: | (double) z | Z position in the drawing sheet space for the center of the drawing view |
| Input: | (VARIANT_BOOL) notAligned | TRUE if you want to break the alignment with the parent view, FALSE if you want to keep the view aligned with the parent view |
| Output: | (VARIANT_BOOL) retval | TRUE if successful |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
