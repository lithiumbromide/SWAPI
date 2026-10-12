---
title: "SimpleHoleFeatureData::Type"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleHoleFeatureData/SimpleHoleFeatureData__Type.htm"
---

# SimpleHoleFeatureData::Type

This property is obsolete and has been superseded by [SimpleHoleFeatureData2::Type](sldworksAPI.chm::/SimpleHoleFeatureData2/SimpleHoleFeatureData2__Type.htm).

Description

This property gets or sets the type of the simple hole.

Syntax (OLE Automation)

holeType = SimpleHoleFeatureData.Type (VB Get property)

SimpleHoleFeatureData.Type = holeType (VB Set property)

holeType = SimpleHoleFeatureData.GetType ( ) (C++ Get property)

SimpleHoleFeatureData.SetType ( holeType ) (C++ Set property)

| Property: | (long) holeType | Type of the simple hole feature as defined in swEndConditions_e |
| --- | --- | --- |

Syntax (COM)

status = SimpleHoleFeatureData ->get_Type ( &holeType )

status = SimpleHoleFeatureData ->put_Type ( holeType )

| Property: | (int) holeType | Type of the simple hole feature as defined in swEndConditions_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
