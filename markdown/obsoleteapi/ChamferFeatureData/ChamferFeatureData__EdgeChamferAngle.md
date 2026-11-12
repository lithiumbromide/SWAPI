---
title: "ChamferFeatureData::EdgeChamferAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ChamferFeatureData/ChamferFeatureData__EdgeChamferAngle.htm"
---

# ChamferFeatureData::EdgeChamferAngle

This property is obsolete and has been superseded by [ChamferFeatureData2::EdgeChamferAngle](sldworksAPI.chm::/ChamferFeatureData2/ChamferFeatureData2__EdgeChamferAngle.htm).

Description

This property gets or sets the chamfer feature edge chamfer angle.

Syntax (OLE Automation)

angle = ChamferFeatureData.EdgeChamferAngle (VB Get property)

ChamferFeatureData.EdgeChamferAngle = angle (VB Set property)

angle = ChamferFeatureData.GetEdgeChamferAngle ( ) (C++ Get property)

ChamferFeatureData.SetEdgeChamferAngle ( angle ) (C++ Set property)

| Property: | ( double ) angle | Chamfer angle of the chamfer feature edge |
| --- | --- | --- |

Syntax (COM)

status = ChamferFeatureData ->get_EdgeChamferAngle ( &angle )

status = ChamferFeatureData ->put_EdgeChamferAngle ( angle )

| Property: | ( double ) angle | Chamfer angle of the chamfer feature edge |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for angle-distance type chamfers.
