---
title: "ModelDoc::InsertProtrusionBlend4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertProtrusionBlend4.htm"
---

# ModelDoc::InsertProtrusionBlend4

This method is obsolete and has been superseded by [ModelDoc2::InsertProtrusionBlend4](../ModelDoc2/ModelDoc2__InsertProtrusionBlend4.htm).

Description

This method creates a lofted body or boss cut from the selected profiles, centerline, and guide curves.

Syntax (OLE Automation)

void ModelDoc.InsertProtrusionBlend4 ( closed, keepTangency, forceNonRational, tessToleranceFactor, startMatchingType, endMatchingType, isThinBody, thickness1, thickness2, thinType)

| Input: | (BOOL) closed | TRUE if you want the loft to be closed, FALSE if the loft will be open; if TRUE, and if you have selected less that three profiles, then any selected guide curves must be closed curves |
| --- | --- | --- |
| Input: | (BOOL) keepTangency | If the section curves are tangent, then you have the option to specify whether the resulting faces will also be tangent; specify TRUE to maintain the tangency as seen in the section curves, FALSE otherwise; when generating tangent surfaces, SolidWorks will maintain planar and cylindrical surface shapes if the section curves exhibit these characteristics |
| Input: | (BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Input: | (double) tessToleranceFactor | Factor to control the number of intermediate sections used for loft with centerline; the default value is 1.0; the greater the variable, the more intermediate sections are created |
| Input: | (short) startMatchingType | Tangency type at the start profile: = 0: none; = 1: tangent to the normal of the profile; = 2: tangent to a selected vector; = 3: tangency to all the adjacent faces sharing an edge with the start profile; = 4: tangent to some of the selected faces sharing an edge with the start profile (not available at this moment) |
| Input: | (short) endMatchingType | Tangency type at the end profile: = 0: none; = 1: tangent to the normal of the profile; = 2: tangent to a selected vector; = 3: tangency to all the adjacent faces sharing an edge with the start profile; = 4: tangent to some of the selected faces sharing an edge with the end profile (not available at this moment) |
| Input: | (BOOL) isThinBody | TRUE if this feature is a thin body, FALSE otherwise |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | TRUE if this feature is a thin feature, FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertProtrusionBlend4 ( closed, keepTangency, forceNonRational, tessToleranceFactor, startMatchingType, endMatchingType, isThinBody, thickness1, thickness2, thinType )

| Input: | (VARIANT_BOOL) closed | TRUE if you want the loft to be closed, FALSE if the loft will be open; if TRUE, and if you have selected less that three profiles, then any selected guide curves must be closed curves |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) keepTangency | If the section curves are tangent, then you have the option to specify whether the resulting faces will also be tangent; specify TRUE to maintain the tangency as seen in the section curves, FALSE otherwise; when generating tangent surfaces, SolidWorks will maintain planar and cylindrical surface shapes if the section curves exhibit these characteristics |
| Input: | (VARIANT_BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Input: | (double) tessToleranceFactor | Factor to control the number of intermediate sections used for loft with centerline; the default value is 1.0; the greater the variable, the more intermediate sections are created |
| Input: | (short) startMatchingType | Tangency type at the start profile: = 0: none; = 1: tangent to the normal of the profile; = 2: tangent to a selected vector; = 3: tangency to all the adjacent faces sharing an edge with the start profile; = 4: tangent to some of the selected faces sharing an edge with the start profile (not available at this moment) |
| Input: | (short) endMatchingType | Tangency type at the end profile: = 0: none; = 1: tangent to the normal of the profile; = 2: tangent to a selected vector; = 3: tangency to all the adjacent faces sharing an edge with the start profile; = 4: tangent to some of the selected faces sharing an edge with the end profile (not available at this moment) |
| Input: | (VARIANT_BOOL) isThinBody | TRUE if this feature is a thin body, FALSE otherwise. |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | TRUE if this feature is a thin feature, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Selection of guide curves and centerline is optional,; however, selection of the profiles must be in an order consistent with the desired direction of the loft. Since we are creating a surface, the section profiles can be open.

Use of guide curves is strongly recommended, especially when selection of profiles is done in the FeatureManager design tree.

You may use any number of profiles; however, if you have selected only one profile, then any selected guide curves must be closed curves.

SelectByMark and AndSelectByMark should be used to select the profiles and guide curves. The mark for the profile selections should be 1 ; the mark for any guide curve selection, if provided, should be a 2; the mark for the centerline selection, if provided, should be a 4; the mark for the start tangency vector selection, if provided, should be a 8; the mark for the start tangency faces selection, if provided, should be a 16 (not available currently); the mark for the end tangency vector selection, if provided, should be a 32; the mark for the end tangency faces selection, if provided, should be a 64 (not available currently); Note that linear edge, sketch line, axis, plane and planar faces are qualified for tangency vector sections.

The tangency types may be one of the following:

- 0 none
- 1 tangent to the normal of the profile
- 2 tangent to a selected vector
- 3 tangency to all the adjacent faces sharing an edge with the start profile
- 4 tangent to some of the selected faces sharing an edge with the start profile (not available at this moment)
