---
title: "Curve::Evaluate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve__Evaluate.htm"
---

# Curve::Evaluate

This method is obsolete and has been superseded by [Curve::Evaluate2](sldworksAPI.chm::/Curve/Curve__Evaluate2.htm).

Description

This method evaluates the curve at the specified parameter of the curve.

Syntax (OLE Automation)

retval = Curve.Evaluate ( Parameter )

| Input: | (double) Parameter | Curve parameter |
| --- | --- | --- |
| Return: | (VARIANT) retval | SafeArray containing an array of doubles |

Syntax (COM)

status = Curve->IEvaluate ( Parameter, &retval )

| Input: | (double) Parameter | Curve parameter |
| --- | --- | --- |
| Output: | (double) retval | Pointer to an array of doubles |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To determine a valid parameter range, use Curve::GetEndParams or Edge::GetCurveParams2.

The OLE Automation retval is an array of doubles with the following format:

[ PointX, PointY, PointZ, TangentX, TangentY, TangentZ, Success ]

where:

- PointX, PointY, and PointZ represent the 3D point in space for the given parameter
- TangentX, TangentY, and TangentZ represent the tangent vector at the point
- TRUE if the operation is successful

The COM return value is an array of 6 doubles representing the point and tangent. The success value is determined from the HRESULT return.

This method returns values in meters.
