---
title: "ModelDoc2::CreatePlaneAtOffset2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePlaneAtOffset2.htm"
---

# ModelDoc2::CreatePlaneAtOffset2

This method is obsolete and has been superseded by [ModelDoc2::CreatePlaneAtOffset3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreatePlaneAtOffset3.htm).

Description

This method creates a construction (also called reference) plane at an offset from the selected plane or planar face.

Syntax (OLE Automation)

retval = ModelDoc2.CreatePlaneAtOffset2 ( val, flipDir )

| Input: | (double) val | Offset distance from selected plane in meters |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | This flag will determine the offset direction for the resulting plane |
| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created RefPlane object |

Syntax (COM)

status = ModelDoc2->ICreatePlaneAtOffset2 ( val, flipDir, &retval )

| Input: | (double) val | Offset distance from selected plane in meters |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | This flag will determine the offset direction for the resulting plane |
| Output: | (LPREFPLANE) retval | Pointer to the newly created RefPlane object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method uses the current document setting for displaying of the reference plane as it is created. If display of reference planes is disabled, then you do not see the reference plane on the screen as it is created. If display of reference planes is enabled, then you see it as it is created. ModelDoc2::GetUserPreferenceToggle and ModelDoc2::SetUserPreferenceToggle, with swDisplayPlanes enum value, get or set this display preference.

This method does not select the reference plane after it is created. Objects that are selected before running this method are still selected when the method is completed, not the newly created reference plane.

This method returns a RefPlane object. This object can then be used for further operations on the reference plane feature. Having just a RefPlane object may not be terribly useful, except that it is a feature, which is an entity, so methods available on those objects are available. For an OLE user, those functions are directly accessible; for a COM user, those functions are available via QueryInterface. For example, if the reference plane must be selected, use Entity::Select.
