---
title: "ModelDoc::SketchConvertIsoCurves"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchConvertIsoCurves.htm"
---

# ModelDoc::SketchConvertIsoCurves

This method is obsolete and has been superseded by [ModelDoc2::SketchConvertIsoCurves](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchConvertIsoCurves.htm).

Description

This method converts an ISO-parametric curve or curves on a selected surface into a sketch entity.

Syntax (OLE Automation)

void ModelDoc.SketchConvertIsoCurves ( percentRatio, vORuDir, doConstrain, skipHoles)

| Input: | (double) percentRatio | Value for percent ratio |
| --- | --- | --- |
| Input: | (BOOL) vORuDir | TRUE for V direction, FALSE for U direction |
| Input: | (BOOL) doConstrain | TRUE if you want to constrain these new sketch entities, FALSE otherwise |
| Input | (BOOL) skipHoles | TRUE if you want to skip the holes in this surface, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SketchConvertIsoCurves ( percentRatio, vORuDir, doConstrain)

| Input: | (double) percentRatio | Value for percent ratio |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) vORuDir | TRUE for V direction, FASLE for U direction |
| Input: | (VARIANT_BOOL) doConstrain | TRUE if you want to constrain these new sketch entities, FALSE otherwise |
| Input | (VARIANT_BOOL) skipHoles | TRUE if you want to skip the holes in this surface, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
