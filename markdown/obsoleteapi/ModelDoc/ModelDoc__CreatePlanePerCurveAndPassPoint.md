---
title: "ModelDoc::CreatePlanePerCurveAndPassPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePlanePerCurveAndPassPoint.htm"
---

# ModelDoc::CreatePlanePerCurveAndPassPoint

This method is obsolete and has been superseded by [ModelDoc::CreatePlanePerCurveAndPassPoint2](ModelDoc__CreatePlanePerCurveAndPassPoint2.htm).

Description

This method creates a reference plane that is perpendicular to the selected curve and passes through a selected point.

Syntax (OLE Automation)

void ModelDoc.CreatePlanePerCurveAndPassPoint ( origAtCurve)

| Input: | (BOOL) origAtCurve | TRUE if you want the origin to be on the curve, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->CreatePlanePerCurveAndPassPoint ( origAtCurve )

| Input: | (VARIANT_BOOL) origAtCurve | TRUE if you want the origin to be on the curve, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
