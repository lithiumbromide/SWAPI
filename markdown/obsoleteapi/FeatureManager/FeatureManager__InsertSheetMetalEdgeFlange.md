---
title: "FeatureManager::InsertSheetMetalEdgeFlange"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertSheetMetalEdgeFlange.htm"
---

# FeatureManager::InsertSheetMetalEdgeFlange

This method is obsolete and has been superseded by [FeatureManager::InsertSheetMetalEdgeFlange2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertSheetMetalEdgeFlange2.htm).

Description

This method inserts an edge flange in this sheet metal part.

Syntax (OLE Automation)

pFeat = FeatureManager.InsertSheetMetalEdgeFlange ( flangeEdge, sketchFeat, booleanOptions, dAngle, dRadius, bendPosition, dOffsetDist, reliefType, dReliefRatio, dReliefWidth, dReliefDepth, flangeSharpType, pCBA)

| Input: | (LPEDGE) flangeEdge | Edge to which to apply a flange |
| --- | --- | --- |
| Input: | (LPFEATURE) sketchFeat | Sketch to use for the flange |
| Input: | (long) booleanOptions | Flange options as defined by swInsertEdgeFlangeOptions_e |
| Input: | (double) dAngle | Flange angle |
| Input: | (double) dRadius | Bend radius |
| Input: | (long) bendPosition | Flange bend position as defined by swFlangePositionTypes_e |
| Input: | (double) dOffsetDist | Length of flange |
| Input: | (long) reliefType | Relief type as defined by swSheetMetalReliefTypes |
| Input: | (double) dReliefRatio | Relief ratio |
| Input: | (double) dReliefWidth | Relief width |
| Input: | (double) dReliefDepth | Relief depth |
| Input: | (long) flangeSharpType | Flange virtual sharp type as defined by swFlangeDimType_e |
| Input: | (LPCUSTOMBENDALLOWANCE) pCBA | If... Then... non-NULL Pointer to CustomBendAllowance object for which required values have been set NULL Parent bend's bend allowance is used |
| If... | Then... |  |
| non-NULL | Pointer to CustomBendAllowance object for which required values have been set |  |
| NULL | Parent bend's bend allowance is used |  |
| Output: | (LPFEATURE) pFeat | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertSheetMetalEdgeFlange ( flangeEdge, sketchFeat, booleanOptions, dAngle, dRadius, bendPosition, dOffsetDist, reliefType, dReliefRatio, dReliefWidth, dReliefDepth, flangeSharpType, pCBA, &pFeat)

| Input: | (LPEDGE) flangeEdge | Edge to which to apply a flange |
| --- | --- | --- |
| Input: | (LPFEATURE) sketchFeat | Sketch to use for the flange |
| Input: | (long) booleanOptions | Flange options as defined by swInsertEdgeFlangeOptions_e |
| Input: | (double) dAngle | Flange angle |
| Input: | (double) dRadius | Bend radius |
| Input: | (long) bendPosition | Flange bend position as defined by swFlangePositionTypes_e |
| Input: | (double) dOffsetDist | Length of flange |
| Input: | (long) reliefType | Relief type as defined by swSheetMetalReliefTypes |
| Input: | (double) dReliefRatio | Relief ratio |
| Input: | (double) dReliefWidth | Relief width |
| Input: | (double) dReliefDepth | Relief depth |
| Input: | (long) flangeSharpType | Flange virtual sharp type as defined by swFlangeDimType_e |
| Input: | (LPCUSTOMBENDALLOWANCE) pCBA | If... Then... non-NULL Pointer to CustomBendAllowance object for which required values have been set NULL Parent bend's bend allowance is used |
| If... | Then... |  |
| non-NULL | Pointer to CustomBendAllowance object for which required values have been set |  |
| NULL | Parent bend's bend allowance is used |  |
| Output: | (LPFEATURE) pFeat | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before calling this method, call ModelDoc2::InsertSketchForEdgeFlange and create a profile for the flange. After creating the profile, call this method to create the flange.
