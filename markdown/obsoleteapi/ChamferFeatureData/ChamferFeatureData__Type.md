---
title: "ChamferFeatureData::Type"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ChamferFeatureData/ChamferFeatureData__Type.htm"
---

# ChamferFeatureData::Type

This property is obsolete and has been superseded by [ChamferFeatureData2::Type](sldworksAPI.chm::/ChamferFeatureData2/ChamferFeatureData2__Type.htm).

Description

This property gets or sets the chamfer feature type.

Syntax (OLE Automation)

chamferType = ChamferFeatureData.Type (VB Get property)

ChamferFeatureData.Type = chamferType (VB Set property)

chamferType = ChamferFeatureData.GetType ( ) (C++ Get property)

ChamferFeatureData.SetType ( chamferType ) (C++ Set property)

| Property: | ( int ) chamferType | Type of the Chamfer feature (see below) |
| --- | --- | --- |

Syntax (COM)

status = ChamferFeatureData ->get_Type ( &chamferType )

status = ChamferFeatureData ->put_Type ( chamferType )

| Property: | ( int ) chamferType | Type of the Chamfer feature (see below) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The chamfer feature type should have one of the values below.

- 1 = Angle-Distance
- 2 = Distance-Distance
- 3 = Vertex
