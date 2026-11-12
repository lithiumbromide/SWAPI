---
title: "RibFeatureData::DraftAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RibFeatureData/RibFeatureData__DraftAngle.htm"
---

# RibFeatureData::DraftAngle

This property is obsolete and has been superseded by [RibFeatureData2::DraftAngle](sldworksAPI.chm::/RibFeatureData2/RibFeatureData2__DraftAngle.htm).

Description

This property controls the draft angle for the rib. Additional draft control can be done with RibFeatureData::EnableDraft and RibFeatureData::DraftOutward.

Syntax (OLE Automation)

DraftAngle= RibFeatureData.DraftAngle (VB Get property)

RibFeatureData.DraftAngle= DraftAngle (VB Set property)

DraftAngle= RibFeatureData.GetDraftAngle ( ) (C++ Get property)

RibFeatureData.SetDraftAngle ( DraftAngle) (C++ Set property)

| Property: | (double) DraftAngle | Angle for the draft |
| --- | --- | --- |

Syntax (COM)

status = RibFeatureData-> get_DraftAngle( &DraftAngle)

status = RibFeatureData-> put_DraftAngle( DraftAngle)

| Property: | (double) DraftAngle | Angle for the draft |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Changing the value of this property does not affect geometry until Feature::ModifyDefinition is called.
