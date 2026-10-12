---
title: "ModelDoc2::CreatePlaneAtAngle2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePlaneAtAngle2.htm"
---

# ModelDoc2::CreatePlaneAtAngle2

This method is obsolete and has been superseded by [ModelDoc2::CreatePlaneAtAngle3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreatePlaneAtAngle3.htm).

Description

This method creates a construction (also called reference) plane at an angle from the selected plane along the selected edge.

Syntax (OLE Automation)

retval = ModelDoc2.CreatePlaneAtAngle2 ( val, flipDir )

| Input: | (double) val | Angle from the selected plane in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | TRUE for other way for first direction |
| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created reference plane |

Syntax (COM)

status = ModelDoc2->ICreatePlaneAtAngle2 ( val, flipDir, &retval )

| Input: | (double) val | Angle from the selected plane in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | TRUE for other way for first direction |
| Output: | (LPREFPLANE) retval | Pointer to the newly created reference plane |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method uses the current document setting for displaying the reference plane as it is created. If display of reference planes is disabled, then you do not see the reference plane on the screen as it is created. If display of reference planes is enabled, then you see it as it is created. ModelDoc2::GetUserPreferenceToggle and ModelDoc2::SetUserPreferenceToggle, with swDisplayPlanes enum value, get or set this display preference.

This method does not select the reference plane after it is created. Objects that are selected before running this method are still be selected when the method is completed, not the newly created reference plane.

This method returns a RefPlane object. You can use this object for further operations on the reference plane feature. Having ust a RefPlane may not be terribly useful, except that it is a feature, which is an entity, so methods available on those objects are available. For an OLE user, those functions are directly accessible; for a COM user, those functions are available via QueryInterface. For example, if the reference plane must be selected, you can use Entity::Select.
