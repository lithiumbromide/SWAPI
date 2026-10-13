---
title: "ModelDoc2::InsertSheetMetalEdgeFlange"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertSheetMetalEdgeFlange.htm"
---

# ModelDoc2::InsertSheetMetalEdgeFlange

This method is obsolete and has been superseded by [FeatureManager::InsertSheetMetalEdgeFlange](../FeatureManager/FeatureManager__InsertSheetMetalEdgeFlange.htm).

Description

This method inserts a sheet metal edge flange in this model document.

Syntax (OLE Automation)

void ModelDoc2.InsertSheetMetalEdgeFlange ( flangeEdge, sketchFeat, booleanOptions, dAngle, dRadius, bendPosition, dOffsetDist, reliefType, dReliefRatio, dReliefWidth, dReliefDepth, &retval )

| Input: | (LPDISPATCH) flangeEdge | Edge to which to apply flange |
| --- | --- | --- |
| Input: | (LPDISPATCH) sketchFeat | Sketch to use for flange |
| Input: | (long) booleanOptions | Flange options as defined in swInsertEdgeFlangeOptions_e |
| Input: | (double) dAngle | Flange angle |
| Input: | (double) dRadius | Bend radius |
| Input: | (long) bendPosition | Flange position as defined in swFlangePositionTypes_e |
| Input: | (double) dOffsetDist | Flange length |
| Input: | (long) reliefType | Relief type as defined in swSheetMetalReliefTypes |
| Input: | (double) dReliefRatio | Relief ratio |
| Input: | (double) dReliefWidth | Relief width |
| Input: | (double) dReliefDepth | Relief depth |
| Output: | (LPDISPATCH) retval | Pointer to the new edge flange |

Syntax (COM)

status = ModelDoc2->IInsertSheetMetalEdgeFlange ( flangeEdge, sketchFeat, booleanOptions, dAngle, dRadius, bendPosition, dOffsetDist, reliefType, dReliefRatio, dReliefWidth, dReliefDepth, &retval )

| Input: | (LPEDGE) flangeEdge | Edge to which to apply flange |
| --- | --- | --- |
| Input: | (LPFEATURE) sketchFeat | Sketch to use for flange |
| Input: | (long) booleanOptions | Flange options as defined in swInsertEdgeFlangeOptions_e |
| Input: | (double) dAngle | Flange angle |
| Input: | (double) dRadius | Bend radius |
| Input: | (long) bendPosition | Flange position as defined in swFlangePositionTypes_e |
| Input: | (double) dOffsetDist | Flange length |
| Input: | (long) reliefType | Relief type as defined in swSheetMetalReliefTypes |
| Input: | (double) dReliefRatio | Relief ratio |
| Input: | (double) dReliefWidth | Relief width |
| Input: | (double) dReliefDepth | Relief depth |
| Output: | (LPFEATURE) retval | Pointer to the new edge flange |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDoc2::InsertSketchForEdgeFlange to create a sketch for this method.
