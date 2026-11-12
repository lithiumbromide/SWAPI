---
title: "ModelDoc::SketchPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchPoint.htm"
---

# ModelDoc::SketchPoint

This method is obsolete and has been superseded by [ModelDoc::CreatePoint2](ModelDoc__CreatePoint2.htm).

Description

This method creates a point entity at point (x, y, z).

Syntax (OLE Automation)

void ModelDoc.SketchPoint ( x, y, z)

| Input: | (double) x | x value of point in meters |
| --- | --- | --- |
| Input: | (double) y | y value of point in meters |
| Input: | (double) z | Not used |

Syntax (COM)

status = ModelDoc->SketchPoint ( x, y, z )

| Input: | (double) x | x value of point in meters |
| --- | --- | --- |
| Input: | (double) y | y value of point in meters |
| Input: | (double) z | Not used |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The z value should be set to 0.0 as points created in a sketch must be in the particular sketch plane.
