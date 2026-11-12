---
title: "ExtrudeFeatureData::SetWallThickness"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__SetWallThickness.htm"
---

# ExtrudeFeatureData::SetWallThickness

This method is obsolete and has been superseded by [ExtrudeFeatureData2::SetWallThickness](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__SetWallThickness.htm).

Description

This method sets the wall thickness of the thin extrusion feature in forward or reverse direction.

Syntax (OLE Automation)

void ExtrudeFeatureData.SetWallThickness ( forward, wallThickness )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Return: | (double) wallThickness | Wall thickness |

Syntax (COM)

status = ExtrudeFeatureData->SetWallThickness ( forward, wallThickness )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Output: | (double) wallThickness | Wall thickness |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is relevant only for thin features.
