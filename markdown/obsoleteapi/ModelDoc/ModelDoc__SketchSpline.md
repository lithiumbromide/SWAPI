---
title: "ModelDoc::SketchSpline"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchSpline.htm"
---

# ModelDoc::SketchSpline

This method is obsolete and has been superseded by [ModelDoc2::SketchSpline](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchSpline.htm).

Description

This method creates a spline, or continues one, passing through the point (x, y, z). See also ModelDoc::CreateSpline.

Syntax (OLE Automation)

void ModelDoc.SketchSpline ( morePts, x, y, z)

| Input: | (long) morePts | Number of points left to specify after this point |
| --- | --- | --- |
| Input: | (double) x | x coordinate of point in meters |
| Input: | (double) y | y coordinate of point in meters |
| Input: | (double) z | z coordinate of point in meters |

Syntax (COM)

status = ModelDoc->SketchSpline ( morePts, x, y, z )

| Input: | (long) morePts | Number of points left to specify after this point |
| --- | --- | --- |
| Input: | (double) x | x coordinate of point in meters |
| Input: | (double) y | y coordinate of point in meters |
| Input: | (double) z | z coordinate of point in meters |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If you are creating a sketch spline from a macro, then you must use ModelDoc::SketchSpline. You cannot use ModelDoc::CreateSpline because it requires an array of points.

In 2D sketches, SolidWorks ignores the z value.
