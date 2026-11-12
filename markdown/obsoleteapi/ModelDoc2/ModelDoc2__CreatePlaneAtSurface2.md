---
title: "ModelDoc2::CreatePlaneAtSurface2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePlaneAtSurface2.htm"
---

# ModelDoc2::CreatePlaneAtSurface2

This method is obsolete and has been superseded by [ModelDoc2::CreatePlaneAtSurface3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreatePlaneAtSurface3.htm).

Description

This method creates a reference plane tangent (or normal) to a surface.

Syntax (OLE Automation)

retval = ModelDoc2.CreatePlaneAtSurface2 ( interIndex, projOpt, reverseDir, normalPlane, angle )

| Input: | (int) interIndex | Multiple intersections - other solutions may exist Surface, plane, and edge - the intersection index is the intersection point to use when there are multiple intersections; when the intersection index input is more than the number of intersection points, the index of the last intersection point found will be used |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) projOpt | TRUE to project the sketch plane point along the sketch plane normal for a sketch point and a surface, FALSE to project the sketch plane point normal to the surface |
| Input: | (VARIANT_BOOL) reverseDir | TRUE to create the plane on the opposite side of the sketch plane, FALSE to not |
| Input: | (VARIANT_BOOL) normalPlane | TRUE to find the plane normal to the surface for a conical surface, FALSE to find the plane tangent to the surface |
| Input: | (double) angle | Value of the angular offset of the normal plane, relative to a chosen reference plane |
| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created RefPlane object |

Syntax (COM)

status = ModelDoc2->ICreatePlaneAtSurface2 ( interIndex, projOpt, reverseDir, normalPlane, angle, &retval )

| Input: | (int) interIndex | Multiple intersections - other solutions may exist Surface, plane, and edge - the intersection index is the intersection point to use when there are multiple intersections; when the intersection index input is more than the number of intersection points, the index of the last intersection point found will be used |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) projOpt | TRUE to project the sketch plane point along the sketch plane normal for a sketch point and a surface, FALSE to project the sketch plane point normal to the surface |
| Input: | (VARIANT_BOOL) reverseDir | TRUE to create the plane on the opposite side of the sketch plane, FALSE to not |
| Input: | (VARIANT_BOOL) normalPlane | TRUE to find the plane normal to the surface for a conical surface, FALSE to find the plane tangent to the surface |
| Input: | (double) angle | Value of the angular offset of the normal plane, relative to a chosen reference plane |
| Output: | (LPREFPLANE) retval | Pointer to the newly created RefPlane object |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method uses the current document setting for displaying of the reference plane as it is created. If display of reference planes is disabled, then you do not see the reference plane on the screen as it is created. If display of reference planes is enabled, then you do see it as it is created. ModelDoc2::GetUserPreferenceToggle and ModelDoc2::SetUserPreferenceToggle with swDisplayPlanes enum value, get or set this display preference.

This method does not select the reference plane after it is created. Objects that are selected before running this method are still be selected when the method is completed, not the newly created reference plane.

This method returns a RefPlane object. This object can then be used for further operations on the reference plane feature. Just having a RefPlane object may not be terribly useful, except that it is a feature, which is an entity, so methods available on those objects are available. For an OLE user, those functions are directly accessible; for a COM user, those functions are available via QueryInterface. For example, if the reference plane must be selected, use Entity::Select.
