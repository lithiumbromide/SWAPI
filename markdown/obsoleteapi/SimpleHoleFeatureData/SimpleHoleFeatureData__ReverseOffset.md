---
title: "SimpleHoleFeatureData::ReverseOffset"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleHoleFeatureData/SimpleHoleFeatureData__ReverseOffset.htm"
---

# SimpleHoleFeatureData::ReverseOffset

This property is obsolete and has been superseded by [SimpleHoleFeatureData2::ReverseOffset](sldworksAPI.chm::/SimpleHoleFeatureData2/SimpleHoleFeatureData2__ReverseOffset.htm).

Description

This property gets or sets whether the offset from the surface should be reversed.

Syntax (OLE Automation)

reverseOffset = SimpleHoleFeatureData.ReverseOffset (VB Get property)

SimpleHoleFeatureData.ReverseOffset = reverseOffset (VB Set property)

reverseOffset = SimpleHoleFeatureData.GetReverseOffset ( ) (C++ Get property)

SimpleHoleFeatureData.SetReverseOffset (reverseOffset) (C++ Set property)

| Property: | (BOOL) reverseOffset | TRUE if the offset from the surface should be reversed, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = SimpleHoleFeatureData ->get_ReverseOffset ( &reverseOffse t)

status = SimpleHoleFeatureData ->put_ReverseOffset ( reverseOffset )

| Property: | ( VARIANT_BOOL ) reverseOffset | TRUE if the offset from the surface should be reversed, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
