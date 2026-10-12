---
title: "SimpleHoleFeatureData::DraftWhileExtruding"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleHoleFeatureData/SimpleHoleFeatureData__DraftWhileExtruding.htm"
---

# SimpleHoleFeatureData::DraftWhileExtruding

This property is obsolete and has been superseded by [SimpleHoleFeatureData2::DraftWhileExtruding](sldworksAPI.chm::/SimpleHoleFeatureData2/SimpleHoleFeatureData2__DraftWhileExtruding.htm).

Description

This property gets or sets whether to draft the simple hole feature while extruding.

Syntax (OLE Automation)

draftWhileExtrude = SimpleHoleFeatureData.DraftWhileExtruding (VB Get property)

SimpleHoleFeatureData.DraftWhileExtruding = draftWhileExtrude (VB Set property)

draftWhileExtrude = SimpleHoleFeatureData.GetDraftWhileExtruding ( ) (C++ Get property)

SimpleHoleFeatureData.SetDraftWhileExtruding ( draftWhileExtrude ) (C++ Set property)

| Property: | (BOOL) draftWhileExtrude | TRUE if to draft the simple hole feature while extruding, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = SimpleHoleFeatureData ->get_DraftWhileExtruding ( &draftWhileExtrude )

status = SimpleHoleFeatureData ->put_DraftWhileExtruding ( draftWhileExtrude )

| Property: | ( VARIANT_BOOL ) draftWhileExtrude | TRUE if to draft the simple hole feature while extruding, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
