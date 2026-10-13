---
title: "ModelDoc::CreatePlaneAtAngle2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePlaneAtAngle2.htm"
---

# ModelDoc::CreatePlaneAtAngle2

This method is obsolete and has been superseded by [ModelDoc2::CreatePlaneAtAngle2](../ModelDoc2/ModelDoc2__CreatePlaneAtAngle2.htm).

Description

This method creates a construction (reference) plane at an angle from the selected plane along the selected edge.

Syntax (OLE Automation)

retval = ModelDoc.CreatePlaneAtAngle2 ( val, flipDir )

| Input: | (double) val | Angle from the selected plane in radians |
| --- | --- | --- |
| Input: | (BOOL) flipDir | TRUE to flip the direction away from the first direction |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created RefPlane object |

Syntax (COM)

status = ModelDoc->ICreatePlaneAtAngle2 ( val, flipDir, &retval )

| Input: | (double) val | Angle from the selected plane in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the direction away from the first direction |
| Output: | (LPREFPLANE) retval | Pointer to the newly created RefPlane object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method follows the current document setting for displaying of the reference plane as it is created. If display of reference planes is disabled, then you do not see the reference plane on the screen as it is created. If display of reference planes is enabled, then you do see it as it is created. ModelDoc2::GetUserPreferenceToggle and ModelDoc2::SetUserPreferenceToggle with swDisplayPlanes enum value get or set this display preference.

This method does not select the reference plane after it is created. Objects that are selected before running this method are still be selected when the method completes rather than the newly created reference plane.

This method returns a RefPlane object. You can then use this object for further operations on the reference plane feature. Just having a reference plane may not be terribly useful, except that it is a feature, which is an entity, so methods available on those objects are available. For an OLE user, those functions are directly accessible; for a COM user, those functions are available via use of a QueryInterface. For example, if the reference plane must be selected, you can use Entity::Select.
