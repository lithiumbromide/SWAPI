---
title: "ModelDoc::CreatePlanePerCurveAndPassPoint2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePlanePerCurveAndPassPoint2.htm"
---

# ModelDoc::CreatePlanePerCurveAndPassPoint2

This method is obsolete and has been superseded by [ModelDoc2::CreatePlanePerCurveAndPassPoint2](../ModelDoc2/ModelDoc2__CreatePlanePerCurveAndPassPoint2.htm).

Description

This method creates a reference plane that is perpendicular to the selected curve and passes through a selected point.

Syntax (OLE Automation)

retval = ModelDoc.CreatePlanePerCurveAndPassPoint2 ( origAtCurve )

| Input: | (BOOL) origAtCurve | TRUE if you want the origin to be on the curve, FALSE otherwise |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created RefPlane object |

Syntax (COM)

status = ModelDoc->ICreatePlanePerCurveAndPassPoint2 ( origAtCurve, &retval )

| Input: | (VARIANT_BOOL) origAtCurve | TRUE if you want the origin to be on the curve, FALSE otherwise |
| --- | --- | --- |
| Output: | (LPREFPLANE) retval | Pointer to the newly created RefPlane object |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

This method follows the current document setting for displaying of the reference plane as it is created. If display of reference planes is disabled, then you do not see the reference plane on the screen as it is created. If display of reference planes is enabled, then you see it as it is created. ModelDoc2::GetUserPreferenceToggle and ModelDoc2::SetUserPreferenceToggle with swDisplayPlanes enum value get or set this display preference.

This method does not select the reference plane after it is created. Objects that are selected before running this method are still selected when the method completes rather than the newly created reference plane.

This method returns a RefPlane object. This object can then be used for operations on the reference plane feature. Just having a RefPlane object may not be terribly useful, except that it is a feature, which is an entity, so methods available on those objects are available. For an OLE user, those functions are directly accessible; for a COM user, those functions are available via use of a QueryInterface. For example, if the reference plane must be selected, use Entity::Select.
