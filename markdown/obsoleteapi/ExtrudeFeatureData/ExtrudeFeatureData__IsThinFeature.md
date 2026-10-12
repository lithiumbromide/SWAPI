---
title: "ExtrudeFeatureData::IsThinFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__IsThinFeature.htm"
---

# ExtrudeFeatureData::IsThinFeature

This method is obsolete and has been superseded by [ExtrudeFeatureData2::IsThinFeature](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__IsThinFeature.htm).

Description

This method gets whether the extrusion is a thin feature.

Syntax (OLE Automation)

isThinFeature = ExtrudeFeatureData.IsThinFeature ( )

| Return: | (BOOL) isThinFeature | TRUE if extrusion is a thin feature, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = ExtrudeFeatureData->get_IsThinFeature ( &isThinFeature )

| Output: | (VARIANT_BOOL) isThinFeature | TRUE if extrusion is a thin feature, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
