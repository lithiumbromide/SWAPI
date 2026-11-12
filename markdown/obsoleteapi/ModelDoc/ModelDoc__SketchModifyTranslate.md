---
title: "ModelDoc::SketchModifyTranslate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchModifyTranslate.htm"
---

# ModelDoc::SketchModifyTranslate

This method is obsolete and has been superseded by [ModelDoc2::SketchModifyTranslate](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchModifyTranslate.htm).

Description

This method translates the coordinate system of the active or selected sketch.

Syntax (OLE Automation)

void ModelDoc.SketchModifyTranslate ( startX, startY, endX, endY)

| Input: | (double) startX | X sketch value defining "from" position |
| --- | --- | --- |
| Input: | (double) startY | Y sketch value defining "from" position |
| Input: | (double) endX | X sketch value defining "to" position |
| Input: | (double) endY | Y sketch value defining "to" position |

Syntax (COM)

status = ModelDoc-> SketchModifyTranslate (double startX, double startY, double endX, double endY )

| Input: | (double) startX | X sketch value defining "from" position |
| --- | --- | --- |
| Input: | (double) startY | Y sketch value defining "from" position |
| Input: | (double) endX | X sketch value defining "to" position |
| Input: | (double) endY | Y sketch value defining "to" position |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The sketch 9s translated from the XY start-point position, to the XY end-point position.
