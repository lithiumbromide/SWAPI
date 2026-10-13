---
title: "ModelDoc2::CreatePlanePerCurveAndPassPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePlanePerCurveAndPassPoint.htm"
---

# ModelDoc2::CreatePlanePerCurveAndPassPoint

This method is obsolete and has been superseded by [ModelDoc2::CreatePlanePerCurveAndPassPoint2](ModelDoc2__CreatePlanePerCurveAndPassPoint2.htm).

Description

This method creates a reference plane that is perpendicular to the selected curve and passes through a selected point.

Syntax (OLE Automation)

void ModelDoc2.CreatePlanePerCurveAndPassPoint ( origAtCurve)

| Input: | (BOOL) origAtCurve | TRUE if you want the origin to be on the curve, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->CreatePlanePerCurveAndPassPoint ( origAtCurve )

| Input: | (VARIANT_BOOL) origAtCurve | TRUE if you want the origin to be on the curve, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
