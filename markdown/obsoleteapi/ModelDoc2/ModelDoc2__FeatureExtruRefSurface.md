---
title: "ModelDoc2::FeatureExtruRefSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureExtruRefSurface.htm"
---

# ModelDoc2::FeatureExtruRefSurface

This method is obsolete and has been superseded by [ModelDoc2::FeatureExtruRefSurface2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FeatureExtruRefSurface2.htm).

Description

This method creates an extruded reference surface in a part according to the options specified.

Syntax (OLE Automation)

void ModelDoc2.FeatureExtruRefSurface ( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1, offsetReverse2)

| Input: | (BOOL) sd | TRUE for single-ended, FALSE for double-ended |
| --- | --- | --- |
| Input: | (BOOL) flip | TRUE to flip the direction to cut |
| Input: | (BOOL) dir | TRUE to flip direction to extrude |
| Input: | (long) t1 | Termination type for first end as defined swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined swEndConditions_e |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (BOOL) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (BOOL) ddir1 | TRUE for first draft angle to be inward, FALSE for draft angle outward |
| Input: | (BOOL) ddir2 | TRUE for second draft angle to be inward, FALSE for draft angle outward |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (BOOL) offsetReverse1 | TRUE specifies offset in direction away from the sketch if you chose to offset the first end condition from another face or plane, FALSE specifies offset from the face or plane in a direction toward the sketch |
| Input: | (BOOL) offsetReverse2 | TRUE specifies offset in direction away from the sketch if you chose to offset the second end condition from another face or plane, FALSE specifies offset from the face or plane in a direction toward the sketch |

Syntax (COM)

status = ModelDoc2->FeatureExtruRefSurface ( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1, offsetReverse2 )

| Input: | (VARIANT_BOOL) sd | TRUE for single-ended, FALSE for double-ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | TRUE to flip the direction to cut |
| Input: | (VARIANT_BOOL) dir | TRUE to flip direction to extrude |
| Input: | (long) t1 | Termination type for first end as defined swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined swEndConditions_e |
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
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is similar to the ModelDoc2::FeatureBoss method. Both methods insert extrusion entities. This method creates surfaces, and ModelDoc2::FeatureBoss creates solid bodies.
