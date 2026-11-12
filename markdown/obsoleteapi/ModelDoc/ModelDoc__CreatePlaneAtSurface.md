---
title: "ModelDoc::CreatePlaneAtSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePlaneAtSurface.htm"
---

# ModelDoc::CreatePlaneAtSurface

This method is obsolete and has been superseded by [ModelDoc::CreatePlaneAtSurface2](ModelDoc__CreatePlaneAtSurface2.htm).

Description

This method creates a reference plane tangent (or normal) to a surface.

Syntax (OLE Automation)

void ModelDoc.CreatePlaneAtSurface ( interIndex, projOpt, reverseDir, normalPlane, angle )

| Input: | (int) interIndex | When there are multiple intersections, other solutions may exist; for a surface, plane, and edge, the intersection index is the intersection point to use when there are multiple intersections; when the intersection index input is more than the number of intersection points, the index of the last intersection point found will be used |
| --- | --- | --- |
| Input: | (BOOL) projOpt | For a sketch point and a surface, TRUE to project the sketch plane point along the sketch plane normal, FALSE to project the sketch plane point normal to the surface |
| Input: | (BOOL) normalPlane | For a conical surface, TRUE to find the plane normal to the surface, FALSE to find the plane tangent to the surface |
| Input: | (double) angle | Value of the angular offset of the normal plane, relative to a chosen reference plane |

Syntax (COM)

status = ModelDoc->CreatePlaneAtSurface ( interIndex, projOpt, reverseDir, normalPlane, angle )

| Input: | (int) interIndex | When there are multiple intersections, other solutions may exist; for a surface, plane, and edge, the intersection index is the intersection point to use when there are multiple intersections; when the intersection index input is more than the number of intersection points, the index of the last intersection point found will be used |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) projOpt | For a sketch point and a surface, TRUE to project the sketch plane point along the sketch plane normal, FALSE to project the sketch plane point normal to the surface |
| Input: | (VARIANT_BOOL) normalPlane | For a conical surface, TRUE to find the plane normal to the surface, FALSE to find the plane tangent to the surface |
| Input: | (double) angle | Value of the angular offset of the normal plane, relative to a chosen reference plane |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
