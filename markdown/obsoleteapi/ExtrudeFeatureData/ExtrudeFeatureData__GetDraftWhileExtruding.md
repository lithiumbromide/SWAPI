---
title: "ExtrudeFeatureData::GetDraftWhileExtruding"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__GetDraftWhileExtruding.htm"
---

# ExtrudeFeatureData::GetDraftWhileExtruding

This method is obsolete and has been superseded by [ExtrudeFeatureData2::GetDraftWhileExtruding](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__GetDraftWhileExtruding.htm).

Description

This method gets whether the feature is drafted while extruding in forward or reverse direction.

Syntax (OLE Automation)

draftWhileExtrude = ExtrudeFeatureData.GetDraftWhileExtruding ( forward )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Return: | (BOOL) draftWhileExtrude | TRUE if feature is drafted while extruding, FALSE if not |

Syntax (COM)

status = ExtrudeFeatureData->GetDraftWhileExtruding ( forward, &draftWhileExtrude )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) draftWhileExtrude | TRUE if feature is drafted while extruding, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
