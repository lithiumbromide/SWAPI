---
title: "ModelDoc::FeatureSketchDrivenPattern"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureSketchDrivenPattern.htm"
---

# ModelDoc::FeatureSketchDrivenPattern

This method is obsolete and has been superseded by [ModelDoc2::FeatureSketchDrivenPattern](../ModelDoc2/ModelDoc2__FeatureSketchDrivenPattern.htm).

Description

This method creates a sketch-driven pattern.

Syntax (OLE Automation)

void ModelDoc.FeatureSketchDrivenPattern (useCentroid )

| Input: | (BOOL) useCentroid | TRUE to use centroid as reference point, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->FeatureSketchDrivenPattern ( useCentroid )

| Input: | (VARIANT_BOOL) useCentroid | TRUE to use centroid as reference point, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
