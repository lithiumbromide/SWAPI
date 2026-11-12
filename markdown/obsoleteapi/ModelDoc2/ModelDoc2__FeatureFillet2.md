---
title: "ModelDoc2::FeatureFillet2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureFillet2.htm"
---

# ModelDoc2::FeatureFillet2

This method is obsolete and has been superseded by [ModelDoc2::FeatureFillet3](ModelDoc2__FeatureFillet3.htm).

Description

This method creates a fillet feature.

Syntax (OLE Automation)

retval = ModelDoc2.FeatureFillet2 ( r1, propagate, ftyp, varRadTyp, overFlowType, nRadii, radii)

| Input: | (double) r1 | Radius for end1 |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) propagate | TRUE to propagate the blend, FALSE to not |
| Input: | (VARIANT_BOOL) ftyp | 0 - simple fillet 1 - variable radius fillet |
| Input: | (VARIANT_BOOL) varRadTyp | 0 - linear 1 - smooth transition (variable radius) |
| Input: | (long) overFlowType | Control of fillet overflowing onto adjacent surfaces |
| Input: | (int) nRadii | Number of radii for variable radius fillets |
| Input: | (VARIANT) radii | SafeArray containing the radii for variable radius fillets |
| Return: | (long) retval | 1 if the fillet was created, 0 if not |

Syntax (COM)

status = ModelDoc2->IFeatureFillet2( r1, propagate, ftyp, varRadTyp, overFlowType, nRadii, radii, &retval )

| Input: | (double) r1 | Radius for end1 |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) propagate | TRUE to propagate the blend, FALSE otherwise |
| Input: | (VARIANT_BOOL) ftyp | 0 - simple fillet 1 - variable radius fillet |
| Input: | (VARIANT_BOOL) varRadTyp | 0 - linear 1 - smooth transition (variable radius) |
| Input: | (long) overFlowType | Control of fillet overflowing onto adjacent surfaces |
| Input: | (int) nRadii | Number of radii for variable radius fillets |
| Input: | (double*) radii | Array containing the radii for variable radius fillets |
| Output: | (long) retval | 1 if the fillet was created, 0 if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For variable radius fillets, the r1 argument is ignored as the radii array contains values for all the radii.

The overFlowType argument controls how the fillet behaves when it meets adjacent surfaces:

- 0 - Default - The system picks the appropriate method to create a fillet when the fillet surface overflows to adjacent surfaces. It either smoothly blends with adjacent surfaces or limits the fillet surface with the adjacent edges
  (thus, not changing the edge) or trims the fillet surface by the adjacent surface onto which the fillet overflows. The method that is used by default depends on the geometric condition. This option always tries to create a fillet, if possible.
- 1 - Keep Edge - The edges that are overflowed by the fillet are not modified. The fillet surface is trimmed by all the adjacent edges. As a result, an additional transition fillet surface might be needed to complete the fillet.
- 2 - Keep Surface - The fillet surface is either merged with the adjacent surfaces smoothly or trimmed by the adjacent surfaces. As a result, it is unlikely that an additional transition fillet surface will be created.
