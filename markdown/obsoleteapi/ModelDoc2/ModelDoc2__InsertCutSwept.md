---
title: "ModelDoc2::InsertCutSwept"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertCutSwept.htm"
---

# ModelDoc2::InsertCutSwept

This method is obsolete and has been superseded by [ModelDoc2::InsertCutSwept2](ModelDoc2__InsertCutSwept2.htm).

Description

This method inserts a swept cut from the selected profile and the selected sweep curves.

Syntax (OLE Automation)

ModelDoc2.InsertCutSwept ( propagate, alignment, keepNormalConstant )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the swept cut is propagated to the next edge, FALSE causes the swept cut to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from one face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, if you choose FALSE, then the swept cut begins and ends perpendicular to the sweep curve; therefore, it may not break through the two end faces of the body being cut |
| Input: | (VARIANT_BOOL) keepNormalConstant | TRUE keeps the constant normal, FALSE does not |

Syntax (COM)

status = ModelDoc2->InsertCutSwept ( propagate, alignment, keepNormalConstant )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the swept cut is propagated to the next edge, FALSE causes the swept cut to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from one face to another, or from one edge to another, passing TRUE causes the sweep to cut completely through the end faces of the cut, if you choose FALSE, then the swept cut begins and ends perpendicular to the sweep curve; therefore, it may not break through the two end faces of the body being cut |
| Input: | (VARIANT_BOOL) keepNormalConstant | TRUE keeps the constant normal, FALSE does not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
