---
title: "ModelDoc::FeatureBoss"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureBoss.htm"
---

# ModelDoc::FeatureBoss

This method is obsolete and has been superseded by [ModelDoc2::FeatureBoss](../ModelDoc2/ModelDoc2__FeatureBoss.htm).

Description

This method creates an extruded boss feature.

Syntax (OLE Automation)

void ModelDoc.FeatureBoss ( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1, offsetReverse2)

| Input: | (BOOL) sd | TRUE for single ended, FALSE for double ended |
| --- | --- | --- |
| Input: | (BOOL) flip | Not used |
| Input: | (BOOL) dir | Reverse direction; TRUE if you want Direction1 to be opposite the default direction |
| Input: | (long) t1 | Termination type for first end |
| Input: | (long) t2 | Termination type for second end |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (BOOL) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (BOOL) ddir1 | For first draft angle to be inward, use TRUE; for draft angle outward, use FALSE |
| Input: | (BOOL) ddir2 | For second draft angle to be inward, use TRUE; for draft angle outward ,use FALSE |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (BOOL) offsetReverse1 | If you chose to offset the first end condition from another face or plane, then TRUE specifies offset in direction away from the sketch and FALSE specifies offset from the face or plane in a direction toward the sketch |
| Input: | (BOOL) offsetReverse2 | If you chose to offset the second end condition from another face or plane, then TRUE specifies offset in direction away from the sketch and FALSE would specifies offset from the face or plane in a direction toward the sketch |

Syntax (COM)

status = ModelDoc->FeatureBoss ( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1, offsetReverse2 )

| Input: | (VARIANT_BOOL) sd | TRUE for single ended, FALSE for double ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | Not used |
| Input: | (VARIANT_BOOL) dir | Reverse direction; TRUE if you want Direction1 to be opposite the default direction |
| Input: | (long) t1 | Termination type for first end |
| Input: | (long) t2 | Termination type for second end |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (VARIANT_BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) ddir1 | For first draft angle to be inward use TRUE, for draft angle outward use FALSE |
| Input: | (VARIANT_BOOL) ddir2 | For second draft angle to be inward use TRUE, for draft angle outward use FALSE |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (VARIANT_BOOL) offsetReverse1 | If you chose to offset the first end condition from another face or plane, then TRUE specifies offset in direction away from the sketch and FALSE specifies offset from the face or plane in a direction toward the sketch. |
| Input: | (VARIANT_BOOL) offsetReverse2 | If you chose to offset the second end condition from another face or plane, th3n TRUE specifies offset in direction away from the sketch and FALSE specifies offset from the face or plane in a direction toward the sketch. |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Termination type may be any of the values in the swEndConditions_e enumeration.

The default direction for cut operations are opposite the sketch normal. The default direction for boss operations is along the sketch normal. Setting the ddir1 and ddir2 arguments to TRUE reverses the default direction. For double-ended extrusions, Direction2 is always be opposite of Direction1.

The default sketch normal is the same as the face or plane normal where the sketch was placed. To determine this normal vector, see Face2::Normal and RefPlane::GetRefPlaneParams, respectively.
