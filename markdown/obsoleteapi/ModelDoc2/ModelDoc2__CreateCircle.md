---
title: "ModelDoc2::CreateCircle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateCircle.htm"
---

# ModelDoc2::CreateCircle

This method is obsolete and has been superseded by [ModelDoc2::CreateCircle2](ModelDoc2__CreateCircle2.htm).

Description

This method creates a circle using a center point and another point on the circle which helps determine the radius. This point also enables any automatic relations/snapping to grid and so on that may be applicable depending on its location. See ModelDoc2::CreateCircleVB for use in Visual Basic and other forms of Basic that do not support SafeArrarys.

Syntax (OLE Automation)

retval = ModelDoc2.CreateCircle ( p1x, p1y, p1z, p2x, p2y, p2z)

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) p2x | Point on circle x value in meters |
| Input: | (double) p2y | Point on circle y value in meters |
| Input: | (double) p2z | Point on circle z value in meters |
| Return: | (BOOL) retval | 1 = success, 0 = failure |

Syntax (COM)

status = ModelDoc2->CreateCircle ( p1x, p1y, p1z, p2x, p2y, p2z, &retval )

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
