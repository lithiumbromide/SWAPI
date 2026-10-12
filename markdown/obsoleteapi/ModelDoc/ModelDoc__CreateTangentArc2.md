---
title: "ModelDoc::CreateTangentArc2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateTangentArc2.htm"
---

# ModelDoc::CreateTangentArc2

This method is obsolete and has been superseded by [ModelDoc2::CreateTangentArc2](../ModelDoc2/ModelDoc2__CreateTangentArc2.htm).

Description

This method creates an arc that is tangent to the entity that shares it start point. The input start point must be an existing point in the sketch and be the endpoint of another sketch entity.

Syntax (OLE Automation)

retval = ModelDoc.CreateTangentArc2 ( p1x, p1y, p1z, p2x, p2y, p2z, arcType )

| Input: | (double) p1x | Start point x |
| --- | --- | --- |
| Input: | (double) p1y | Start point y |
| Input: | (double) p1z | Start point z |
| Input: | (double) p2x | End point x |
| Input: | (double) p2y | End point y |
| Input: | (double) p2z | End point z |
| Input: | (long) arcType | Type of tangent arc as defined in swTangentArcTypes_e |
| Return: | (BOOL) retval | True for success |

Syntax (COM)

status = ModelDoc->CreateTangentArc2 ( p1x, p1y, p1z, p2x, p2y, p2z, arcType, &retval )

| Input: | (double) p1x | Start point x |
| --- | --- | --- |
| Input: | (double) p1y | Start point y |
| Input: | (double) p1z | Start point z |
| Input: | (double) p2x | End point x |
| Input: | (double) p2y | End point y |
| Input: | (double) p2z | End point z |
| Input: | (long) arcType | Type of tangent arc as defined in swTangentArcTypes_e |
| Output: | (VARIANT_BOOL) retval | TRUE for success, FALSE for failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The arcType argument refers to the direction that the tangent takes off from the other sketch entity.
