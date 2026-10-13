---
title: "ModelDoc2::CreateTangentArc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateTangentArc.htm"
---

# ModelDoc2::CreateTangentArc

This method is obsolete and has been superseded by [ModelDoc2::CreateTangentArc2](ModelDoc2__CreateTangentArc2.htm).

Description

This method creates an arc that is tangent to the entity which shares its start point. The input start point must be an existing point in the sketch and an endpoint of some other sketch entity.

Syntax (OLE Automation)

retval = ModelDoc2.CreateTangentArc ( p1x, p1y, p1z, p2x, p2y, p2z)

| Input: | (double) p1x | Start point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Start point y value in meters |
| Input: | (double) p1z | Start point z value in meters |
| Input: | (double) p2x | End point x value in meters |
| Input: | (double) p2y | End point y value in meters |
| Input: | (double) p2z | End point z value in meters |
| Return: | (BOOL) retval | 1 = success, 0 = failure |

Syntax (COM)

status = ModelDoc2->CreateTangentArc ( p1x, p1y, p1z, p2x, p2y, p2z, &retval )

| Input: | (double) p1x | Start point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Start point y value in meters |
| Input: | (double) p1z | Start point z value in meters |
| Input: | (double) p2x | End point x value in meters |
| Input: | (double) p2y | End point y value in meters |
| Input: | (double) p2z | End point z value in meters |
| Output: | (VARIANT_BOOL) retval | 1 = success, 0 = failure |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
