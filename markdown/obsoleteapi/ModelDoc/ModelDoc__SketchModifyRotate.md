---
title: "ModelDoc::SketchModifyRotate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchModifyRotate.htm"
---

# ModelDoc::SketchModifyRotate

This method is obsolete and has been superseded by [ModelDoc2::SketchModifyRotate](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchModifyRotate.htm).

Description

This method rotates the coordinate system of the active or selected sketch.

Syntax (OLE Automation)

void ModelDoc.SketchModifyRotate ( centerX, centerY, angle )

| Input: | (double) centerX | X point to rotate about |
| --- | --- | --- |
| Input: | (double) centerY | Y point to rotate about |
| Input: | (double) angle | Angle of rotation |

Syntax (COM)

status = ModelDoc->SketchModifyRotate ( centerX, centerY, angle )

| Input: | (double) centerX | X point to rotate about |
| --- | --- | --- |
| Input: | (double) centerY | Y point to rotate about |
| Input: | (double) angle | Angle of rotation |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
