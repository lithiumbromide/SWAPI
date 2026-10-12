---
title: "DrawingDoc::CreateAuxiliaryViewAt"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateAuxiliaryViewAt.htm"
---

# DrawingDoc::CreateAuxiliaryViewAt

This method is obsolete and has been superseded by [DrawingDoc::CreateAuxiliaryViewAt2](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateAuxiliaryViewAt2.htm).

Description

This method creates an auxiliary view at the specified location in sheet space.

Syntax (OLE Automation)

retval = DrawingDoc.CreateAuxiliaryViewAt ( x, y, z, notAligned )

| Input: | (double) x | X location |
| --- | --- | --- |
| Input: | (double) y | Y location |
| Input: | (double) z | Z location |
| Input: | (BOOL) notAligned | TRUE aligns the view from its owner, FALSE does not |
| Return: | (BOOL) retval | TRUE if successfully created, FALSE if not |

Syntax (COM)

status = DrawingDoc->CreateAuxiliaryViewAt ( x, y, z, notAligned, &retval )

| Input: | (double) x | X location |
| --- | --- | --- |
| Input: | (double) y | Y location |
| Input: | (double) z | Z location |
| Input: | (VARIANT_BOOL) notAligned | TRUE aligns the view from its owner, FALSE does not |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
