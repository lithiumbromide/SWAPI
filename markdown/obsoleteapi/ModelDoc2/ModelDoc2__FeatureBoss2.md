---
title: "ModelDoc2::FeatureBoss2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureBoss2.htm"
---

# ModelDoc2::FeatureBoss2

This method is obsolete and has been superseded by [FeatureManager::FeatureExtrusion2](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureExtrusion2.htm).

Description

This method creates an extruded boss feature.

Syntax (OLE Automation)

void = ModelDoc2.FeatureBoss2 ( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1, offsetReverse2, translateSurface1, translateSurface2 )

| Input: | (VARIANT_BOOL) sd | TRUE for single-ended, FALSE for double-ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | Not used |
| Input: | (VARIANT_BOOL) dir | TRUE if you want Direction 1 to be opposite the default direction (see Remarks ) |
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
| Input: | (VARIANT_BOOL) offsetReverse1 | TRUE specifies offset away from the sketch if you chose to offset the first end condition from another face or plane, FALSE specifies offset from the face or plane toward the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | TRUE specifies offset away from the sketch if you chose to offset the second end condition from another face or plane, FALSE specifies offset from the face or plane toward the sketch |
| Input: | (VARIANT_BOOL) translateSurface1 | If you choose swEndcondOffsetFromSurface as the termination type for the first end, then TRUE specifies that the end of the extrusion is a translation of the reference surface, FALSE specifies to use a true offset |
| Input: | (VARIANT_BOOL) translateSurface2 | If you choose swEndcondOffsetFromSurface as the termination type for the second end, then TRUE specifies that the end of the extrusion is a translation of the reference surface, FALSE specifies to use a true offset |

Syntax (COM)

status = ModelDoc2->FeatureBoss2 ( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1, offsetReverse2, translateSurface1, translateSurface2 )

| Input: | (VARIANT_BOOL) sd | TRUE for single-ended, FALSE for double-ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | Not used |
| Input: | (VARIANT_BOOL) dir | TRUE if you want Direction 1 to be opposite the default direction (see Remarks ) |
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
| Input: | (VARIANT_BOOL) offsetReverse1 | If you chose to offset the first end condition from another face or plane then TRUE specifies offset in direction away from the sketch, FALSE specifies offset from the face or plane in a direction toward the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | If you chose to offset the second end condition from another face or plane then TRUE specifies offset in direction away from the sketch, FALSE specifies offset from the face or plane in a direction toward the sketch |
| Input: | (VARIANT_BOOL) translateSurface1 | If you choose swEndcondOffsetFromSurface as the termination type for the first end, then TRUE specifies that the end of the extrusion is a translation of the reference surface, FALSE specifies to use a true offset |
| Input: | (VARIANT_BOOL) translateSurface2 | If you choose swEndcondOffsetFromSurface as the termination type for the second end, then TRUE specifies that the end of the extrusion is a translation of the reference surface, FALSE specifies to use a true offset |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The default direction for cut operations is opposite the sketch normal. The default direction for boss operations is along the sketch normal. Setting the dir argument to TRUE reverses the default direction. For double-ended extrusions, Direction 2 is always opposite of Direction 1.

The default sketch normal is the same as the face or pPlane normal where the sketch was placed. To determine this normal vector, see Face2::Normal and RefPlane::Transform, respectively.
