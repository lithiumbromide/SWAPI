---
title: "ModelDoc2::FeatureFillet4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureFillet4.htm"
---

# ModelDoc2::FeatureFillet4

This method is obsolete and has been superseded by [ModelDoc2::FeatureFillet5](ModelDoc2__FeatureFillet5.htm).

Description

This method creates an edge fillet feature.

Syntax (OLE Automation)

retval = ModelDoc2.FeatureFillet4 ( r1, propagate, uniformRadius, ftype, varRadTyp, overFlowType, nRadii, radii, useHelpPoint, useTangentHoldLine, cornerType, setbackDistCount, setBackDistances )

| Input: | (double) r1 | Fillet radius |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) propagate | TRUE to propagate the blend, FALSE to not |
| Input: | (VARIANT_BOOL) uniformRadius | TRUE for uniform radius, FALSE for not |
| Input: | (int) ftype | 0 - simple fillet 1 - variable radius fillet 2 - surface blend |
| Input: | (VARIANT_BOOL) varRadTyp | 0 - linear 1 - smooth transition ( variable radius) |
| Input: | (long) overFlowType | Control of fillet overflowing onto adjacent surfaces |
| Input: | (int) nRadii | Number of radii for variable radius fillets |
| Input: | (VARIANT) radii | SafeArray containing the radii for variable radius fillets |
| Input: | (VARIANT_BOOL) useHelpPoint | TRUE to use help points, FALSE to not |
| Input: | (VARIANT_BOOL) useTangentHoldLine | TRUE to use tangent hold line, FALSE to not |
| Input: | (VARIANT_BOOL) cornerType | TRUE to use round corners, FALSE to not |
| Input: | (int) setbackDistCount | Number of setback distances when fillet of type setback |
| Input: | (VARIANT) setBackDistances | SafeArray containing setback distances for the fillet along the edge |
| Return: | (long) retval | 1 if the fillet is created, 0 if it is not |

Syntax (COM)

status = ModelDoc2->IFeatureFillet4 ( r1, propagate, uniformRadius, ftype, varRadTyp, overFlowType, nRadii, radii, useHelpPoint, useTangentHoldLine, cornerType, setbackDistCount, setBackDistances, &retval )

| Input: | (double) r1 | Fillet radius |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) propagate | TRUE to propagate the blend, FALSE to not |
| Input: | (VARIANT_BOOL) uniformRadius | TRUE for uniform radius, FALSE for not |
| Input: | (int) ftype | 0 - simple fillet 1 - variable radius fillet 2 - surface blend |
| Input: | (VARIANT_BOOL) varRadTyp | 0 - linear 1 - smooth transition ( variable radius) |
| Input: | (long) overFlowType | Control of fillet overflowing onto adjacent surfaces |
| Input: | (int) nRadii | Number of radii for variable radius fillets |
| Input: | (double*) radii | Array containing the radii for variable radius fillets |
| Input: | (VARIANT_BOOL) useHelpPoint | TRUE to use help points, FALSE to not |
| Input: | (VARIANT_BOOL) useTangentHoldLine | TRUE to use tangent hold line, FALSE to not |
| Input: | (VARIANT_BOOL) cornerType | TRUE to use round corners, FALSE to not |
| Input: | (int) setbackDistCount | Number of setback distances when fillet of type setback |
| Input: | (double*) setBackDistances | Array containing setback distances for the fillet along the edge |
| Output: | (long) retval | 1 if the fillet is created, 0 if it is not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The overFlowType argument controls how the fillet behaves when it meets adjacent surfaces:

- 0 - Default - The system picks the appropriate method to create a fillet when the fillet surface overflows to adjacent surfaces. It either smoothly blends with adjacent surfaces or limits the fillet surface with the adjacent edges
  (thus, not changing the edge) or trims the fillet surface by the adjacent surface onto which the fillet overflows. The method that is used by default depends on the geometric condition. This option always tries to create a fillet, if possible.
- 1 - Keep Edge - The edges that are overflowed by the fillet are not modified. The fillet surface is trimmed by all the adjacent edges. As a result, an additional transition fillet surface might be needed to complete the fillet.
- 2 - Keep Surface - The fillet surface is either merged with the adjacent surfaces smoothly or trimmed by the adjacent surfaces. As a result, it is unlikely that an additional transition fillet surface will be created.

For face blend fillets, select the first set of faces with mark 2 and the second set of faces with mark 4.
