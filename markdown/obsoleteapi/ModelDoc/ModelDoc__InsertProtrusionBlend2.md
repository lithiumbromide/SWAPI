---
title: "ModelDoc::InsertProtrusionBlend2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertProtrusionBlend2.htm"
---

# ModelDoc::InsertProtrusionBlend2

This method is obsolete and has been superseded by [ModelDoc::InsertProtrusionBlend3](ModelDoc__InsertProtrusionBlend3.htm).

Description

This method creates a lofted body or boss from the selected profiles and guide curves.

Syntax (OLE Automation)

void ModelDoc.InsertProtrusionBlend2 ( closed, keepTangency, forceNonRational)

| Input: | (BOOL) closed | TRUE if you want the loft to be closed, FALSE if the loft will be open; if TRUE, and if you have selected less that three profiles, then any selected guide curves must be closed curves |
| --- | --- | --- |
| Input: | (BOOL) keepTangency | If the section curves are tangent, then you have the option to specify whether the resulting faces will also be tangent; specify TRUE to maintain the tangency as seen in the section curves, FALSE otherwise; when generating tangent surfaces, SolidWorks will maintain planar and cylindrical surface shapes if the section curves exhibit these characteristics |
| Input: | (BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertProtrusionBlend2 ( closed, keepTangency, forceNonRational )

| Input: | (VARIANT_BOOL) closed | TRUE if you want the loft to be closed, FALSE if the loft will be open; if TRUE, and if you have selected less that three profiles, then any selected guide curves must be closed curves |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) keepTangency | If the section curves are tangent, then you have the option to specify whether the resulting faces will also be tangent; specify TRUE to maintain the tangency as seen in the section curves, FALSE otherwise; when generating tangent surfaces, SolidWorks will maintain planar and cylindrical surface shapes if the section curves exhibit these characteristics |
| Input: | (VARIANT_BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use of guide curves is recommended, especially when selection of profiles is done in the FeatureManager design tree.

You can use any number of profiles; however, if you have selected less that three profiles, then any selected guide curves must be closed curves.

Use a SelectByMark method to select the profiles and guide curves. The mark for the profile selections should be a 1, while the mark for any guide curve selection, if provided, should be a 2.
