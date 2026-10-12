---
title: "ExtrudeFeatureData::IsBossFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__IsBossFeature.htm"
---

# ExtrudeFeatureData::IsBossFeature

This method is obsolete and has been superseded by [ExtrudeFeatureData2::IsBossFeature](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__IsBossFeature.htm).

Description

This method gets whether the extrusion is a boss feature.

Syntax (OLE Automation)

isBossFeature = ExtrudeFeatureData. IsBossFeature ( )

| Return: | (BOOL) isBossFeature | TRUE if extrusion is a boss feature, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = ExtrudeFeatureData->IsBossFeature ( &isBossFeature )

| Output: | (VARIANT_BOOL) isBossFeature | TRUE if extrusion is a boss feature, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
