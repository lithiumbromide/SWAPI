---
title: "ExtrudeFeatureData::SetDraftWhileExtruding"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__SetDraftWhileExtruding.htm"
---

# ExtrudeFeatureData::SetDraftWhileExtruding

This method is obsolete and has been superseded by [ExtrudeFeatureData2::SetDraftWhileExtruding](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__SetDraftWhileExtruding.htm).

Description

This method sets whether the feature is drafted while extruding in forward or reverse direction.

Syntax (OLE Automation)

void ExtrudeFeatureData.SetDraftWhileExtruding ( forward, draftWhileExtrude )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (BOOL) draftWhileExtrude | TRUE if feature is drafted while extruding, FALSE if not |

Syntax (COM)

status = ExtrudeFeatureData->SetDraftWhileExtruding ( forward, draftWhileExtrude )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) draftWhileExtrude | TRUE if feature is drafted while extruding, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
