---
title: "Curve::GetBCurveParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve__GetBCurveParams.htm"
---

# Curve::GetBCurveParams

This method is obsolete and has been superseded by [Curve::GetBCurveParams3](sldworksAPI.chm::/Curve/Curve__GetBCurveParams3.htm).

Description

This method gets the parameters of the curve.

Syntax (OLE Automation)

retval = Curve.GetBCurveParams ( wantCubicIn)

| Input: | (BOOL) wantCubicIn | TRUE returns cubic rational parameters, FALSE does not |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray describing the parameters of the curve |

Syntax (COM)

status = Curve->IGetBCurveParams ( retval )

| Output: | (double*) retval | Pointer to an array of doubles describing the parameters of the curve |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For COM implementations, see Curve::IGetBCurveParamsSize2 to determine the size of the array returned and whether the curve data returned by Cure::IGetBCurveParams is cubic rational or not.

To control the accuracy of the curve data, see Modeler::SetToleranceValue.

The return value retval is an array of doubles. The array size is ( 2 + numKnots + numControlPointDoubles) where numKnots is (numControlPoints + order). The array is as follows:

[ packedDouble1, packedDouble2, knot1, knot2,..., ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

where:

- packedDouble1 is an integer pair containing the Dimension and Order
- packedDouble2 is an integer pair containing the NumControlPoints and Periodicity
- knot1
- knot2

...

- ControlPoint1[dimension]
- ControlPoint2[dimension]

...

The size of the control point array is based on the curve dimension:

- If Dimension = 3, then ControlPoint is an array of 3 doubles ( x, y, z )
- If Dimension = 4, then ControlPoint is an array of 4 doubles ( x, y, z, w ) where w = weight
