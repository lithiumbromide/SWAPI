---
title: "VariableFilletFeatureData::OverflowType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/VariableFilletFeatureData/VariableFilletFeatureData__OverflowType.htm"
---

# VariableFilletFeatureData::OverflowType

This property is obsolete and has been superseded by [VariableFilletFeatureData2::OverflowType](sldworksAPI.chm::/VariableFilletFeatureData2/VariableFilletFeatureData2__OverflowType.htm).

Description

This property gets or sets the variable fillet feature overflow type.

Syntax (OLE Automation)

overflowType = VariableFilletFeatureData.OverflowType (VB Get property)

VariableFilletFeatureData.OverflowType = overflowType (VB Set property)

overflowType = VariableFilletFeatureData.GetOverflowType ( ) (C++ Get property)

VariableFilletFeatureData.SetOverflowType ( overflowType ) (C++ Set property)

| Property: | (int) overflowType | Overflow type of the variable fillet feature: 0 = Default 1 = Keep edge 2 = Keep surface |
| --- | --- | --- |

Syntax (COM)

status = VariableFilletFeatureData ->get_OverflowType ( &overflowType )

status = VariableFilletFeatureData ->put_OverflowType ( overflowType )

| Property: | (int) overflowType | Overflow type of the variable fillet feature: 0 = Default 1 = Keep edge 2 = Keep surface |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
