---
title: "ExtrudeFeatureData::GetWallThickness"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__GetWallThickness.htm"
---

# ExtrudeFeatureData::GetWallThickness

This method is obsolete and has been superseded by [ExtrudeFeatureData2::GetWallThickness](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__GetWallThickness.htm).

Description

This method gets the wall thickness of the thin extrusion feature in forward or reverse direction.

Syntax (OLE Automation)

wallThickness = ExtrudeFeatureData.GetWallThickness ( forward )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Return: | (double) wallThickness | Wall thickness |

Syntax (COM)

status = ExtrudeFeatureData->GetWallThickness ( forward, &wallThickness )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Output: | (double) wallThickness | Wall thickness |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is relevant only for thin features.
