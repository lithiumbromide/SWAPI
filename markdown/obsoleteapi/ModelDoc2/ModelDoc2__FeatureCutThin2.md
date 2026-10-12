---
title: "ModelDoc2::FeatureCutThin2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureCutThin2.htm"
---

# ModelDoc2::FeatureCutThin2

This method is obsolete and has been superseded by [FeatureManager::FeatureCutThin](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureCutThin.htm).

Description

This method creates a cut thin feature.

Syntax (OLE Automation)

void = ModelDoc2.FeatureCutThin2 ( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1, offsetReverse2, translateSurface1, translateSurface2, thk1, thk2, endThk, revThinDir, capEnds, addBends, bendRad )

| Input: | (VARIANT_BOOL) sd | TRUE for single-ended, FALSE for double-ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | Flip side to cut; TRUE if you want to remove the material outside of the profile |
| Input: | (VARIANT_BOOL) dir | Reverse direction; TRUE if you want Direction1 to be opposite the default direction |
| Input: | (long) t1 | Termination type for first end as defined in swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined in swEndConditions_e |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (VARIANT_BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) ddir1 | TRUE for first draft angle to be inward, FALSE for draft angle outward |
| Input: | (VARIANT_BOOL) ddir2 | TRUE for second draft angle to be inward, FALSE for draft angle outward |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (VARIANT_BOOL) offsetReverse1 | TRUE specifies offset in direction away from the sketch if you chose to offset the first end condition from another face or plane, FALSE specifies offset from the face or plane in a direction toward the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | TRUE specifies offset in direction away from the sketch if you chose to offset the second end condition from another face or plane, FALSE specifies offset from the face or plane in a direction toward the sketch |
| Input: | (VARIANT_BOOL) translateSurface1 | TRUE specifies that the end of the extrusion is a translation of the reference surface if you choose swEndcondOffsetFromSurface as the termination type for the first end, FALSE specifies to use a true offset |
| Input: | (VARIANT_BOOL) translateSurface2 | TRUE specifies that the end of the extrusion is a translation of the reference surface if you choose swEndcondOffsetFromSurface as the termination type for the second end, FALSE specifies to use a true offset |
| Input: | (double) thk1 | Wall thickness 1 (midplane uses (thk1)/2 for each direction) |
| Input: | (double) thk2 | Wall thickness 2 (only used when thinType = 3) |
| Input: | (double) endThk | End cap thickness (only used when capEnds = 1) |
| Input: | (long) revThinDir | Thin feature type: 0 = one direction 1 = one direction reverse 2 = midplane 3 = two direction |
| Input: | (long) capEnds | Cap the ends: 0 = no cap 1 = cap (base features only) |
| Input: | (VARIANT_BOOL) addBends | TRUE to add auto-bends (open profile base features only) |
| Input: | (double) bendRad | Fillet radii if addBends is TRUE |

Syntax (COM)

status = ModelDoc2->FeatureCutThin2 ( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1, offsetReverse2, translateSurface1, translateSurface2, thk1, thk2, endThk, revThinDir, capEnds, addBends, bendRad )

| Input: | (VARIANT_BOOL) sd | TRUE for single-ended, FALSE for double-ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | Flip side to cut; TRUE if you want to remove the material outside of the profile |
| Input: | (VARIANT_BOOL) dir | Reverse direction; TRUE if you want Direction 1 to be opposite the default direction |
| Input: | (long) t1 | Termination type for first end as defined in swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined in swEndConditions_e |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (VARIANT_BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) ddir1 | TRUE for first draft angle to be inward, FALSE for draft angle outward |
| Input: | (VARIANT_BOOL) ddir2 | TRUE for second draft angle to be inward, FALSE for draft angle outward |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (VARIANT_BOOL) offsetReverse1 | TRUE specifies offset in direction away from the sketch if you chose to offset the first end condition from another face or plane, FALSE specifies offset from the face or plane in a direction toward the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | TRUE specifies offset in direction away from the sketch if you chose to offset the second end condition from another face or plane, FALSE specifies offset from the face or plane in a direction toward the sketch |
| Input: | (VARIANT_BOOL) translateSurface1 | TRUE specifies that the end of the extrusion is a translation of the reference surface if you choose swEndcondOffsetFromSurface as the termination type for the first end, FALSE specifies to use a true offset |
| Input: | (VARIANT_BOOL) translateSurface2 | TRUE specifies that the end of the extrusion is a translation of the reference surface if you choose swEndcondOffsetFromSurface as the termination type for the second end, FALSE specifies to use a true offset |
| Input: | (double) thk1 | Wall thickness 1 (midplane uses (thk1)/2 for each direction) |
| Input: | (double) thk2 | Wall thickness 2 (only used when thinType = 3) |
| Input: | (double) endThk | End cap thickness (only used when capEnds = 1) |
| Input: | (long) revThinDir | Thin feature type: 0 = one direction 1 = one direction reverse 2 = midplane 3 = two direction |
| Input: | (long) capEnds | Cap the ends: 0 = no cap 1 = cap (base features only) |
| Input: | (VARIANT_BOOL) addBends | TRUE to add auto-bends (open profile base features only) |
| Input: | (double) bendRad | Fillet radii if addBends is TRUE |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
