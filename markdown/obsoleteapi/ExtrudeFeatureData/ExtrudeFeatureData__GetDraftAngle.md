---
title: "ExtrudeFeatureData::GetDraftAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__GetDraftAngle.htm"
---

# ExtrudeFeatureData::GetDraftAngle

This method is obsolete and has been superseded by [ExtrudeFeatureData2::GetDraftAngle](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__GetDraftAngle.htm).

Description

This method gets the draft angle of the extrusion in forward/reverse direction.

Syntax (OLE Automation)

draftAngle = ExtrudeFeatureData.GetDraftAngle ( forward )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Return: | (double) draftAngle | Draft angle of the extrusion in radians |

Syntax (COM)

status = ExtrudeFeatureData->GetDraftAngle ( forward, &draftAngle )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Output: | (double) draftAngle | Draft angle of the extrusion in radians |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
