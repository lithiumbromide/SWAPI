---
title: "VariableFilletFeatureData::DefaultRadius"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/VariableFilletFeatureData/VariableFilletFeatureData__DefaultRadius.htm"
---

# VariableFilletFeatureData::DefaultRadius

This property is obsolete and has been superseded by [VariableFilletFeatureData2::DefaultRadius](sldworksAPI.chm::/VariableFilletFeatureData2/VariableFilletFeatureData2__DefaultRadius.htm).

Description

This property gets or sets the variable fillet feature default fillet radius.

Syntax (OLE Automation)

radius = VariableFilletFeatureData.DefaultRadius (VB Get property)

VariableFilletFeatureData.DefaultRadius = radius (VB Set property)

radius = VariableFilletFeatureData.GetDefaultRadius ( ) (C++ Get property)

VariableFilletFeatureData.SetDefaultRadius ( radius ) (C++ Set property)

| Property: | (double) radius | Default fillet radius of the variable fillet feature |
| --- | --- | --- |

Syntax (COM)

status = VariableFilletFeatureData ->get_DefaultRadius ( &radius )

status = VariableFilletFeatureData ->put_DefaultRadius ( radius )

| Property: | (double) radius | Default fillet radius of the variable fillet feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
