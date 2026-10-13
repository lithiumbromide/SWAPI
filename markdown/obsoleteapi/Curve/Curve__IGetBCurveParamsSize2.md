---
title: "Curve::IGetBCurveParamsSize2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve__IGetBCurveParamsSize2.htm"
---

# Curve::IGetBCurveParamsSize2

This method is obsolete and has been superseded by [Curve::IGetBCurveParamsSize3](sldworksAPI.chm::/Curve/Curve__IGetBCurveParamsSize3.htm).

Description

This method gets the b-curve size.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Curve->IGetBCurveParamsSize2 ( wantCubicIn, wantNRational, &retval )

| Input: | (VARIANT_BOOL) wantCubicIn | TRUE for cubic curves, FALSE if not |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) wantNRational | TRUE for non-rational curves, FALSE if not |
| Output: | (long) retval | Size of the data set returned by Curve::IGetBCurveParams. |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use this method to control the type of information returned in the subsequent call to Curve::IGetBCurveParams.

To control the accuracy of the curve data, see Modeler::SetToleranceValue.
