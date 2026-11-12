---
title: "ModelDoc::CreatePlaneAtSurface2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePlaneAtSurface2.htm"
---

# ModelDoc::CreatePlaneAtSurface2

This method is obsolete and has been superseded by [ModelDoc2::CreatePlaneAtSurface2](../ModelDoc2/ModelDoc2__CreatePlaneAtSurface2.htm).

Description

This method creates a reference plane tangent (or normal) to a surface.

Syntax (OLE Automation)

retval = ModelDoc.CreatePlaneAtSurface2 ( interIndex, projOpt, reverseDir, normalPlane, angle )

| Input: | (int) interIndex | When there are multiple intersections, other solutions may exist; for a surface, plane, and edge, the intersection index is the intersection point to use when there are multiple intersections; when the intersection index input is more than the number of intersection points, the index of the last intersection point found will be used |
| --- | --- | --- |
| Input: | (BOOL) projOpt | For a sketch point and a surface, TRUE to project the sketch plane point along the sketch plane normal, FALSE to project the sketch plane point normal to the surface |
| Input: | (BOOL) reverseDir | Flag to create the plane on the opposite side of the sketch plane |
| Input: | (BOOL) normalPlane | For a conical surface, TRUE to find the plane normal to the surface, FALSE to find the plane tangent to the surface |
| Input: | (double) angle | Value of the angular offset of the normal plane, relative to a chosen reference plane |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created RefPlane object |

Syntax (COM)

status = ModelDoc->ICreatePlaneAtSurface2 ( interIndex, projOpt, reverseDir, normalPlane, angle, &retval )

| Input: | (int) interIndex | When there are multiple intersections, other solutions may exist; for a surface, plane, and edge, the intersection index is the intersection point to use when there are multiple intersections; when the intersection index input is more than the number of intersection points, the index of the last intersection point found will be used |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) projOpt | For a sketch point and a surface, TRUE to project the sketch plane point along the sketch plane normal, FALSE to project the sketch plane point normal to the surface |
| Input: | (VARIANT_BOOL) reverseDir | Flag to create the plane on the opposite side of the sketch plane |
| Input: | (VARIANT_BOOL) normalPlane | For a conical surface, TRUE to find the plane normal to the surface, FALSE to find the plane tangent to the surface |
| Input: | (double) angle | Value of the angular offset of the normal plane, relative to a chosen reference plane |
| Output: | (LPREFPLANE) retval | Pointer to the newly created RefPlane object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method follows the current document setting for displaying of the reference plane as it is created. If display of reference planes is disabled, then you do not see the reference plane on the screen as it is created. If display of reference planes is enabled, then you do see it as it is created. ModelDoc2::GetUserPreferenceToggle and ModelDoc2::SetUserPreferenceToggle with swDisplayPlanes enum value get or set this display preference.

This method does not select the reference plane after it is created. Objects that are selected before running this method are still be selected when the method completes rather than the newly created reference plane.

This method returns a RefPlane object. This object can then be used for further operations on the reference plane feature. Just having a RefPlane object may not be terribly useful, except that it is a feature, which is an entity, so methods available on those objects are available. For an OLE user, those functions are directly accessible; for a COM user, those functions are available via use of a QueryInterface. For example, if the reference plane must be selected, use Entity::Select.
