---
title: "ModelDoc2::InsertCutSwept3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertCutSwept3.htm"
---

# ModelDoc2::InsertCutSwept3

This method is obsolete and has been superseded by [ModelDoc2:InsertCutSwept4](ModelDoc2__InsertCutSwept4.htm).

Description

This method inserts a swept cut from the selected profile and the selected sweep curves.

Syntax (OLE Automation)

(void) ModelDoc2.InsertCutSwept3 ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType )

| Input: | (Boolean) propagate | TRUE propagates the swept cut to the next edge, FALSE causes the swept cut to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (Boolean) alignment | If the curve used to sweep goes from on face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and end perpendicular to the sweep curve; therefore, it may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (Boolean) keepTangency | Follow path |
| Input: | (Boolean) forceNonRational | Keep constant normal |
| Input: | (short) startMatchingType | Tangency type |
| Input: | (short) endMatchingType | Tangency type |

Syntax (COM)

status = ModelDoc2->InsertCutSwept3 ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType )

| Input: | (VARIANT_BOOL) propagate | TRUE propagates the swept cut to the next edge, FALSE causes the swept cut to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from on face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and end perpendicular to the sweep curve; therefore, it may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options, see below. |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Input: | (short) startMatchingType | Tangency type |
| Input: | (short) endMatchingType | Tangency type |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDocExtension::SelectByID to select the profile and sweep curves. The mark for:

- Profile selection should be a 1
- Sweep path should be 4
- Guide-curve selection should be 2

The twistCtrlOption argument can take one of these values:

- 0 = Follow path
- 1 = Keep constant normal
- 2 = Follow path and first guide curve
- 3 = Follow first and second guide curve

The Tangency type arguments can take one of these values:

- 0 - none
- 1 - tangent to the normal of the profile
- 2 - tangent to a selected vector
- 3 - tangency to all the adjacent faces sharing an edge with the start profile
- 4 - tangent to some of the selected faces sharing an edge with the start profile (not currently available)
