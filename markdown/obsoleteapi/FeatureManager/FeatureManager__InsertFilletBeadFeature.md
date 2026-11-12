---
title: "FeatureManager::InsertFilletBeadFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertFilletBeadFeature.htm"
---

# FeatureManager::InsertFilletBeadFeature

This method is obsolete and has been superseded by [FeatureManager::InsertFilletBeadFeature2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertFilletBeadFeature2.htm).

Description

This method inserts a fillet weld bead feature.

Syntax (OLE Automation)

retval = FeatureManager.InsertFilletBeadFeature ( type1, size1, length1, pitch, type2, size2, length2, flag, edgeNum1, deSelEdge1, edgeNum2, deSelEdge2)

| Input: | (short) type1 | First side: 0 = Full length 1 = Intermittent 2 = Staggered |
| --- | --- | --- |
| Input: | (double) size1 | Size of fillet on first side |
| Input: | (double) length1 | Length of fillet on first side |
| Input: | (double) pitch | Pitch, if Intermittent or Staggered on both sides |
| Input: | (short) type2 | Second side: 0= Full length 1 = Intermittent 2= Staggered |
| Input: | (double) size2 | Size of fillet on second side |
| Input: | (double) length2 | Length of fillet on second side |
| Input: | (long) flag | 0 = One-sided and no tangent propagation 1 = Two-sided 2 = Tangent propagation 3 = Two-sided and tangent propagation |
| Input: | (long) edgeNum1 | Number of intersecting edges on first side |
| Input: | (VARIANT) deSelEdge1 | Array indicating if intersecting edges are selected (0) or deselected (1) on first side |
| Input: | (long) edgeNum2 | Number of intersecting edges on second side |
| Input: | (VARIANT) deSelEdge2 | Array indicating if intersecting edges are selected (0) or deselected (1) on second side |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertFilletBeadFeature ( type1, size1, length1, pitch, type2, size2, length2, flag, edgeNum1, deSelEdge1, edgeNum2, deSelEdge2, &retval)

| Input: | (short) type1 | First side: 0 = Full length 1 = Intermittent 2 = Staggered |
| --- | --- | --- |
| Input: | (double) size1 | Size of fillet on first side |
| Input: | (double) length1 | Length of fillet on first side |
| Input: | (double) pitch | Pitch, if Intermittent or Staggered on both sides |
| Input: | (short) type2 | Second side: 0 = Full length 2 = Intermittent 3 = Staggered |
| Input: | (double) size2 | Size of fillet on second side |
| Input: | (double) length2 | Length of fillet on second side |
| Input: | (long) flag | 0 = One-sided and no tangent propagation 1 = Two-sided 2 = Tangent propagation 3 = Two-sided and tangent propagation |
| Input: | (long) edgeNum1 | Number of intersecting edges on first side |
| Input: | (VARIANT) deSelEdge1 | Array indicating if intersecting edges are selected (0) or deselected (1) on first side |
| Input: | (long) edgeNum2 | Number of intersecting edges on second side |
| Input: | (VARIANT) deSelEdge2 | Array indicating if intersecting edges are selected (0) or deselected (1) on second side |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
