---
title: "FeatureManager::InsertCutSwept"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertCutSwept.htm"
---

# FeatureManager::InsertCutSwept

This method is obsolete and has been superseded by [FeatureManager::InsertCutSwept2](FeatureManager__InsertCutSwept2.htm).

Description

This method inserts a swept cut.

Syntax (OLE Automation)

retval = FeatureManager.InsertCutSwept ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType, isThinBody, thickness1, thickness2, thinType, useFeatScope, useAutoSelect )

| Input: | (BOOL) propagate | TRUE propagates the swept cut propagates to the next edge, FALSE causes the swept cut to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (BOOL) alignment | If the curve used to sweep goes from one face to another or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and ends perpendicular to the sweep curve; therefore, it may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options (see Remarks ) |
| Input: | (BOOL) keepTangency | Follow path |
| Input: | (BOOL) forceNonRational | Keep constant normal |
| Input: | (short) startMatchingType | Tangency type (see Remarks ) |
| Input: | (short) endMatchingType | Tangency type (see Remarks ) |
| Input: | (BOOL) isThinBody | TRUE if this feature is a thin body, FALSE if not |
| Input: | (double) thickness1 | Thickness value for the first direction. |
| Input: | (double) thickness2 | Thickness value for the second direction. |
| Input: | (short) thinType | Thin wall type (see Remarks ) |
| Input: | (VARIANT_BOOL) useFeatScope | TRUE if the feature only affects selected bodies, FALSE if the feature affects all bodies |
| Input: | (VARIANT_BOOL) useAutoSelect | TRUE to automatically select all bodies and have the feature affect those bodies, FALSE to select the bodies the feature affects (see Remarks ) |
| Output: | (LPFEATURE) *retval | Pointer to the feature object |

Syntax (COM)

status = FeatureManager->InsertCutSwept ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType, isThinBody, thickness1, thickness2, thinType, useFeatScope, useAutoSelect, retval )

| Input: | (BOOL) propagate | TRUE propagates the swept cut propagates to the next edge, FALSE causes the swept cut to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (BOOL) alignment | If the curve used to sweep goes from one face to another or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and ends perpendicular to the sweep curve; therefore, it may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options (see Remarks ) |
| Input: | (BOOL) keepTangency | Follow path |
| Input: | (BOOL) forceNonRational | Keep constant normal |
| Input: | (short) startMatchingType | Tangency type (see Remarks ) |
| Input: | (short) endMatchingType | Tangency type (see Remarks ) |
| Input: | (BOOL) isThinBody | TRUE if this feature is a thin body, FALSE if not |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | Thin wall type (see Remarks ) |
| Input: | (VARIANT_BOOL) useFeatScope | TRUE if the feature only affects selected bodies, FALSE if the feature affects all bodies |
| Input: | (VARIANT_BOOL) useAutoSelect | TRUE to automatically select all bodies and have the feature affect those bodies, FALSE to select the bodies the feature affects (see Remarks ) |
| Output: | (LPFEATURE) *retval | Pointer to the feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDocExtension::SelectByID to select the profile and sweep curves. The mark for:

Profile selection should be a 1

Sweep path should be 4

Guide-curve selection should be 2

The twistCtrlOption argument can take one of these values:

0 = Follow path

1 = Keep constant normal

2 = Follow path and first guide curve

3 = Follow first and second guide curve

The tangency type arguments can take one of these following values:

0 - none

1 - tangent to the normal of the profile

2 - tangent to a selected vector

3 - tangency to all the adjacent faces sharing an edge with the start profile

4 - tangent to some of the selected faces sharing an edge with the start profile (not available)

The thinType arguemnt can take one of these values:

0 = One direction

1 = One direction reverse

2 = Mid-plane

3 = Two direction

When useAutoSelect is FALSE, the user must select the bodies that the feature will affect.

When using cut or cavity features that result in multiple bodies, you cannot select to keep all of the resulting bodies or one or more selected bodies.
