---
title: "SimpleHoleFeatureData::ReverseDirection"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleHoleFeatureData/SimpleHoleFeatureData__ReverseDirection.htm"
---

# SimpleHoleFeatureData::ReverseDirection

This property is obsolete and has been superseded by [SimpleHoleFeatureData2::ReverseDirection](sldworksAPI.chm::/SimpleHoleFeatureData2/SimpleHoleFeatureData2__ReverseDirection.htm).

Description

This property gets or sets whether the direction of the cut is reversed.

Syntax (OLE Automation)

reverseDirection = SimpleHoleFeatureData.ReverseDirection (VB Get property)

SimpleHoleFeatureData.ReverseDirection = reverseDirection (VB Set property)

reverseDirection = SimpleHoleFeatureData.GetReverseDirection ( ) (C++ Get property)

SimpleHoleFeatureData.SetReverseDirection ( reverseDirection ) (C++ Set property)

| Property: | (BOOL) reverseDirection | TRUE if the direction of the cut should be reversed, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = SimpleHoleFeatureData ->get_ReverseDirection ( &reverseDirection )

status = SimpleHoleFeatureData ->put_ReverseDirection ( reverseDirection )

| Property: | ( VARIANT_BOOL ) reverseDirection | TRUE if the direction of the cut should be reversed, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
