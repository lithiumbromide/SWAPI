---
title: "FeatureManager::InsertRuledSurfaceFromEdge"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertRuledSurfaceFromEdge.htm"
---

# FeatureManager::InsertRuledSurfaceFromEdge

This method is obsolete and has been superseded by [FeatureManager::InsertRuledSurfaceFromEdge2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertRuledSurfaceFromEdge2.htm).

Description

This method inserts a surface from the selected edge on this feature.

Syntax (OLE Automation)

retval = FeatureManager.InsertRuledSurfaceFromEdge ( type, length, flipPullDir, flipDir, trimAndSew, angle, coordInput, x, y, z )

| Input: | (long) type | 0 = Tangent to Surface 1 = Normal to Surface 2 = Tapered to Vector 3 = Perpendicular to Vector 4 = Sweep |
| --- | --- | --- |
| Input: | (double) length | Distance at which to create the surface; valid for Tangent to Surface, Tapered to Vector, Perpendicular to Vector, and Sweep types only |
| Input: | (VARIANT_BOOL) flipPullDir | TRUE to flip the pull direction, FALSE to not; valid for Normal to Surface and Tapered to Vector types only |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the direction, FALSE to not; valid for Perpendicular to Vector type only |
| Input: | (VARIANT_BOOL) trimAndSew | Trim and knit the surface, FALSE to not |
| Input: | (double) angle | Angle for Tapered to Vector type only |
| Input: | (VARIANT_BOOL) coordInput | TRUE to enable coordinate input, FALSE if not; for Sweep type only |
| Input: | (double) x | x coordinate |
| Input: | (double) y | y coordinate |
| Input: | (double) z | z coordinate |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertRuledSurfaceFromEdge ( type, length, flipPullDir, flipDir, trimAndSew, angle, coordInput, x, y, z, &retval )

| Input: | (long) type | 0 = Tangent to Surface 1 = Normal to Surface 2 = Tapered to Vector 3 = Perpendicular to Vector 4 = Sweep |
| --- | --- | --- |
| Input: | (double) length | Distance at which to create the surface; valid for Tangent to Surface, Tapered to Vector, Perpendicular to Vector, and Sweep types only |
| Input: | (VARIANT_BOOL) flipPullDir | TRUE to flip the pull direction, FALSE to not; valid for Normal to Surface and Tapered to Vector types only |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the direction, FALSE to not; valid for Perpendicular to Vector type only |
| Input: | (VARIANT_BOOL) trimAndSew | Trim and knit the surface, FALSE to not |
| Input: | (double) angle | Angle for Tapered to Vector type only |
| Input: | (VARIANT_BOOL) coordInput | TRUE to enable coordinate input, FALSE if not; for Sweep type only |
| Input: | (double) x | x coordinate |
| Input: | (double) y | y coordinate |
| Input: | (double) z | z coordinate |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
