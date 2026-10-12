---
title: "ExtrudeFeatureData::SetDepth"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__SetDepth.htm"
---

# ExtrudeFeatureData::SetDepth

This method is obsolete and has been superseded by [ExtrudeFeatureData2::SetDepth](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__SetDepth.htm).

Description

This method sets the depth of the feature in forward or reverse direction.

Syntax (OLE Automation)

void ExtrudeFeatureData.SetDepth ( forward, depth )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (double) depth | Depth of the extrusion |

Syntax (COM)

status = ExtrudeFeatureData->SetDepth ( forward, depth )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (double) depth | Depth of the extrusion |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For swEndCondOffsetFromSurface type end condition, use the same method to specify the surface offset distance.
