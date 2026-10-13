---
title: "ModelDoc2::InsertProtrusionSwept"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertProtrusionSwept.htm"
---

# ModelDoc2::InsertProtrusionSwept

This method is obsolete and has been superseded by [ModelDoc2::InsertProtrusionSwept2](ModelDoc2__InsertProtrusionSwept2.htm).

Description

This method inserts a swept boss or base feature from the selected profile and the selected sweep curves.

Syntax (OLE Automation)

ModelDoc2.InsertProtrusionSwept ( propagate, alignment, keepNormalConstant )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the swept cut propagated to the next edge, FALSE causes the swept cut to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from one face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and end perpendicular to the sweep curve and may not break through the two end faces of the body being cut |
| Input: | (VARIANT_BOOL) keepNormalConstant | TRUE keeps the constant normal, FALSE does not |

Syntax (COM)

status = ModelDoc2->InsertProtrusionSwept ( propagate, alignment, keepNormalConstant )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the swept cut propagated to the next edge, FALSE causes the swept cut to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from one face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, FALSE causes the swept cut to begin and end perpendicular to the sweep curve and may not break through the two end faces of the body being cut |
| Input: | (VARIANT_BOOL) keepNormalConstant | TRUE keeps the constant normal, FALSE does not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDocExtension::SelectByID select the profile and sweep curves. The mark for:

- profile selection should be a 1
- sweep path should be 4
- guide curve selection, if provided, should be 2
