---
title: "SimpleFilletFeatureData::RoundCorners"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleFilletFeatureData/SimpleFilletFeatureData__RoundCorners.htm"
---

# SimpleFilletFeatureData::RoundCorners

This property is obsolete and has been superseded by [SimpleFilletFeatureData2::RoundCorners](sldworksAPI.chm::/SimpleFilletFeatureData2/SimpleFilletFeatureData2__RoundCorners.htm).

Description

This property gets or sets whether the simple fillet feature has round corners.

Syntax (OLE Automation)

roundCorners = SimpleFilletFeatureData.RoundCorners (VB Get property)

SimpleFilletFeatureData.RoundCorners = roundCorners (VB Set property)

roundCorners = SimpleFilletFeatureData.GetRoundCorners ( ) (C++ Get property)

SimpleFilletFeatureData.SetRoundCorners ( roundCorners ) (C++ Set property)

| Property: | ( BOOL ) roundCorners | TRUE if simple fillet feature has round corners, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = SimpleFilletFeatureData ->get_RoundCorners ( &roundCorners )

status = SimpleFilletFeatureData ->put_RoundCorners ( roundCorners )

| Property: | ( VARIANT_BOOL ) roundCorners | TRUE if simple fillet feature has round corners, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
