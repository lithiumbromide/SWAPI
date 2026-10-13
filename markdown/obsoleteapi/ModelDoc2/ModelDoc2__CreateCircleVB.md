---
title: "ModelDoc2::CreateCircleVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateCircleVB.htm"
---

# ModelDoc2::CreateCircleVB

This method is obsolete and has been superseded by [ModelDoc2::CreateCircle2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateCircle2.htm).

Description

This method creates a circle using a center point and another point on the circle that helps determine the radius. This point also enables any automatic relations, snapping to grid, and so on., which may be applicable depending on its location. This method is for use in Visual Basic and other forms of Basic that do not support SafeArrays.

Syntax (OLE Automation)

void ModelDoc2.CreateCircleVB ( p1x, p1y, p1z, radius)

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) radius | Radius of circle in meters |

Syntax (COM)

status = ModelDoc2->CreateCircleVB ( p1x, p1y, p1z, radius )

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) radius | Radius of circle in meters |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
