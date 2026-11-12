---
title: "DraftFeatureData::Type"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DraftFeatureData/DraftFeatureData__Type.htm"
---

# DraftFeatureData::Type

This property is obsolete and has been superseded by [DraftFeatureData2::Type](sldworksAPI.chm::/DraftFeatureData2/DraftFeatureData2__Type.htm).

Description

This property gets the draft feature type.

Syntax (OLE Automation)

type = DraftFeatureData.Type (VB Get property)

type = DraftFeatureData.GetType ( ) (C++ Get property)

| Property: | ( int ) type | Draft type: 0 = Neutral Plane 1 = Parting Line |
| --- | --- | --- |

Syntax (COM)

status = DraftFeatureData ->get_Type ( & type )

| Property: | ( int ) type | Draft type: 0 = Neutral Plane 1 = Parting Line |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This is a read-only property.
