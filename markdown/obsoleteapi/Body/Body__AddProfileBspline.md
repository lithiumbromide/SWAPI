---
title: "Body::AddProfileBspline"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__AddProfileBspline.htm"
---

# Body::AddProfileBspline

This method is obsolete and has been superseded by [Body2::AddProfileBspline](sldworksAPI.chm::/Body2/Body2__AddProfileBspline.htm).

Description

This method creates an B-spline profile curve and returns a pointer to that curve.

Syntax (OLE Automation)

retval = Body.AddProfileBspline ( props, knots, ctrlPtCoords )

| Input: | (VARIANT) props | Contains 4 integers packed into 2 double elements (see below) |
| --- | --- | --- |
| Input: | (VARIANT) knots | VARIANT of type SafeArray of numKnots doubles (see below) |
| Input: | (VARIANT) ctrlPtCoords | VARIANT of type SafeArray of numCtrlPtCoord doubles (see below) |
| Return: | (LPDISPATCH) retval | Pointer to dispatch object, the B-spline profile curve |

Syntax (COM)

status = Body->IAddProfileBsplineDLL ( props, knots, ctrlPtCoords, &retval )

| Input: | (long*) props | Contains 4 longs (see below) |
| --- | --- | --- |
| Input: | (double*) knots | Pointer to an array of numKnots doubles (see below) |
| Input: | (double*) ctrlPtCoords | Pointer to an array of numCtrlPtCoord doubles (see below) |
| Output: | (LPCURVE) retval | Pointer to the B-spline profile curve |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can use this method in conjunction with Body::CreateRevolutionSurface to generate any surface of revolution, or with Body::CreateExtrusionSurface to generate a tabulated cylinder.

The props argument contains the following values:

- DimensionControlPoints
- Order
- NumCtrlPoints
- Periodicity

The length of the knots array is given by:

```vb
numKnots = NumCtrlPoints + Order
```

The length of the CtrlPtCoords is given by:

```vb
numCtrlPtCoord = NumCtrlPoints * DimensionControlPoints
```
