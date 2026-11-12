---
title: "ModelDoc::InsertCutSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCutSurface.htm"
---

# ModelDoc::InsertCutSurface

This method is obsolete and has been superseded by [ModelDoc2::InsertCutSurface](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertCutSurface.htm).

Description

This method creates a surface cut feature.

Syntax (OLE Automation)

void ModelDoc.InsertCutSurface ( flip, keepPieceIndex )

| Input: | (BOOL) flip | TRUE to flip the direction |
| --- | --- | --- |
| Input: | (long) keepPieceIndex | Piece to keep if there is ambiguity |

Syntax (COM)

status = ModelDoc->InsertCutSurface ( flip, keepPieceIndex )

| Input: | (VARIANT_BOOL) flip | TRUE to flip the direction |
| --- | --- | --- |
| Input: | (long) keepPieceIndex | Piece to keep if there is ambiguity |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a cut from a selected surface.

When there is ambiguity in the result of a cut, the keepPieceIndex is used to resolve which of the possible results is used. This can be set to -1 if there is no ambiguity; otherwise, it should be the index of the result, starting from 0 (up to 1 less than the possible number of outcomes).
