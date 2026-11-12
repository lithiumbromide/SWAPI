---
title: "ModelDoc::InsertRib"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertRib.htm"
---

# ModelDoc::InsertRib

This method is obsolete and has been superseded by [ModelDoc::InsertRib2](ModelDoc__InsertRib2.htm).

Description

This method inserts a rib.

Syntax (OLE Automation)

void ModelDoc.InsertRib ( is2Sided, reverseThicknessDir, thickness, referenceEdgeIndex, reverseMaterialDir, isDrafted, draftOutward, draftAngle)

| Input: | (BOOL) is2Sided | TRUE if the rib will be a double-sided rib or FALSE if the rib is single-sided; a double-sided rib will thicken on both sides of the sketch |
| --- | --- | --- |
| Input: | (BOOL) reverseThicknessDir | For single side ribs, this will thicken on the opposite side of the sketch normal |
| Input: | (double) thickness | Rib thickness |
| Input: | (long) referenceEdgeIndex | Edge in the sketch to use to determine the material direction and for draft reference; when the rib is drafted, the midpoint of this edge will maintain the thickness value, other points on the rib may have a different thickness due to the draft |
| Input: | (BOOL) reverseMaterialDir | Direction the rib has material; it will be on one side or the order side of the reference edge base on this flag |
| Input: | (BOOL) isDrafted | TRUE if the rib will be drafted, FALSE otherwise |
| Input: | (BOOL) draftOutward | TRUE to draft outwards, FALSE inwards |
| Input: | (double) draftAngle | Draft angle applied to the rib |

Syntax (COM)

status = ModelDoc->InsertRib ( is2Sided, reverseThicknessDir, thickness, referenceEdgeIndex, reverseMaterialDir, isDrafted, draftOutward, draftAngle )

| Input: | (VARIANT_BOOL) is2Sided | TRUE if the rib will be a double-sided rib or FALSE if the rib is single-sided; a double-sided rib will thicken on both sides of the sketch |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseThicknessDir | For single side ribs, this will thicken on the opposite side of the sketch normal |
| Input: | (double) thickness | Rib thickness |
| Input: | (long) referenceEdgeIndex | Edge in the sketch will be used to determine the material direction and for draft reference; when the rib is drafted, the midpoint of this edge will maintain the thickness value other points on the rib may have a different thickness due to the draft |
| Input: | (VARIANT_BOOL) reverseMaterialDir | Direction the rib has material; it will be on one side or the order side of the reference edge base on this flag |
| Input: | (VARIANT_BOOL) isDrafted | TRUE if the rib will be drafted, FALSE otherwise |
| Input: | (VARIANT_BOOL) draftOutward | TRUE to draft outwards, FALSE inwards |
| Input: | (double) draftAngle | Draft angle applied to the rib |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
