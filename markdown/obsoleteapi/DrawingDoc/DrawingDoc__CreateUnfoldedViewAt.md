---
title: "DrawingDoc::CreateUnfoldedViewAt"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateUnfoldedViewAt.htm"
---

# DrawingDoc::CreateUnfoldedViewAt

This method is obsolete and has been superseded by [DrawingDoc::CreateUnfoldedViewAt2](DrawingDoc__CreateUnfoldedViewAt2.htm).

Description

This method uses the selected drawing view to create a unfolded drawing view and places it in the drawing at the location specified.

Syntax (OLE Automation)

retval = DrawingDoc.CreateUnfoldedViewAt ( x, y, z)

| Input: | (double) x | X location of the unfolded drawing view in meters |
| --- | --- | --- |
| Input: | (double) y | Y location of the unfolded drawing view in meters |
| Input: | (double) z | Z location of the unfolded drawing view in meters |
| Return: | (BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = DrawingDoc->CreateUnfoldedViewAt ( x, y, z, &retval )

| Input: | (double) x | X location of the unfolded drawing view in meters |
| --- | --- | --- |
| Input: | (double) y | Y location of the unfolded drawing view in meters |
| Input: | (double) z | Z location of the unfolded drawing view in meters |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
