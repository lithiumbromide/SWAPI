---
title: "ExtrudeFeatureData::SetDraftOutward"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__SetDraftOutward.htm"
---

# ExtrudeFeatureData::SetDraftOutward

This method is obsolete and has been superseded by [ExtrudeFeatureData2::SetDraftOutward](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__SetDraftOutward.htm).

Description

This method sets whether the extrusion feature should draft outward in forward or reverse direction.

Syntax (OLE Automation)

void ExtrudeFeatureData.SetDraftOutward ( forward, draftOutward )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (BOOL) draftOutward | TRUE if feature is drafted outward, FALSE if not |

Syntax (COM)

status = ExtrudeFeatureData->SetDraftOutward ( forward, draftOutward )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) draftOutward | TRUE if feature is drafted outward, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
