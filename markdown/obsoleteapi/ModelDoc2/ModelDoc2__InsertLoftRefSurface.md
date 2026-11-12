---
title: "ModelDoc2::InsertLoftRefSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertLoftRefSurface.htm"
---

# ModelDoc2::InsertLoftRefSurface

This method is obsolete and has been superseded by [ModelDoc2::InsertLoftRefSurfac2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertLoftRefSurface2.htm).

Description

This method creates a lofted surface from the selected profiles and guide curves. Selection of guide curves is optional; however, selection of the profiles must be in an order consistent with the desired direction of the loft. Because you are creating a surface, the section profiles can be open.

Syntax (OLE Automation)

void ModelDoc2.InsertLoftRefSurface ( closed, keepTangency, forceNonRational)

| Input: | (BOOL) closed | TRUE if you want the loft to be closed, FALSE if the loft will be open; if TRUE, then you must have at least three profiles selected, and if you are using guide curves, the guide curves must be closed |
| --- | --- | --- |
| Input: | (BOOL) keepTangency | If the section curves are tangent, then you have the option to specify whether the resulting surfaces are also be tangent; specify TRUE to maintain the tangency as seen in the section curves, FALSE otherwise; when generating tangent surfaces, SolidWorks maintains planar and cylindrical surface shapes if the section curves exhibit these characteristics |
| Input: | (BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational; FALSE to not |

Syntax (COM)

status = ModelDoc2->InsertLoftRefSurface ( closed, keepTangency, forceNonRational )

| Input: | (VARIANT_BOOL) closed | TRUE if you want the loft to be closed, FALSE if the loft will be open; if TRUE, then you must have at least three profiles selected, and if you are using guide curves, the guide curves must be closed |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) keepTangency | If the section curves are tangent, then you have the option to specify whether the resulting surfaces are also be tangent; specify TRUE to maintain the tangency as seen in the section curves, FALSE otherwise; when generating tangent surfaces, SolidWorks maintains planar and cylindrical surface shapes if the section curves exhibit these characteristics |
| Input: | (VARIANT_BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational; FALSE to not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use of guide curves is recommended, especially when selection of profiles is done in the FeatureManager design tree.

You can use any number of profiles; however, if you have selected less that three profiles, then any selected guide curves must be closed curves.

Use ModelDoc2::SelectByMark to select the profiles and guide curves. The mark for the profile selections should be a 1 while the mark for any guide curve selection, if provided, should be a 2.
