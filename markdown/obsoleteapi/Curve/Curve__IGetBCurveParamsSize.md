---
title: "Curve::IGetBCurveParamsSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve__IGetBCurveParamsSize.htm"
---

# Curve::IGetBCurveParamsSize

This method is obsolete and has been superseded by [Curve::IGetBCurveParamsSize2](Curve__IGetBCurveParamsSize2.htm).

Description

This method gets the B-curve size.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Curve->IGetBCurveParamsSize ( wantCubicIn, &retval )

| Input: | (VARIANT_BOOL) wantCubicIn | TRUE for cubic curves, FALSE if not |
| --- | --- | --- |
| Output: | (long) retval | Size of the data set |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is used with Curve::GetBCurveParams.

If wantCubicIn is set to TRUE, then SolidWorks forces the output from a subsequent call to Curve::IGetBCurveParams to cubic. This might come out as rational if the underlying curve is a conic section, such as a circle or an ellipse.
