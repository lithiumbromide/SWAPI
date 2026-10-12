---
title: "RevolveFeatureData::SetWallThickness"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RevolveFeatureData/RevolveFeatureData__SetWallThickness.htm"
---

# RevolveFeatureData::SetWallThickness

This method is obsolete and has been superseded by [RevolveFeatureData2::SetWallThickness](sldworksAPI.chm::/RevolveFeatureData2/RevolveFeatureData2__ThinWallType.htm).

Description

This method sets the wall thickness of the thin revolution feature in forward or reverse direction.

Syntax (OLE Automation)

void RevolveFeatureData.SetWallThickness ( forward, wallThickness )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Return: | (double) wallThickness | Wall thickness |

Syntax (COM)

status = RevolveFeatureData ->SetWallThickness ( forward, wallThickness )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Output: | (double) wallThickness | Wall thickness |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is relevant only for thin features.
