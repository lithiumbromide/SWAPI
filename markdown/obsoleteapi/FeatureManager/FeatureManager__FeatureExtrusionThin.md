---
title: "FeatureManager::FeatureExtrusionThin"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__FeatureExtrusionThin.htm"
---

# FeatureManager::FeatureExtrusionThin

This method is obsolete and has been superseded by [FeatureManager::FeatureExtrusionThin2](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureExtrusionThin2.htm).

Description

This method creates an extruded thin feature.

Syntax (OLE Automation)

pFeat = FeatureManager.FeatureExtrusionThin ( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1, offsetReverse2, translateSurface1, translateSurface2, merge, thk1, thk2, endThk, revThinDir, capEnds, addBends, bendRad, useFeatScope, useAutoSelect )

| Input: | (VARIANT_BOOL) sd | TRUE for single ended, FALSE for double ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | Not used |
| Input: | (VARIANT_BOOL) dir | Reverse direction TRUE if you want Direction1 to be opposite the default direction (see Remarks ) |
| Input: | (long) t1 | Termination type for first end as defined in swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined in swEndConditions_e |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (VARIANT_BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) ddir1 | TRUE for first draft angle to be inward, FALSE to be outward |
| Input: | (VARIANT_BOOL) ddir2 | TRUE for second draft angle to be inward, FALSE to be outward |
| Input: | (double) dang1 | First draft angle |
| Input: | (double) dang2 | Second draft angle |
| Input: | (VARIANT_BOOL) offsetReverse1 | If you chose to offset the first end condition from another face or plane, then TRUE specifies offset in direction away from the sketch, FALSE specifies offset from the face or plane in direction toward the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | If you chose to offset the second end condition from another face or plane, then TRUE specifies offset in direction away from the sketch, FALSE specifies offset from the face or plane in direction toward the sketch |
| Input: | (VARIANT_BOOL) translateSurface1 | When you choose swEndcondOffsetFromSurface as the termination type for the first end, then TRUE specifies that the end of the extrusion is a translation of the reference surface, FALSE specifies to use a true offset |
| Input: | (VARIANT_BOOL) translateSurface2 | When you choose swEndcondOffsetFromSurface as the termination type for the second end, then TRUE specifies that the end of the extrusion is a translation of the reference surface, FALSE specifies to use a true offset |
| Input: | (double) thk1 | Wall thickness 1 (Mid-plane type uses (thk1)/2 for each direction) |
| Input: | (double) thk2 | Wall thickness 2 (Only used when thinType =3 ) |
| Input: | (double) endThk | End cap thickness (Only used when capEnds = 1) |
| Input: | (long) revThinDir | Thin feature type: 0 = One direction 1 = One direction reverse 2 = Mid-plane 3 = Two direction |
| Input: | (long) capEnds | Cap the ends: 0 = no cap 1 = cap (base features only) |
| Input: | (VARIANT_BOOL) addBends | TRUE to add auto bends (open profile base features only), FALSE to not |
| Input: | (double) bendRad | Fillet radii if addBends = TRUE |
| Input: | (VARIANT_BOOL) useFeatScope | TRUE if the feature only affects selected bodies, FALSE if the feature affects all bodies |
| Input: | (VARIANT_BOOL) useAutoSelect | TRUE to automatically select all bodies and have the feature affect those bodies, FALSE to select the bodies the feature affects (see Remarks ) |
| Output: | (LPFEATURE) pFeat | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->FeatureExtrusionThin ( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1, offsetReverse2, translateSurface1, translateSurface2, merge, thk1, thk2, endThk, revThinDir, capEnds, addBends, bendRad, useFeatScope, useAutoSelect, &pFeat )

| Input: | (VARIANT_BOOL) sd | TRUE for single ended, FALSE for double ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | Not used |
| Input: | (VARIANT_BOOL) dir | Reverse direction TRUE if you want Direction1 to be opposite the default direction (see Remarks ) |
| Input: | (long) t1 | Termination type for first end as defined in swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined in swEndConditions_e |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (VARIANT_BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) ddir1 | TRUE for first draft angle to be inward, FALSE to be outward |
| Input: | (VARIANT_BOOL) ddir2 | TRUE for second draft angle to be inward, FALSE to be outward |
| Input: | (double) dang1 | First draft angle |
| Input: | (double) dang2 | Second draft angle |
| Input: | (VARIANT_BOOL) offsetReverse1 | If you chose to offset the first end condition from another face or plane, then TRUE specifies offset in direction away from the sketch, FALSE specifies offset from the face or plane in direction toward the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | If you chose to offset the second end condition from another face or plane, then TRUE specifies offset in direction away from the sketch, FALSE specifies offset from the face or plane in direction toward the sketch |
| Input: | (VARIANT_BOOL) translateSurface1 | When you choose swEndcondOffsetFromSurface as the termination type for the first end, then TRUE specifies that the end of the extrusion is a translation of the reference surface, FALSE specifies to use a true offset |
| Input: | (VARIANT_BOOL) translateSurface2 | When you choose swEndcondOffsetFromSurface as the termination type for the second end, then TRUE specifies that the end of the extrusion is a translation of the reference surface, FALSE specifies to use a true offset |
| Input: | (double) thk1 | Wall thickness 1 (Mid-plane type uses (thk1)/2 for each direction) |
| Input: | (double) thk2 | Wall thickness 2 (Only used when thinType =3 ) |
| Input: | (double) endThk | End cap thickness (Only used when capEnds = 1) |
| Input: | (long) revThinDir | Thin feature type: 0 = One direction 1 = One direction reverse 2 = Mid-plane 3 = Two direction |
| Input: | (long) capEnds | Cap the ends: 0 = no cap 1 = cap (base features only) |
| Input: | (VARIANT_BOOL) addBends | TRUE to add auto bends (open profile base features only), FALSE to not |
| Input: | (double) bendRad | Fillet radii if addBends = TRUE |
| Input: | (VARIANT_BOOL) useFeatScope | TRUE if the feature only affects selected bodies, FALSE if the feature affects all bodies |
| Input: | (VARIANT_BOOL) useAutoSelect | TRUE to automatically select all bodies and have the feature affect those bodies, FALSE to select the bodies the feature affects (see Remarks ) |
| Output: | (LPFEATURE) pFeat | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The default direction for cut operations are opposite the sketch normal. The default direction for boss operations is along the sketch normal. Setting the dir argument to TRUE reverses the default direction. For double-ended extrusions, Direction 2 is always be opposite to Direction 1.

The default sketch normal is the same as the face or plane normal where the sketch was placed. To determine this normal vector, refer to Face2::Normal and RefPlane::Transform, respectively.

When useAutoSelect is FALSE, the user must select the bodies that the feature will affect.

When using cut or cavity features that result in multiple bodies, you cannot select to keep all of the resulting bodies or one or more selected bodies.
