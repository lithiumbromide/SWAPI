---
title: "ModelDoc::InsertSheetMetalBaseFlange"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSheetMetalBaseFlange.htm"
---

# ModelDoc::InsertSheetMetalBaseFlange

This method is obsolete and has been superseded by [ModelDoc2::InsertSheetMetalBaseFlange](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertSheetMetalBaseFlange.htm).

Description

Given a selected sketch or active sketch, this method inserts a sheet metal base flange feature.

Syntax (OLE Automation)

voidModelDoc.InsertSheetMetalBaseFlange ( thickness, thickenDir, radius, extrudeDist1, extrudeDist2, flipExtruDir, endCondition1, endCondition2, dirToUse)

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

status = ModelDoc->InsertSheetMetalBaseFlange ( thickness, thickenDir, radius, extrudeDist1, extrudeDist2, flipExtruDir, endCondition1, endCondition2, dirToUse)

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
| thickenDir | Refers to the direction that the profile will be offset and thus the thickness of the resulting sheet metal flange. TRUE will thicken to the inside, FALSE will thicken to the outside. |
| flipExtruDir | Refers to the direction the extrude distance will go from the sketch plane. If this value is TRUE, the direction will be reversed from the default direction. |
| endCondition1 and endCondition2 | Can have values of: 0 – use the distance, 1 – extrude up to a point, or 2 – extrude up to a surface. For a midplane distance, endCondition1 and endCondition2 should be equal and each half the desired distance. |
| dirToUse | Refers to which direction to use:0 – use both directions, 1 – use the first direction, or 2 – use the second direction. |
