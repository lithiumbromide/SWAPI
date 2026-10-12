---
title: "ModelDoc::GetStandardViewRotation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetStandardViewRotation.htm"
---

# ModelDoc::GetStandardViewRotation

This method is obsolete and has been superseded by [ModelDoc2::GetStandardViewRotation](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IGetStandardViewRotation.htm).

Description

This method gets the specified view orientation matrix with respect to the Front view. Be aware that the user may have redefined the Front view to be something other than the X-Y plane.

Syntax (OLE Automation)

retval = ModelDoc.GetStandardViewRotation ( viewId)

| Input: | (long) viewId | View ID to evaluate as defined in swStandardViews_e |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray describing the view rotation with respect to the Front view; this is an array of 9 doubles |

Syntax (COM)

status = ModelDoc->IGetStandardViewRotation ( viewId, retval )

| Input: | (long) viewId | View ID to evaluate as defined in swStandardViews_e |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of 9 doubles describing the view rotation with respect to the Front view |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
