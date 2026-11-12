---
title: "FeatureManager::FeatureExtrusion"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__FeatureExtrusion.htm"
---

# FeatureManager::FeatureExtrusion

This method is obsolete and has been superseded by [FeatureManager::FeatureExtrusion2](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureExtrusion2.htm).

Description

This method creates an extruded feature.

Syntax (OLE Automation)

pFeat = FeatureManager.FeatureExtrusion ( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1, offsetReverse2, translateSurface1, translateSurface2, merge, useFeatScope, useAutoSelect )

| Input: | (VARIANT_BOOL) sd | TRUE for single ended, FALSE for double ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | TRUE to flip the direction to cut |
| Input: | (VARIANT_BOOL) dir | TRUE to flip the direction to extrude |
| Input: | (long) t1 | Termination type for first end as defined in swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined in swEndConditions_e |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meter |
| Input: | (VARIANT_BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) ddir1 | TRUE for first draft angle to be inward, FALSE to be outward |
| Input: | (VARIANT_BOOL) ddir2 | TRUE for second draft angle to be inward, FALSE to be outward |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (VARIANT_BOOL) offsetReverse1 | If you chose to offset the first end condition from another face or plane, then TRUE specifies offset in direction away from the sketch, FALSE specifies offset from the face or plane in direction toward the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | If you chose to offset the second end condition from another face or plane, then TRUE specifies offset in direction away from the sketch, FALSE specifies offset from the face or plane in direction toward the sketch |
| Input: | (VARIANT_BOOL) translateSurface1 | When you choose swEndcondOffsetFromSurface as the termination type for the first end, then TRUE specifies that the end of the extrusion is a translation of the reference surface, FALSE specifies to use a true offset |
| Input: | (VARIANT_BOOL) translateSurface2 | When you choose swEndcondOffsetFromSurface as the termination type for the second end, then TRUE specifies that the end of the extrusion is a translation of the reference surface, FALSE specifies to use a true offset |
| Input: | (VARIANT_BOOL) merge | TRUE to merge the results in a multibody part, FALSE to not |
| Input: | (VARIANT_BOOL) useFeatScope | TRUE if the feature only affects selected bodies, FALSE if the feature affects all bodies |
| Input: | (VARIANT_BOOL) useAutoSelect | TRUE to automatically select all bodies and have the feature affect those bodies, FALSE to select the bodies the feature affects (see Remarks ) |
| Output: | (LPFEATURE) pFeat | Pointer to the feature object |

Syntax (COM)

status = FeatureManager->FeatureExtrusion ( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1, offsetReverse2, translateSurface1, translateSurface2, merge, useFeatScope, useAutoSelect, &pFeat )

| Input: | (VARIANT_BOOL) sd | TRUE for single ended, FALSE for double ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | TRUE to flip the direction to cut |
| Input: | (VARIANT_BOOL) dir | TRUE to flip the direction to extrude |
| Input: | (long) t1 | Termination type for first end as defined in swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined in swEndConditions_e |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meter |
| Input: | (VARIANT_BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) ddir1 | TRUE for first draft angle to be inward, FALSE to be outward |
| Input: | (VARIANT_BOOL) ddir2 | TRUE for second draft angle to be inward, FALSE to be outward |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (VARIANT_BOOL) offsetReverse1 | If you chose to offset the first end condition from another face or plane, then TRUE specifies offset in direction away from the sketch, FALSE specifies offset from the face or plane in direction toward the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | If you chose to offset the second end condition from another face or plane, then TRUE specifies offset in direction away from the sketch, FALSE specifies offset from the face or plane in direction toward the sketch |
| Input: | (VARIANT_BOOL) translateSurface1 | When you choose swEndcondOffsetFromSurface as the termination type for the first end, then TRUE specifies that the end of the extrusion is a translation of the reference surface, FALSE specifies to use a true offset |
| Input: | (VARIANT_BOOL) translateSurface2 | When you choose swEndcondOffsetFromSurface as the termination type for the second end, then TRUE specifies that the end of the extrusion is a translation of the reference surface, FALSE specifies to use a true offset |
| Input: | (VARIANT_BOOL) merge | TRUE to merge the results in a multibody part, FALSE to not |
| Input: | (VARIANT_BOOL) useFeatScope | TRUE if the feature only affects selected bodies, FALSE if the feature affects all bodies |
| Input: | (VARIANT_BOOL) useAutoSelect | TRUE if the feature only affects selected bodies, FALSE if the feature affects all bodies (see Remarks ) |
| Output: | (LPFEATURE) pFeat | Pointer to the feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

When useAutoSelect is FALSE, the user must select the bodies that the feature will affect.

When using cut or cavity features that result in multiple bodies, you cannot select to keep all of the resulting bodies or one or more selected bodies.

To extrude a 3D sketch, select:

- 3D sketch with selection mark 0
- Extrusion direction edge with selection mark 16
