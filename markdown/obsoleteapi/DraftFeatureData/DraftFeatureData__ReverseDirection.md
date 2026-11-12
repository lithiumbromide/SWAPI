---
title: "DraftFeatureData::ReverseDirection"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DraftFeatureData/DraftFeatureData__ReverseDirection.htm"
---

# DraftFeatureData::ReverseDirection

This property is obsolete and has been superseded by [DraftFeatureData2::ReverseDirection](sldworksAPI.chm::/DraftFeatureData2/DraftFeatureData2__ReverseDirection.htm).

Description

This property gets or sets whether to reverse the direction of the draft feature.

Syntax (OLE Automation)

reverseDirection = DraftFeatureData.ReverseDirection (VB Get property)

DraftFeatureData.ReverseDirection = reverseDirection (VB Set property)

reverseDirection = DraftFeatureData.GetReverseDirection ( ) (C++ Get property)

DraftFeatureData.SetReverseDirection ( reverseDirection ) (C++ Set property)

| Property: | (BOOL) reverseDirection | TRUE if the direction of the draft feature is reversed, FALSE if it is not |
| --- | --- | --- |

Syntax (COM)

status = DraftFeatureData ->get_ReverseDirection ( &reverseDirection )

status = DraftFeatureData ->put_ReverseDirection ( reverseDirection )

| Property: | (VARIANT_BOOL) reverseDirection | TRUE if the direction of the draft feature is reversed, FALSE if it is not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
