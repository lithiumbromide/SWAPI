---
title: "ModelDoc2::InsertCutBlend4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertCutBlend4.htm"
---

# ModelDoc2::InsertCutBlend4

This method is obsolete and has been superseded by [FeatureManager::InsertCutBlend](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertCutBlend.htm).

Description

This method inserts a lofted cut based on the selected profiles, centerline, and guide curves.

Syntax (OLE Automation)

void ModelDoc2.InsertCutBlend4 ( closed, keepTangency, forceNonRational, tessToleranceFactor, startMatchingType, endMatchingType, isThinBody, thickness1, thickness2, thinType )

| Input: | (BOOL) closed | TRUE for closed loft, FALSE for open loft |
| --- | --- | --- |
| Input: | (BOOL) keepTangency | Controls whether the section curves are tangent |
| Input: | (BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Input: | (double) tessToleranceFactor | Factor to control the number of intermediate sections used for loft with centerline; default value is 1.0; the greater the variable, the more intermediate sections created |
| Input: | (short) startMatchingType | Tangency type at the start profile |
| Input: | (short) endMatchingType | Tangency type at the end profile |
| Input: | (BOOL) isThinBody | TRUE if this feature is a thin body, FALSE otherwise |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | TRUE if this feature is a thin feature, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->InsertCutBlend4 ( closed, keepTangency, forceNonRational, tessToleranceFactor, startMatchingType, endMatchingType, isThinBody, thickness1, thickness2, thinType )

| Input: | (VARIANT_BOOL) closed | TRUE for closed loft, FALSE for open loft |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) keepTangency | Controls whether the section curves are tangent |
| Input: | (VARIANT_BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Input: | (double) tessToleranceFactor | Factor to control the number of intermediate sections used for loft with centerline.; default value is 1.0; the greater the variable, the more intermediate sections are created |
| Input: | (short) startMatchingType | Tangency type at the start profile |
| Input: | (short) endMatchingType | Tangency type at the end profile |
| Input: | (VARIANT_BOOL) isThinBody | TRUE if this feature is a thin body, FALSE otherwise |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | TRUE if this feature is a thin feature, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Selection of guide curves and centerline is optional; however, selection of the profiles must be in an order consistent with the desired direction of the loft. Because you are creating a surface, the section profiles can be open.

Use of guide curves is recommended, especially when selection of profiles is done in the FeatureManager design tree.

You can use any number of profiles; however, if you selected only one profile, then any selected guide curves must be closed curves.

If closed is TRUE and you have selected less that three profiles, then any selected guide curves must be closed curves.

If the section curves are tangent, then keepTangency controls whether the resulting surfaces arel also be tangent. Specify TRUE to maintain the tangency as seen in the section curves. When generating tangent surfaces, planar and cylindrical surface shapes are maintained if the section curves exhibit these characteristics.

UseModelDocExtenstion::SelectByID to select the profiles and guide curves. The mark for:

- profile selections should be a 1
- any guide curve selection, if provided, should be a 2
- centerline selection, if provided, should be a 4
- start tangency vector selection, if provided, should be a 8
- start tangency faces selection, if provided, should be a 16 (not currently available)
- end tangency vector selection, if provided, should be a 32
- end tangency faces selection, if provided, should be a 64 (not currently available)

Linear edge, sketch line, axis, plane ,and planar faces are qualified for tangency vector sections.

The tangency type arguments can be:

- 0 - none
- 1 - tangent to the normal of the profile
- 2 - tangent to a selected vector
- 3 - tangent to all the adjacent faces sharing an edge with the start profile
- 4 - tangent to some of the selected faces sharing an edge with the start profile (not currently available)
