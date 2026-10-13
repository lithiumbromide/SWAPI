---
title: "ModelDoc2::FeatureSketchDrivenPattern"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureSketchDrivenPattern.htm"
---

# ModelDoc2::FeatureSketchDrivenPattern

This method is obsolete and has been superseded by [FeatureManager::FeatureSketchDrivenPattern](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureSketchDrivenPattern.htm).

Description

This method creates a sketch-driven pattern.

Syntax (OLE Automation)

void ModelDoc2.FeatureSketchDrivenPattern (useCentroid )

| Input: | (BOOL) useCentroid | TRUE to use centroid as reference point, FALSE to not |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->FeatureSketchDrivenPattern ( useCentroid )

| Input: | (VARIANT_BOOL) useCentroid | TRUE to use centroid as reference point, FALSE to not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method requires selecting the required input entities using the proper selection marks:

- sketch to follow = 0
- seed features = 4
- seed faces = 128
- seed bodies = 256

See the SolidWorks Help for more information about sketch-driven patterns.
