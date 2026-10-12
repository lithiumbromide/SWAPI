---
title: "ExtrudeFeatureData::ThinWallType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__ThinWallType.htm"
---

# ExtrudeFeatureData::ThinWallType

This property is obsolete and has been superseded by [ExtrudeFeatureData2::ThinWallType](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__ThinWallType.htm).

Description

This property gets or sets the thin wall type for a thin base extrude feature.

Syntax (OLE Automation)

thinWallType = ExtrudeFeatureData.ThinWallType (VB Get property)

ExtrudeFeatureData.ThinWallType = thinWallType (VB Set property)

thinWallType = ExtrudeFeatureData.GetThinWallType ( ) (C++ Get property)

ExtrudeFeatureData.SetThinWallType ( thinWallType ) (C++ Set property)

| Property: | (int) thinWallType | Thin feature type: 0 = One Direction 1 = One Direction Reverse 2 = MidPlane 3 = Two Direction |
| --- | --- | --- |

Syntax (COM)

status = ExtrudeFeatureData->get_ThinWallType ( &thinWallType )

status = ExtrudeFeatureData->put_ThinWallType ( thinWallType )

| Property: | (int) thinWallType | Thin feature type: 0 = One Direction 1 = One Direction Reverse 2 = MidPlane 3 = Two Direction |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
