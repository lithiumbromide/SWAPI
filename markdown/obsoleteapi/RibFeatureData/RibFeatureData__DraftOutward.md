---
title: "RibFeatureData::DraftOutward"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RibFeatureData/RibFeatureData__DraftOutward.htm"
---

# RibFeatureData::DraftOutward

This property is obsolete and has been superseded by [RibFeatureData2::DraftOutward](sldworksAPI.chm::/RibFeatureData2/RibFeatureData2__DraftOutward.htm).

Description

This property controls whether the rib has an associated draft. Additional draft control can be done with RibFeatureData::DraftAngle and RibFeatureData::EnableDraft.

Syntax (OLE Automation)

DraftOutward= RibFeatureData.DraftOutward (VB Get property)

RibFeatureData.DraftOutward= DraftOutward (VB Set property)

DraftOutward= RibFeatureData.GetDraftOutward ( ) (C++ Get property)

RibFeatureData.SetDraftOutward ( DraftOutward) (C++ Set property)

| Property: | (BOOL) DraftOutward | TRUE if the draft is outward |
| --- | --- | --- |

Syntax (COM)

status = RibFeatureData-> get_DraftOutward( &DraftOutward)

status = RibFeatureData-> put_DraftOutward( DraftOutward)

| Property: | (VARIANT_BOOL) DraftOutward | TRUE if the draft is outward |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Changing the value of this property does not affect geometry until Feature::ModifyDefinition is called.
