---
title: "ModelDoc::SketchModifyFlip"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchModifyFlip.htm"
---

# ModelDoc::SketchModifyFlip

This method is obsolete and has been superseded by [ModelDoc2::SketchModifyFlip](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchModifyFlip.htm).

Description

This method flips the coordinate system of the active or selected sketch.

Syntax (OLE Automation)

void ModelDoc.SketchModifyFlip ( axisFlag )

| Input: | (int) axisFlag | Axis flag to flip about |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SketchModifyFlip ( axisFlag )

| Input: | (int) axisFlag | Axis flag to flip about |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
