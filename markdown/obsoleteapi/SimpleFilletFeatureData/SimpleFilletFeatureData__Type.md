---
title: "SimpleFilletFeatureData::Type"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleFilletFeatureData/SimpleFilletFeatureData__Type.htm"
---

# SimpleFilletFeatureData::Type

This property is obsolete and has been superseded by [SimpleFilletFeatureData2::Type](sldworksAPI.chm::/SimpleFilletFeatureData2/SimpleFilletFeatureData2__Type.htm).

Description

This property gets the simple fillet feature type.

Syntax (OLE Automation)

type = SimpleFilletFeatureData.Type (VB Get property)

type = SimpleFilletFeatureData.GetType ( ) (C++ Get property)

| Property: | ( int ) type | Type of fillet feature: 0 = Constant radius 1 = Variable radius 2 = Face blend |
| --- | --- | --- |

Syntax (COM)

status = SimpleFilletFeatureData ->get_Type ( &type )

| Property: | ( int ) type | Type of fillet feature: 0 = Constant radius 1 = Variable radius 2 = Face blend |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
