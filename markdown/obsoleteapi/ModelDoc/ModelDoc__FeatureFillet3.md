---
title: "ModelDoc::FeatureFillet3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureFillet3.htm"
---

# ModelDoc::FeatureFillet3

This method is obsolete and has been superseded by [ModelDoc::FeatureFillet4](ModelDoc__FeatureFillet4.htm).

Description

This method creates a fillet feature.

Syntax (OLE Automation)

retval = ModelDoc.FeatureFillet3 ( r1, propagate, ftyp, varRadTyp, overFlowType, radii, useHelpPoint, useTangentHoldLine )

| Input: | (double) r1 | Radius for end1 |
| --- | --- | --- |
| Input: | (BOOL) propagate | TRUE to propagate the blend, FALSE otherwise |
| Input: | (int) ftyp | 0 for simple fillet, 1 for variable radius fillete, 2 for surface blend fillet |
| Input: | (BOOL) varRadTyp | 0 for linear, 1 for smooth transition (variable radius) |
| Input: | (long) overFlowType | Control of fillet overflowing onto adjacent surfaces |
| Input: | (VARIANT) radii | SafeArray containing the radii for variable radius fillets |
| Input: | (BOOL) useHelpPoint | Use help points |
| Input: | (BOOL) useTangentHoldLine | Use tangent hold line |
| Return: | (long) retval | 1 if the fillet was created, otherwise 0 |

Syntax (COM)

status = ModelDoc->IFeatureFillet3 ( r1, propagate, ftyp, varRadTyp, overFlowType, nRadii, radii, useHelpPoint, useTangentHoldLine, &retval )

| Input: | (double) r1 | Radius for end1 |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) propagate | TRUE to propagate the blend, FALSE otherwise |
| Input: | (int) ftyp | 0 for simple fillet, 1 for variable radius fillet, 2 for surface blend fillet |
| Input: | (VARIANT_BOOL) varRadTyp | 0 for linear, 1 for smooth transition (variable radius) |
| Input: | (long) overFlowType | Control of fillet overflowing onto adjacent surfaces, |
| Input: | (int) nRadii | Number of radii for variable radius fillets |
| Input: | (double*) radii | Array containing the radii for variable radius fillets |
| Input: | (VARIANT_BOOL) useHelpPoint | Use help points |
| Input: | (VARIANT_BOOL) useTangentHoldLine | Use tangent hold line |
| Output: | (long) retval | 1 if the fillet was created, otherwise 0 |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The overFlowType argument controls how the fillet behaves when it meats adjacent surfaces:

- 0 - Default: The system picks the appropriate method to create a fillet when the fillet surface overflows to adjacent surfaces. It either smoothly blends with adjacent surfaces or limits the fillet surface with the adjacent edges, thus, not changing the edge, or trims the fillet surface by the adjacent surface on to which the fillet overflows. The method is used by default and depends on the geometric condition. This option always tries to create a fillet if possible.
- 1 - Keep Edge: The edges that are overflowed by the fillet are not modified. The fillet surface is trimmed by all the adjacent edges. As a result, an additional transition fillet surface might be needed to complete the fillet.
- 2 - Keep Surface: The fillet surface either merges with the adjacent surfaces smoothly or is trimmed by the adjacent surfaces. As a result, it is unlikely that an additional transition fillet surface is created.

For face blend fillets, mark the first faces to select with the value 2, and then mark the second set of faces to select with a value of 4.
