---
title: "ModelDoc2::FeatureBossThicken2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureBossThicken2.htm"
---

# ModelDoc2::FeatureBossThicken2

This method is obsolete and has been superseded by [FeatureManager::FeatureBossThicken](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureBossThicken.htm).

Description

This method creates a boss feature by thickening the selected reference surface.

Syntax (OLE Automation)

void ModelDoc2.FeatureBossThicken2 ( thickness, direction, faceIndex, fillVolume )

| Input: | (double) thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0 - Thicken side 1 1 - Thicken side2 2 - Thicken both sides |
| Input: | (long) faceIndex | Not used |
| Input: | (BOOL) fillVolume | TRUE to make a solid from knitted surface, FALSE to not |

Syntax (COM)

status = ModelDoc2->FeatureBossThicken2 ( thickness, direction, faceIndex, fillVolume )

| Input: | (double) thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0 - Thicken side 1 1 - Thicken side2 2 - Thicken both sides |
| Input: | (long) faceIndex | Not used |
| Input: | (VARIANT_BOOL) fillVolume | TRUE to make a solid from knitted surface, FALSE to not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If fillVolume is TRUE, then the other arguments are ignored. A closed surface is required when fillVolume is TRUE.
