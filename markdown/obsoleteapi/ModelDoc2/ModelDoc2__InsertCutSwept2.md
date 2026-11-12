---
title: "ModelDoc2::InsertCutSwept2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertCutSwept2.htm"
---

# ModelDoc2::InsertCutSwept2

This method is obsolete and has been superseded by [ModelDoc2:InsertCutSwept3](ModelDoc2__InsertCutSwept3.htm).

Description

This method inserts a swept cut from the selected profile and the selected sweep curves.

Syntax (OLE Automation)

void ModelDoc2.InsertCutSwept2 ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational)

| Input: | (BOOL) propagate | TRUE propagates the swept cut will propagate to the next edge, FALSE causes the swept cut to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (BOOL) alignment | If the curve used to sweep goes from on face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and end perpendicular to the sweep curve; therefore, it may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | 0 = Follow path 1 = Keep constant normal 2 = Follow path and first guide curve 3 = Follow first and second guide curve |
| Input: | (BOOL) keepTangency | Follow path |
| Input: | (BOOL) forceNonRational | Keep constant normal |

Syntax (COM)

status = ModelDoc2->InsertCutSwept2 ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational )

| Input: | (VARIANT_BOOL) propagate | TRUE propagates the swept cut will propagate to the next edge, FALSE causes the swept cut to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from on face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and end perpendicular to the sweep curve; therefore, it may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | 0 = Follow path 1 = Keep constant normal 2 = Follow path and first guide curve 3 = Follow first and second guide curve |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDocExtension::SelectByID to select the profile and sweep curves. The mark for the profile selection should be a 1 while the mark for the sweep path should be 4. If guide curve selection is provided, mark should be 2.
