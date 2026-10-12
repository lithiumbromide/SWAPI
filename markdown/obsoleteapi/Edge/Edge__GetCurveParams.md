---
title: "Edge::GetCurveParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Edge/Edge__GetCurveParams.htm"
---

# Edge::GetCurveParams

This method is obsolete and has been superseded by [Edge::GetCurveParams2](sldworksAPI.chm::/Edge/Edge__GetCurveParams2.htm).

Description

This function returns the parameterization of the edge.

Syntax (OLE Automation)

retval = Edge.GetCurveParams ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray describing the parameterization of the edge |
| --- | --- | --- |

Syntax (COM)

status = Edge->IGetCurveParams ( &retval )

| Output: | (double*) retval | Pointer to an array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You must precede calls to this by a call to Edge::GetCurve because SolidWorks does not keep the underlying curve information. Edge::GetCurve generates this information and you can extract the curve parameters.

You can use the data returned by this method to determine if a circular edge is a complete circle or an arc.

The return value is the following array of 10 doubles:

```vb
[ StartPtX, StartPtY, StartPtZ, EndPtX, EndPtY, EndPtZ, StartUParam, EndUParam, PackDouble1, PackDouble2 ]
```

where PackDouble1 and PackDouble2 are each a set of two integers packed into a double. They hold the following pair of integers:

| PackDouble1 | Two packed integers: Unused curveType as documented in Curve::Identity |
| --- | --- |
| PackDouble2 | Two packed integers: Unused curveTag |

If the curve is closed and it starts and ends at the same point, then StartUParam and EndUParam are a period apart.
