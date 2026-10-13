---
title: "ModelDoc::InsertProtrusionSwept2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertProtrusionSwept2.htm"
---

# ModelDoc::InsertProtrusionSwept2

This method is obsolete and has been superseded by [ModelDoc2::InsertProtrusionSwept2](../ModelDoc2/ModelDoc2__InsertProtrusionSwept2.htm).

Description

This method inserts a swept boss or base feature from the selected profile and the selected sweep curves.

Syntax (OLE Automation)

void ModelDoc.InsertProtrusionSwept2 ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational)

| Input: | (BOOL) propagate | If TRUE, then the loft will propagate to the next tangent edge, FALSE and it will not propagate |
| --- | --- | --- |
| Input: | (BOOL) alignment | If the curve used to sweep goes from one face to another, or from one edge to another, passing TRUE will cause the sweep to cut completely through the end faces of the cut; if you choose FALSE, then the swept cut will begin and end perpendicular to the sweep curve and, therefore, may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | One of the following twist control options: 0 = Follow path 1 = Keep constant normal 2 = Follow path and first guide curve 3 = Follow first and second guide curve |
| Input: | (BOOL) keepTangency | Follow path |
| Input: | (BOOL) forceNonRational | Keep constant normal |

Syntax (COM)

status = ModelDoc->InsertProtrusionSwept2 ( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the loft will propagate to the next tangent edge, FALSE and it will not propagate |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from one face to another, or from one edge to another, passing TRUE will cause the sweep to cut completely through the end faces of the cut; if you choose FALSE, then the swept cut will begin and end perpendicular to the sweep curve and, therefore, may not break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | One of the following twist control options: 0 = Follow path 1 = Keep constant normal 2 = Follow path and first guide curve 3 = Follow first and second guide curve |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

use SelectByMark to select the profile and sweep curves. The mark for the profile selection should be a 1; the mark for the sweep path should be 4. If guide curve selection is provided, then SelectByMark mark should be 2.
