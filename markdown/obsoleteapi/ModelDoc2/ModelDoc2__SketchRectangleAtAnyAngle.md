---
title: "ModelDoc2::SketchRectangleAtAnyAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchRectangleAtAnyAngle.htm"
---

# ModelDoc2::SketchRectangleAtAnyAngle

This method is obsolete and has been superseded by [SketchManager::Create3PointCornerRectangle](sldworksAPI.chm::/SketchManager/SketchManager__Create3PointCornerRectangle.htm).

Description

This method creates a sketched rectangle at the specified angle.

Syntax (OLE Automation)

void ModelDoc2.SketchRectangleAtAnyAngle ( x1, y1, z1, x2, y2, z2, x3, y3, z3, autoConstrain )

| Input: | (double) x1 | X value of corner 1 |
| --- | --- | --- |
| Input: | (double) y1 | Y value of corner 1 |
| Input: | (double) z1 | Z value of corner 1 |
| Input: | (double) x2 | X value of corner 2 defining the bottom line from corner 1 |
| Input: | (double) y2 | Y value of corner 2 defining the bottom line from corner 1 |
| Input: | (double) z2 | Z value of corner 2 defining the bottom line from corner 1 |
| Input: | (double) x3 | X value of corner 3; diagonal to corner 1 |
| Input: | (double) y3 | Y value of corner 3; diagonal to corner 1 |
| Input: | (double) z3 | Z value of corner 3; diagonal to corner 1 |
| Input: | (BOOL) autoConstrain | TRUE to add automatic constraints to the rectangle geometry, FALSE to not |

Syntax (COM)

status = ModelDoc2->SketchRectangleAtAnyAngle ( x1, y1, z1, x2, y2, z2, x3, y3, z3, autoConstrain )

| Input: | (double) x1 | X value of corner 1 |
| --- | --- | --- |
| Input: | (double) y1 | Y value of corner 1 |
| Input: | (double) z1 | Z value of corner 1 |
| Input: | (double) x2 | X value of corner 2 defining the bottom line from corner 1 |
| Input: | (double) y2 | Y value of corner 2 defining the bottom line from corner 1 |
| Input: | (double) z2 | Z value of corner 2 defining the bottom line from corner 1 |
| Input: | (double) x3 | X value of corner 3; diagonal to corner 1 |
| Input: | (double) y3 | Y value of corner 3; diagonal to corner 1 |
| Input: | (double) z3 | Z value of corner 3; diagonal to corner 1 |
| Input: | (BOOL) autoConstrain | TRUE to add automatic constraints to the rectangle geometry, FALSE to not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
