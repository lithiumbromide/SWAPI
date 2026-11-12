---
title: "ModelDoc::Insert3DSplineCurve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Insert3DSplineCurve.htm"
---

# ModelDoc::Insert3DSplineCurve

This method is obsolete and has been superseded by [ModelDoc2::Insert3DSplineCurve](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Insert3DSplineCurve.htm).

Description

This method inserts a 3D-spline curve through the selected reference points.

Syntax (OLE Automation)

void ModelDoc.Insert3DSplineCurve ( curveClosed)

| Input: | (BOOL) curveClosed | TRUE if you want the curve to be closed, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->Insert3DSplineCurve ( curveClosed )

| Input: | (VARIANT_BOOL) curveClosed | TRUE if you want the curve to be closed, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To create 2D splines on a sketch, use ModelDoc::SketchSpline or ModelDoc::CreateSpline.
