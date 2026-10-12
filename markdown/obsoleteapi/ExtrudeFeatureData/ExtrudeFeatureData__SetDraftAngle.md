---
title: "ExtrudeFeatureData::SetDraftAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__SetDraftAngle.htm"
---

# ExtrudeFeatureData::SetDraftAngle

This method is obsolete and has been superseded by [ExtrudeFeatureData2::SetDraftAngle](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__GetDraftAngle.htm).

Description

This method sets the draft angle of the extrusion in forward or reverse direction.

Syntax (OLE Automation)

void ExtrudeFeatureData.SetDraftAngle ( forward, draftAngle )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (double) draftAngle | Draft angle of the extrusion in radians |

Syntax (COM)

status = ExtrudeFeatureData->SetDraftAngle ( forward, draftAngle )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (double) draftAngle | Draft angle of the extrusion in radians |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
