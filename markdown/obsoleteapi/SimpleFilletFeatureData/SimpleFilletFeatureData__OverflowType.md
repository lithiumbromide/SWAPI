---
title: "SimpleFilletFeatureData::OverflowType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleFilletFeatureData/SimpleFilletFeatureData__OverflowType.htm"
---

# SimpleFilletFeatureData::OverflowType

This property is obsolete and has been superseded by [SimpleFilletFeatureData2::OverflowType](sldworksAPI.chm::/SimpleFilletFeatureData2/SimpleFilletFeatureData2__OverflowType.htm).

Description

This property gets or sets the simple fillet feature overflow type.

Syntax (OLE Automation)

overflowType = SimpleFilletFeatureData.OverflowType (VB Get property)

SimpleFilletFeatureData.OverflowType = overflowType (VB Set property)

overflowType = SimpleFilletFeatureData.GetOverflowType ( ) (C++ Get property)

SimpleFilletFeatureData.SetOverflowType ( overflowType ) (C++ Set property)

| Property: | (int) overflowType | Overflow type of the simple fillet feature: 0 = Default 1 = Keep edge 2 = Keep surface |
| --- | --- | --- |

Syntax (COM)

status = SimpleFilletFeatureData ->get_OverflowType ( &overflowType )

status = SimpleFilletFeatureData ->put_OverflowType ( overflowType )

| Property: | (int) overflowType | Overflow type of the simple fillet feature: 0 = Default 1 = Keep edge 2 = Keep surface |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
