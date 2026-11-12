---
title: "ModelDoc::FeatureFillet4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureFillet4.htm"
---

# ModelDoc::FeatureFillet4

This method is obsolete and has been superseded by [ModelDoc2::FeatureFillet4](../ModelDoc2/ModelDoc2__FeatureFillet4.htm).

Description

This method creates an edge fillet feature.

Syntax (OLE Automation)

retval = ModelDoc.FeatureFillet4 ( r1, propagate, uniformRadius, ftype, varRadTyp, overFlowType, nRadii, radii, useHelpPoint, useTangentHoldLine, cornerType, setbackDistCount, setBackDistances )

| Input: | (double) r1 | Fillet radius |
| --- | --- | --- |
| Input: | (BOOL) propagate | TRUE uses tangent propagation, FALSE does not |
| Input: | (BOOL) uniformRadius | TRUE uses a uniform radius, FALSE does not |
| Input: | (int) ftype | 0 for simple, 1 for variable radius, 2 for surface blend |
| Input: | (BOOL) varRadTyp | 0 for linear, 1 for smooth transition (variable radius) |
| Input: | (long) overFlowType | Control of fillet overflowing onto adjacent surfaces |
| Input: | (int) nRadii | Number of radii for a multiple-radius fillet |
| Input: | (VARIANT) radii | Array if radii for multiple-radius fillet of size nRadii |
| Input: | (BOOL) useHelpPoint | TRUE uses help points, FALSE does not |
| Input: | (BOOL) useTangentHoldLine | TRUE uses a tangent hold line, FALSE does not |
| Input: | (BOOL) cornerType | TRUE uses round corners, FALSE does not |
| Input: | (int) setbackDistCount | Number of setback distances when the fillet of type setback |
| Input: | (VARIANT) setBackDistances | Array of size setbackDistCount |
| Return: | (long) retval | Fillet ID |

Syntax (COM)

status = ModelDoc->IFeatureFillet4 ( r1, propagate, uniformRadius, ftype, varRadTyp, overFlowType, nRadii, radii, useHelpPoint, useTangentHoldLine, cornerType, setbackDistCount, setBackDistances, &retval )

| Input: | (double) r1 | Fillet radius |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) propagate | TRUE uses tangent propagation, FALSE does not |
| Input: | (VARIANT_BOOL) uniformRadius | TRUE uses a uniform radius, FALSE does not |
| Input: | (int) ftype | 0 for simple, 1 for variable radius, 2 for surface blend |
| Input: | (VARIANT_BOOL) varRadTyp | 0 for linear, 1 for smooth transition (variable radius) |
| Input: | (long) overFlowType | Control of fillet overflowing onto adjacent surfaces |
| Input: | (int) nRadii | Number of radii for a multiple-radius fillet |
| Input: | (double*) radii | Array if radii for multiple-radius fillet of size nRadii |
| Input: | (VARIANT_BOOL) useHelpPoint | TRUE uses help points, FALSE does not |
| Input: | (VARIANT_BOOL) useTangentHoldLine | TRUE uses a tangent hold line, FALSE does not |
| Input: | (VARIANT_BOOL) cornerType | TRUE uses round corners, FALSE does not |
| Input: | (int) setbackDistCount | Number of setback distances when the fillet of type setback |
| Input: | (double*) setBackDistances | Array of size setbackDistCount |
| Output: | (long) retval | Fillet ID |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

The overFlowType controls how the fillet behaves when it meets adjacent surfaces:

- 0 - Default - the system will pick the appropriate method to create a fillet when the fillet surface overflows to adjacent surfaces. It will either smoothly blend with adjacent surfaces or limit the fillet surface with the adjacent edges (thus not changing the edge) or trim the fillet surface by the adjacent surface the fillet overflow onto. The method which is actually used by default will depend on the geometric condition. This option will always try to create a fillet if possible.
- 1 - Keep Edge - the edges that are overflowed by the fillet will not be modified. The fillet surface will be trimmed by all the adjacent edges. As a result, an additional transition fillet surface might be needed to complete the fillet.
- 2 - Keep Surface - the fillet surface will either be merged with the adjacent surfaces smoothly or trimmed by the adjacent surfaces. As a result, it is unlikely that an additional transition fillet surface will be created.

For face blend fillets, mark the first faces to select with the value 2, and then mark the second set of faces to select with a value of 4.
