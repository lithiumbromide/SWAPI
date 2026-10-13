---
title: "ModelDoc::CreateCircleVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateCircleVB.htm"
---

# ModelDoc::CreateCircleVB

This method is obsolete and has been superseded by [ModelDoc::CreateCircle2](ModelDoc__CreateCircle2.htm).

Description

This method creates a circle using a center point and another point on the circle, which helps determine the radius. This point also enables any automatic relations, snapping to the grid, and so on, depending on its location. This method is for use in Visual Basic and other forms of Basic that do not support SafeArrays.

Syntax (OLE Automation)

void ModelDoc.CreateCircleVB ( p1x, p1y, p1z, radius)

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) radius | Radius of circle in meters |

Syntax (COM)

status = ModelDoc->CreateCircleVB ( p1x, p1y, p1z, radius )

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) radius | Radius of circle in meters |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
