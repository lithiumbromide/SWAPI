---
title: "ModelDoc2::InsertProtrusionSwept2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertProtrusionSwept2.htm"
---

# ModelDoc2::InsertProtrusionSwept2

This method is obsolete and has been superseded by [ModelDoc2::InsertProtrusionSwept3](ModelDoc2__InsertProtrusionSwept3.htm).

Description

This method inserts a swept boss or base feature from the selected profile and the selected sweep curves.

Syntax (OLE Automation)

void ModelDoc2.InsertProtrusionSwept2 ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational)

| Input: | (BOOL) propagate | If TRUE, then the loft propagates to the next tangent edge, FALSE and it does not propagate. |
| --- | --- | --- |
| Input: | (BOOL) alignment | If the curve used to sweep goes from one face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and end perpendicular to the sweep curve and may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options: 0 = Follow path 1 = Keep constant normal 2 = Follow path and first guide curve 3 = Follow first and second guide curve |
| Input: | (BOOL) keepTangency | Follow path |
| Input: | (BOOL) forceNonRational | Keep constant normal |

Syntax (COM)

status = ModelDoc2->InsertProtrusionSwept2 ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the loft propagates to the next tangent edge, FALSE and it does not propagate. |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from one face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and end perpendicular to the sweep curve and may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options: 0 = Follow path 1 = Keep constant normal 2 = Follow path and first guide curve 3 = Follow first and second guide curve |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use ModelDocExtension::SelectById to select the profile and sweep curves. The mark fo:

- profile selection should be a 1
- sweep path should be 4
- guide curve selection, if provided, should be 2
