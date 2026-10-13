---
title: "ModelDoc::FeatureCutThicken2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureCutThicken2.htm"
---

# ModelDoc::FeatureCutThicken2

This method is obsolete and has been superseded by [ModelDoc2::FeatureCutThicken2](../ModelDoc2/ModelDoc2__FeatureCutThicken2.htm).

Description

This method thickens the selected reference surface feature and then generates a cut.

Syntax (OLE Automation)

void ModelDoc.FeatureCutThicken2 ( thickness, direction, faceIndex, fillVolume )

| Input: | (double) thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0 Thicken side 1 1 Thicken side2 2 Thicken both sides |
| Input: | (long) faceIndex | Not used |
| Input: | (BOOL) fillVolume | TRUE if you wish to make a solid from knitted surface, FALSE if not |

Syntax (COM)

status = ModelDoc->FeatureCutThicken2 ( thickness, direction, faceIndex, fillVolume )

| Input: | (double )thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0 Thicken side 1 1 Thicken side2 2 Thicken both sides |
| Input: | (long) faceIndex | Not used |
| Input: | (VARIANT_BOOL) fillVolume | TRUE if you wish to make a solid from knitted surface, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If fillVolume is TRUE, the other arguments are ignored. A closed surface is required when fillVolume is TRUE.
