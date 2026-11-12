---
title: "SimpleHoleFeatureData::DraftOutward"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleHoleFeatureData/SimpleHoleFeatureData__DraftOutward.htm"
---

# SimpleHoleFeatureData::DraftOutward

This property is obsolete and has been superseded by [SimpleHoleFeatureData2::DraftOutward](sldworksAPI.chm::/SimpleHoleFeatureData2/SimpleHoleFeatureData2__DraftOutward.htm).

Description

This property gets or sets whether to draft the simple hole feature outward.

Syntax (OLE Automation)

draftOutward = SimpleHoleFeatureData.DraftOutward (VB Get property)

SimpleHoleFeatureData.DraftOutward = draftOutward (VB Set property)

draftOutward = SimpleHoleFeatureData.GetDraftOutward ( ) (C++ Get property)

SimpleHoleFeatureData.SetDraftOutward ( draftOutward ) (C++ Set property)

| Property: | (BOOL) draftOutward | TRUE if to draft the simple hole feature outward, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = SimpleHoleFeatureData ->get_DraftOutward ( &draftOutward )

status = SimpleHoleFeatureData ->put_DraftOutward ( draftOutward )

| Property: | ( VARIANT_BOOL ) draftOutward | TRUE if to draft the simple hole feature outward, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
