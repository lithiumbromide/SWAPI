---
title: "ModelDoc::FeatureFillet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureFillet.htm"
---

# ModelDoc::FeatureFillet

This method is obsolete and has been superseded by [ModelDoc::FeatureFillet2](ModelDoc__FeatureFillet2.htm).

Description

This method creates a fillet feature.

Syntax (OLE Automation)

void ModelDoc.FeatureFillet ( r1, propagate, ftyp, varRadTyp, overFlowType)

| Input: | (double) r1 | Radius for end1 |
| --- | --- | --- |
| Input: | (BOOL) propagate | TRUE to propagate the blend, FALSE otherwise |
| Input: | (BOOL) ftyp | 0 for simple fillet, 1 for variable radius fillet |
| Input: | (BOOL) varRadTyp | 0 for linear, 1 for smooth transition (variable radius) |
| Input: | (long) overFlowType | Control of fillet overflowing onto adjacent surfaces |

Syntax (COM)

status = ModelDoc->FeatureFillet ( r1, propagate, ftyp, varRadTyp, overFlowType )

| Input: | (double) r1 | Radius for end1 |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) propagate | TRUE to propagate the blend, FALSE otherwise |
| Input: | (VARIANT_BOOL) ftyp | 0 for simple fillet, 1 for variable radius fillet |
| Input: | (VARIANT_BOOL) varRadTyp | 0 for linear, 1 for smooth transition (variable radius) |
| Input: | (long) overFlowType | Control of fillet overflowing onto adjacent surfaces |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The overFlowType argument controls how the fillet behaves when it meats adjacent surfaces:

- 0 - Default: The system picks the appropriate method to create a fillet when the fillet surface overflows to adjacent surfaces. It either smoothly blends with adjacent surfaces or limits the fillet surface with the adjacent edges, thus, not changing the edge, or trims the fillet surface by the adjacent surface on to which the fillet overflows. The method is used by default and depends on the geometric condition. This option always tries to create a fillet if possible.
- 1 - Keep Edge: The edges that are overflowed by the fillet are not modified. The fillet surface is trimmed by all the adjacent edges. As a result, an additional transition fillet surface might be needed to complete the fillet.
- 2 - Keep Surface: The fillet surface either merges with the adjacent surfaces smoothly or is trimmed by the adjacent surfaces. As a result, it is unlikely that an additional transition fillet surface is created.
