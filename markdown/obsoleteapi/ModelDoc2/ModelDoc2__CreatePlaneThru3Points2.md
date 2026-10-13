---
title: "ModelDoc2::CreatePlaneThru3Points2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePlaneThru3Points2.htm"
---

# ModelDoc2::CreatePlaneThru3Points2

This method is obsolete and has been superseded by [ModelDoc2::CreatePlaneThru3Points3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreatePlaneThru3Points3.htm).

Description

This method creates a construction (also called reference) plane through three currently selected points.

Syntax (OLE Automation)

retval = ModelDoc2.CreatePlaneThru3Points2 ( )

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created RefPlane object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->ICreatePlaneThru3Points2 ( &retval )

| Output: | (LPREFPLANE) retval | Pointer to the newly created RefPlane object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

This method uses the current document setting for displaying of the reference plane as it is created. If display of reference planes is disabled, then you do not see the reference plane on the screen as it is created. If display of reference planes is enabled, then you do see it as it is created. The ModelDoc2::GetUserPreferenceToggle and ModelDoc2::SetUserPreferenceToggle APIs, with swDisplayPlanes enum value, get or set this display preference.

This method does not select the reference plane after it is created. Objects that are selected before running this method are still selected when the method completes, not the newly created reference plane.

This method returns a RefPlane object. This object can then be used for further operations on the reference plane feature. Just having a RefPlane may not be terribly useful, except that it is a feature, which is an dntity, so methods available on those objects are available. For an OLE user, those functions are directly accessible; for a COM user, those functions are available via QueryInterface. For example, if the reference plane must be selected, use Entity::Select.
