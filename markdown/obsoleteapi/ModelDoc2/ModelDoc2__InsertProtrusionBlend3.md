---
title: "ModelDoc2::InsertProtrusionBlend3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertProtrusionBlend3.htm"
---

# ModelDoc2::InsertProtrusionBlend3

This method is obsolete and has been superseded by [ModelDoc2::InsertProtrusionBlend4](ModelDoc2__InsertProtrusionBlend4.htm).

Description

This method creates a lofted body or boss cut from the selected profiles, centerline, and guide curves.

Syntax (OLE Automation)

(void) ModelDoc2.InsertProtrusionBlend3 ( closed, keepTangency, forceNonRational, tessToleranceFactor, startMatchingType, endMatchingType )

| Input: | (BOOL) closed | TRUE for closed loft, FALSE for open loft; if TRUE, and if you have selected less that three profiles, then any selected guide curves must be closed curves |
| --- | --- | --- |
| Input: | (BOOL) keepTangency | If the section curves are tangent, then you have the option to specify whether the resulting faces is also tangent; specify TRUE to maintain the tangency as seen in the section curves, FALSE otherwise; when generating tangent surfaces, planar and cylindrical surface shapes are maintained if the section curves exhibit these characteristics |
| Input: | (BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Input: | (double) tessToleranceFactor | Factor to control the number of intermediate sections used for loft with centerline; default value is 1.0; the greater the variable, the more intermediate sections are created |
| Input: | (short) startMatchingType | Tangency type at the start profile |
| Input: | (short) endMatchingType | Tangency type at the start profile |

Syntax (COM)

status = ModelDoc2->InsertProtrusionBlend3 ( closed, keepTangency, forceNonRational, tessToleranceFactor, startMatchingType, endMatchingType )

| Input: | (VARIANT_BOOL) closed | TRUE for closed loft, FALSE for open loft; if TRUE, and if you have selected less that three profiles, then any selected guide curves must be closed curves |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) keepTangency | If the section curves are tangent, then you have the option to specify whether the resulting faces is also tangent; specify TRUE to maintain the tangency as seen in the section curves, FALSE otherwise; when generating tangent surfaces, planar and cylindrical surface shapes are maintained if the section curves exhibit these characteristics |
| Input: | (VARIANT_BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Input: | (double) tessToleranceFactor | Factor to control the number of intermediate sections used for loft with centerline; default value is 1.0; the greater the variable, the more intermediate sections are created |
| Input: | (short) startMatchingType | Tangency type |
| Input: | (short) endMatchingType | Tangency type |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Selection of guide curves and centerline is optional; however, selection of the profiles must be in an order consistent with the desired direction of the loft. Because you are creating a surface, the section profiles can be open.

Use of guide curves is recommended, especially when selection of profiles is done in the FeatureManager design tree. You can use any number of profiles; however, if you have selected only one profile, then any selected guide curves must be closed curves.

Use ModelDocExtension::SelectByID to select the profiles and guide curves. The mark for:

- profile selections should be 1
- any guide curve selection, if provided, should be a 2
- centerline selection, if provided, should be a 4
- start tangency vector selection, if provided, should be a 8
- start tangency faces selection, if provided, should be a 16 (not available)
- end tangency vector selection, if provided, should be a 32
- end tangency faces selection, if provided, should be a 64 (not available)

Linear edge, sketch line, axis, plane, and planar faces are qualified for tangency vector sections.

The tangency types can be one these:

- 0 none
- 1 tangent to the normal of the profile
- 2 tangent to a selected vector
- 3 tangency to all the adjacent faces sharing an edge with the start profile
- 4 tangent to some of the selected faces sharing an edge with the start profile (not available)
