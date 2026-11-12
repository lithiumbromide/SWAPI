---
title: "ModelDoc2::CreatePlaneAtSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePlaneAtSurface.htm"
---

# ModelDoc2::CreatePlaneAtSurface

This method is obsolete and has been superseded by [ModelDoc2::CreatePlaneAtSurface2](ModelDoc2__CreatePlaneAtSurface2.htm).

Description

This method creates create a reference plane tangent (or normal) to a surface.

Syntax (OLE Automation)

void ModelDoc2.CreatePlaneAtSurface ( interIndex, projOpt, reverseDir, normalPlane, angle )

| Input: | (int) interIndex | Multiple intersections - other solutions may exist Surface, plane, and edge - the intersection index is the intersection point to use when there are multiple intersections; when the intersection index input is more than the number of intersection points, the index of the last intersection point found will be used |
| --- | --- | --- |
| Input: | (BOOL) projOpt | TRUE to project the sketch plane point along the sketch plane normal when a sketch point and a surface, FALSE to project the sketch plane point normal to the surface |
| Input: | (BOOL) normalPlane | TRUE to find the plane normal to the surface for a conical surface, FALSE to find the plane tangent to the surface |
| Input: | (double) angle | Value of the angular offset of the normal plane, relative to a chosen reference plane |

Syntax (COM)

status = ModelDoc2->CreatePlaneAtSurface ( interIndex, projOpt, reverseDir, normalPlane, angle )

| Input: | (int) interIndex | Multiple intersections - other solutions may exist Surface, plane, and edge - the intersection index is the intersection point to use when there are multiple intersections; when the intersection index input is more than the number of intersection points, the index of the last intersection point found will be used |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) projOpt | TRUE to project the sketch plane point along the sketch plane normal when a sketch point and a surface, FALSE to project the sketch plane point normal to the surface |
| Input: | (VARIANT_BOOL) normalPlane | TRUE to find the plane normal to the surface for a conical surface, FALSE to find the plane tangent to the surface |
| Input: | (double) angle | Value of the angular offset of the normal plane, relative to a chosen reference plane |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
