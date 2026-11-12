---
title: "ModelDoc::CreateCircle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateCircle.htm"
---

# ModelDoc::CreateCircle

This method is obsolete and has been superseded by [ModelDoc::CreateCircle2](ModelDoc__CreateCircle2.htm).

Description

This method creates a circle using a center point and another point on the circle that helps determine the radius. This point also enables any automatic relations, snapping to the grid, and so on, depending on its location. See ModelDoc::CreateCircleVB for use in Visual Basic and other forms of Basic that do not support SafeArrays.

Syntax (OLE Automation)

retval = ModelDoc.CreateCircle ( p1x, p1y, p1z, p2x, p2y, p2z)

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) p2x | Point on circle x value in meters |
| Input: | (double) p2y | Point on circle y value in meters |
| Input: | (double) p2z | Point on circle z value in meters |
| Return: | (BOOL) retval | 1 = success, 0 = failure |

Syntax (COM)

status = ModelDoc->CreateCircle ( p1x, p1y, p1z, p2x, p2y, p2z, &retval )

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) p2x | Point on circle x value in meters |
| Input: | (double) p2y | Point on circle y value in meters |
| Input: | (double) p2z | Point on circle z value in meters |
| Output: | (VARIANT_BOOL) retval | 1 = success, 0 = failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
