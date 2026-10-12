---
title: "ModelDoc2::InsertSheetMetalBaseFlange"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertSheetMetalBaseFlange.htm"
---

# ModelDoc2::InsertSheetMetalBaseFlange

This method is obsolete and has been superseded by [FeatureManager::InsertSheetMetalBaseFlange](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertSheetMetalBaseFlange.htm).

Description

This method inserts a sheet metal base flange feature into a selected sketch or an active sketch.

Syntax (OLE Automation)

voidModelDoc2.InsertSheetMetalBaseFlange ( thickness, thickenDir, radius, extrudeDist1, extrudeDist2, flipExtruDir, endCondition1, endCondition2, dirToUse)

| Input: | (double) thickness | Wall thickness of the sheet metal feature |
| --- | --- | --- |
| Input: | (BOOL) thickenDir | Direction to thicken the sheet metal |
| Input: | (double) radius | Global bend radius to insert at the corners |
| Input: | (double) extrudeDist1 | Distance of the sheet metal extrusion for the Direction1 |
| Input: | (double) extrudeDist2 | Distance of the sheet metal extrusion for the Direction2 |
| Input: | (BOOL) flipExtruDir | Reverse extrude direction |
| Input: | (long) endCondition1 | End condition for first extrude distance |
| Input: | (long) endCondition2 | End condition for second extrude distance |
| Input: | (long) dirToUse | Type of end condition |

Syntax (COM)

status = ModelDoc2->InsertSheetMetalBaseFlange ( thickness, thickenDir, radius, extrudeDist1, extrudeDist2, flipExtruDir, endCondition1, endCondition2, dirToUse)

| Input: | (double) thickness | Wall thickness of the sheet metal feature |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) thickenDir | Direction to thicken the sheet metal |
| Input: | (double) radius | Global bend radius to insert at the corners |
| Input: | (double) extrudeDist1 | Distance of the sheet metal extrusion for the Direction1 |
| Input: | (double) extrudeDist2 | Distance of the sheet metal extrusion for the Direction2 |
| Input: | (VARIANT_BOOL) flipExtruDir | Reverse extrude direction |
| Input: | (long) endCondition1 | End condition for first extrude distance |
| Input: | (long) endCondition2 | End condition for second extrude distance |
| Input: | (long) dirToUse | Type of end condition |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

| Argument | Description |
| --- | --- |
| thickenDir | Refers to the direction that the profile is offset; thus, the thickness of the resulting sheet metal flange. TRUE thickens to the inside; FALSE thickens to the outside. |
| flipExtruDir | Refers to the direction the extrude distance goes from the sketch plane. If this value is TRUE, the direction is reversed from the default direction. |
| endCondition1 and endCondition2 | 0 - use the distance 1 - extrude up to a point 2 - extrude up to a surface For a midplane distance, endCondition1 and endCondition2 should be equal and each half the desired distance. |
| dirToUse | Refers to which direction to use. 0 - use both directions 1 - use the first direction 2 - use the second direction |
