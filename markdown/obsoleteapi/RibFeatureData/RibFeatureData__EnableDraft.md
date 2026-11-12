---
title: "RibFeatureData::EnableDraft"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RibFeatureData/RibFeatureData__EnableDraft.htm"
---

# RibFeatureData::EnableDraft

## RibFeatureData::EnableDraf t

This property is obsolete and has been superseded by [RibFeatureData2::EnableDraft](sldworksAPI.chm::/RibFeatureData2/RibFeatureData2__EnableDraft.htm).

Description

This property controls whether the rib has an associated draft. Additional draft control can be done with RibFeatureData::DraftAngle and RibFeatureData::DraftOutward.

Syntax (OLE Automation)

EnableDraft= RibFeatureData.EnableDraft (VB Get property)

RibFeatureData.EnableDraft= EnableDraft (VB Set property)

EnableDraft= RibFeatureData.GetEnableDraft ( ) (C++ Get property)

RibFeatureData.SetEnableDraft ( EnableDraft) (C++ Set property)

| Property: | (BOOL) EnableDraft | True if the rib has a draft angle |
| --- | --- | --- |

Syntax (COM)

status = RibFeatureData-> get_EnableDraft( &EnableDraft)

status = RibFeatureData-> put_EnableDraft( EnableDraft)

| Property: | (VARIANT_BOOL) EnableDraft | True if the rib has a draft angle |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Changing the value of this property does not affect geometry until Feature::ModifyDefinition is called.
