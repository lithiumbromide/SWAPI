---
title: "ModelDoc2::InsertProtrusionSwept4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertProtrusionSwept4.htm"
---

# ModelDoc2::InsertProtrusionSwept4

This method is obsolete and has been superseded by [FeatureManager::InsertProtrusionSwept](../FeatureManager/FeatureManager__InsertProtrusionSwept.htm).

Description

This method inserts a swept boss or base feature from the selected profile and the selected sweep curves.

Syntax (OLE Automation)

void ModelDoc2.InsertProtrusionSwept4 ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType, isThinBody, thickness1, thickness2, thinType)

| Input: | (BOOL) propagate | If TRUE, then the loft propagates to the next tangent edge, FALSE and it does not propagate |
| --- | --- | --- |
| Input: | (BOOL) alignment | If the curve used to sweep goes from one face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and end perpendicular to the sweep curve and may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (BOOL) keepTangency | If the section curves are tangent, then you have the option to specify whether the resulting faces are also tangent; specify TRUE to maintain the tangency as seen in the section curves, FALSE otherwise; when generating tangent faces, planar and cylindrical face shapes are maintained if the section curves exhibit these characteristics |
| Input: | (BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Input: | (short) startMatchingType | Tangency type |
| Input: | (short) endMatchingType | Tangency type |
| Input: | (BOOL) isThinBody | TRUE if this feature is a thin body, FALSE otherwise |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | TRUE if this feature is a thin feature, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->InsertProtrusionSwept4 ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType, isThinBody, thickness1, thickness2, thinType )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the loft propagates to the next tangent edge, FALSE and it does not propagate |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from one face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and end perpendicular to the sweep curve and may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (VARIANT_BOOL) keepTangency | If the section curves are tangent, then you have the option to specify whether the resulting faces are also tangent; specify TRUE to maintain the tangency as seen in the section curves, FALSE otherwise; when generating tangent faces, planar and cylindrical face shapes are maintained if the section curves exhibit these characteristics |
| Input: | (VARIANT_BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Input: | (short) startMatchingType | Tangency type |
| Input: | (short) endMatchingType | Tangency type |
| Input: | (VARIANT_BOOL) isThinBody | TRUE if this feature is a thin body, FALSE otherwise |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | TRUE if this feature is a thin feature, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDocExtension::SelectByID to select the profile and sweep curves. The mark for:

The twistCtrlOption argument may be one of these values:

- 0 = Follow path
- 1 = Keep constant normal
- 2 = Follow path and first guide curve
- 3 = Follow first and second guide curve

The Tangency type arguments can be one of these values:

- 0 - none
- 1 - tangent to the normal of the profile
- 2 - tangent to a selected vector
- 3 - tangency to all the adjacent faces sharing an edge with the start profile
- 4 - tangent to some of the selected faces sharing an edge with the start profile (not available)
