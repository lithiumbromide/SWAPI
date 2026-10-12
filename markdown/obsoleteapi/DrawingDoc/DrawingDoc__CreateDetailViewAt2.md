---
title: "DrawingDoc::CreateDetailViewAt2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateDetailViewAt2.htm"
---

# DrawingDoc::CreateDetailViewAt2

This method is obsolete and has been superseded by [DrawingDoc::CreateDetailViewAt3](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateDetailViewAt3.htm).

Description

This method creates a detail drawing view at the specified position using the selected closed contour as the detail bounds.

Syntax (OLE Automation)

retval = DrawingDoc.CreateDetailViewAt2 ( x, y, z )

| Input: | (double) x | X location |
| --- | --- | --- |
| Input: | (double) y | Y location |
| Input: | (double) z | Z location |
| Return: | (BOOL) retval | TRUE if successfully created, FALSE if not |

Syntax (COM)

status = DrawingDoc->CreateDetailViewAt2 ( x, y, z, &retval )

| Input: | (double) x | X location |
| --- | --- | --- |
| Input: | (double) y | Y location |
| Input: | (double) z | Z location |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
