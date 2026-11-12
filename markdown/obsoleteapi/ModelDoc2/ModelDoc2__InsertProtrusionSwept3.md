---
title: "ModelDoc2::InsertProtrusionSwept3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertProtrusionSwept3.htm"
---

# ModelDoc2::InsertProtrusionSwept3

This method is obsolete and has been superseded by [ModelDoc2::InsertProtrusionSwept4](ModelDoc2__InsertProtrusionSwept4.htm).

Description

This method inserts a swept boss or base feature from the selected profile and the selected sweep curves.

Syntax (OLE Automation)

(void) ModelDoc2.InsertProtrusionSwept3 ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType )

| Input: | (Boolean) propagate | If TRUE, then the loft propagates to the next tangent edge, FALSE and it does not propagate |
| --- | --- | --- |
| Input: | (Boolean) alignment | If the curve used to sweep goes from one face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and end perpendicular to the sweep curve and may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (Boolean) keepTangency | If the section curves are tangent, then you have the option to specify whether the resulting faces are also tangent; specify TRUE to maintain the tangency as seen in the section curves, FALSE otherwise; when generating tangent faces, planar and cylindrical face shapes are maintained if the section curves exhibit these characteristics |
| Input: | (Boolean) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Input: | (short) startMatchingType | Tangency type |
| Input: | (short) endMatchingType | Tangency type |

Syntax (COM)

status = ModelDoc2->InsertProtrusionSwept3 ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the loft propagates to the next tangent edge, FALSE and it does not propagate |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from one face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and end perpendicular to the sweep curve and may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (VARIANT_BOOL) keepTangency | If the section curves are tangent, then you have the option to specify whether the resulting faces are also tangent; specify TRUE to maintain the tangency as seen in the section curves, FALSE otherwise; when generating tangent faces, planar and cylindrical face shapes are maintained if the section curves exhibit these characteristics |
| Input: | (VARIANT_BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Input: | (short) startMatchingType | Tangency type |
| Input: | (short) endMatchingType | Tangency type |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDocExtension::SelectByID to select the profile and sweep curves. The mark for:

1 = profile selection

4 = sweep path

2 = guide curve selection, if provided,

The twistCtrlOption argument can be one of these values:

0 = follow path

1 = keep constant normal

2 = follow path and first guide curve

3 = follow first and second guide curve

The Tangency type arguments can be one of these values:

0 - none

1 - tangent to the normal of the profile

2 - tangent to a selected vector

3 - tangency to all the adjacent faces sharing an edge with the start profile

4 - tangent to some of the selected faces sharing an edge with the start profile (not available)
