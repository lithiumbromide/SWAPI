---
title: "DrawingDoc::AddCenterMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__AddCenterMark.htm"
---

# DrawingDoc::AddCenterMark

This method is obsolete and has been superseded by [DrawingDoc::InsertCenterMark](DrawingDoc__InsertCenterMark.htm).

Description

This method creates a center mark from the last edge selection.

Syntax (OLE Automation)

retval = DrawingDoc.AddCenterMark ( cmSize, cmShowLines)

| Input: | (double) cmSize | Centermark size; this is half the size of the + at the circle center; it is also the distance that the centermark lines overshoot the circle if cmShowLines is set to TRUE |
| --- | --- | --- |
| Input: | (BOOL) cmShowLines | TRUE if you want to display the centermark lines, FALSE if you want only the + to appear at the circle center |
| Return: | (BOOL) retval | TRUE if successfully created, FALSE if not |

Syntax (COM)

status = DrawingDoc->AddCenterMark ( cmSize, cmShowLines, &retval )

| Input: | (double) cmSize | Centermark size; this is half the size of the + at the circle center; it is also the distance that the centermark lines overshoot the circle if cmShowLines is set to TRUE |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) cmShowLines | TRUE if you want to display the centermark lines, FALSE if you want only the + to appear at the circle center |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
