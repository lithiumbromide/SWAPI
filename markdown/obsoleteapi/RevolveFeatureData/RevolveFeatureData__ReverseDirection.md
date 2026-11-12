---
title: "RevolveFeatureData::ReverseDirection"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RevolveFeatureData/RevolveFeatureData__ReverseDirection.htm"
---

# RevolveFeatureData::ReverseDirection

This property is obsolete and has been superseded by [RevolveFeatureData2::ReverseDirection](sldworksAPI.chm::/RevolveFeatureData2/RevolveFeatureData2__ReverseDirection.htm).

Description

This property gets or sets whether the direction of the revolution feature should be reversed.

Syntax (OLE Automation)

reverseDirection = RevolveFeatureData.ReverseDirection (VB Get property)

RevolveFeatureData.ReverseDirection = reverseDirection (VB Set property)

reverseDirection = RevolveFeatureData.GetReverseDirection ( ) (C++ Get property)

RevolveFeatureData.SetReverseDirection (reverseDirection) (C++ Set property)

| Property: | (BOOL) reverseDirection | TRUE if the direction of the revolution feature should be reversed, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = RevolveFeatureData ->get_ReverseDirection ( &reverseDirection)

status = RevolveFeatureData ->put_ReverseDirection (reverseDirection)

| Property: | (VARIANT_BOOL) reverseDirection | TRUE if the direction of the revolution feature should be reversed, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
