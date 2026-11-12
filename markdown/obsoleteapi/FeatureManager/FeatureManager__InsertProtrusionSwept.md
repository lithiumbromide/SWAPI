---
title: "FeatureManager::InsertProtrusionSwept"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertProtrusionSwept.htm"
---

# FeatureManager::InsertProtrusionSwept

This method is obsolete and has been superseded by [FeatureManager::InsertProtrusionSwept2](FeatureManager__InsertProtrusionSwept2.htm).

Description

This method inserts a swept protrusion.

Syntax (OLE Automation)

retval = FeatureManager.InsertProtrusionSwept ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType, isThinBody, thickness1, thickness2, thinType, merge, useFeatScope, useAutoSelect )

| Input: | (BOOL) propagate | TRUE propagates the loft to the next tangent edge, FALSE does not |
| --- | --- | --- |
| Input: | (BOOL) alignment | TRUE causes the sweep to cut completely through the end faces of the cut if the curve used to sweep goes from one face to another or from one edge to another; FALSE causes the swept cut to begin and end perpendicular to the sweep curve and it cannot break through the two end faces of the cut body |
| Input: | (short) twistCtrlOption | 0 = Follow path 1 = Keep constant normal 2 = Follow path and first guide curve 3 = Follow first and second guide curve |
| Input: | (BOOL) keepTangency | TRUE maintains the tangency as in the section curves, FALSE does not If the section curves are tangent, then you can specify whether the resulting faces are also tangent. When generating tangent faces, SolidWorks maintains planar and cylindrical face shapes if the section curves exhibit these characteristics. |
| Input: | (BOOL) forceNonRational | TRUE forces the resulting surface to be non-rational, FALSE does not |
| Input: | (short) startMatchingType | 0 = None 1 = Tangent to the normal of the profile 2 = Tangent to a selected vector 3 = Tangency to all the adjacent faces sharing an edge with the start profile 4 = Tangent to some of the selected faces sharing an edge with the start profile (not available) |
| Input: | (short) endMatchingType | 0 = None 1 = Tangent to the normal of the profile 2 = Tangent to a selected vector 3 = Tangency to all the adjacent faces sharing an edge with the start profile 4 = Tangent to some of the selected faces sharing an edge with the start profile (not available) |
| Input: | (BOOL) isThinBody | TRUE if this feature is a thin body, FALSE if it is not |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | Thin wall type: 0 = One direction 1 = One direction reverse 2 = Mid-plane 3 = Two direction |
| Input: | (BOOL) merge | TRUE to merge the results in the multibody part, FALSE to not |
| Input: | (VARIANT_BOOL) useFeatScope | TRUE if the feature only affects selected bodies, FALSE if the feature affects all bodies |
| Input: | VARIANT_BOOL) useAutoSelect | TRUE to automatically select all bodies and have the feature affect those bodies, FALSE to select the bodies the feature affects |
| Output: | (LPFEATURE) *retval | Pointer to the feature object |

Syntax (COM)

status = FeatureManager->InsertProtrusionSwept ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType, isThinBody, thickness1, thickness2, thinType, merge, useFeatScope, useAutoSelect, retval )

| Input: | (BOOL) propagate | TRUE propagates the loft to the next tangent edge, FALSE does not |
| --- | --- | --- |
| Input: | (BOOL) alignment | TRUE causes the sweep to cut completely through the end faces of the cut if the curve used to sweep goes from one face to another or from one edge to another; FALSE causes the swept cut to begin and end perpendicular to the sweep curve and it cannot break through the two end faces of the cut body |
| Input: | (short) twistCtrlOption | 0 = Follow path 1 = Keep constant normal 2 = Follow path and first guide curve 3 = Follow first and second guide curve |
| Input: | (BOOL) keepTangency | TRUE maintains the tangency as in the section curves, FALSE does not If the section curves are tangent, then you can specify whether the resulting faces are also tangent. When generating tangent faces, SolidWorks maintains planar and cylindrical face shapes if the section curves exhibit these characteristics. |
| Input: | (BOOL) forceNonRational | TRUE forces the resulting surface to be non-rational, FALSE does not |
| Input: | (short) startMatchingType | 0 = None 1 = Tangent to the normal of the profile 2 = Tangent to a selected vector 3 = Tangency to all the adjacent faces sharing an edge with the start profile 4 = Tangent to some of the selected faces sharing an edge with the start profile (not available) |
| Input: | (short) endMatchingType | 0 = None 1 = Tangent to the normal of the profile 2 = Tangent to a selected vector 3 = Tangency to all the adjacent faces sharing an edge with the start profile 4 = Tangent to some of the selected faces sharing an edge with the start profile (not available) |
| Input: | (BOOL) isThinBody | TRUE if this feature is a thin body, FALSE if it is not |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | Thin wall type: 0 = One direction 1 = One direction reverse 2 = Mid-plane 3 = Two direction |
| Input: | (BOOL) merge | TRUE to merge the results in the multibody part, FALSE to not |
| Input: | (VARIANT_BOOL) useFeatScope | TRUE if the feature only affects selected bodies, FALSE if the feature affects all bodies |
| Input: | VARIANT_BOOL) useAutoSelect | TRUE to automatically select all bodies and have the feature affect those bodies, FALSE to select the bodies the feature affects |
| Output: | (LPFEATURE) *retval | Pointer to the feature object |
| Return: | (HRESULT) status | S_OK is successful |

Remarks

Use ModelDocExtension::SelectByID to select the profile and sweep curves. Set the mark for:

- 1 = profile selection to 1
- 4 = sweep path
- 2 = guide curve selection, if provided

When useAutoSelect is FALSE, the user must select the bodies that the feature will affect.
