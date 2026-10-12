---
title: "ModelDoc2::InsertRib"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertRib.htm"
---

# ModelDoc2::InsertRib

This method is obsolete and has been superseded by [ModelDoc2::InsertRib2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertRib2.htm).

Description

This method inserts a rib.

Syntax (OLE Automation)

void ModelDoc2.InsertRib ( is2Sided, reverseThicknessDir, thickness, referenceEdgeIndex, reverseMaterialDir, isDrafted, draftOutward, draftAngle)

| Input: | (BOOL) is2Sided | TRUE if the rib is double-sided, FALSE if single-sided; a double-sided rib thickens on both sides of the sketch |
| --- | --- | --- |
| Input: | (BOOL) reverseThicknessDir | Thicken on the opposite side of the sketch normal for single-sided ribs |
| Input: | (double) thickness | Rib thickness |
| Input: | (long) referenceEdgeIndex | Edge in the sketch to us to determine the material direction and for draft reference; when the rib is drafted, the mid point of this edge maintains the thickness value; other points on the rib may have a different thickness due to the draft |
| Input: | (BOOL) reverseMaterialDir | Direction the rib has material; it can be on one side or the order side of the reference edge base on this flag |
| Input: | (BOOL) isDrafted | TRUE if the rib will be drafted, FALSE otherwise |
| Input: | (BOOL) draftOutward | TRUE to draft outwards, FALSE inwards |
| Input: | (double) draftAngle | Draft angle applied to the rib |

Syntax (COM)

status = ModelDoc2->InsertRib ( is2Sided, reverseThicknessDir, thickness, referenceEdgeIndex, reverseMaterialDir, isDrafted, draftOutward, draftAngle )

| Input: | (VARIANT_BOOL) is2Sided | TRUE if the rib is double-sided, FALSE if single-sided; a double-sided rib thickens on both sides of the sketch |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseThicknessDir | Thicken on the opposite side of the sketch normal for single-sided ribs |
| Input: | (double) thickness | Rib thickness |
| Input: | (long) referenceEdgeIndex | Edge in the sketch to us to determine the material direction and for draft reference; when the rib is drafted, the mid point of this edge maintains the thickness value; other points on the rib may have a different thickness due to the draft |
| Input: | (VARIANT_BOOL) reverseMaterialDir | Direction the rib has material; it can be on one side or the order side of the reference edge base on this flag |
| Input: | (VARIANT_BOOL) isDrafted | TRUE if the rib will be drafted, FALSE otherwise |
| Input: | (VARIANT_BOOL) draftOutward | TRUE to draft outwards, FALSE inwards |
| Input: | (double) draftAngle | Draft angle applied to the rib |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
