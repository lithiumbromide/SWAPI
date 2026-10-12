---
title: "Edge::Evaluate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Edge/Edge__Evaluate.htm"
---

# Edge::Evaluate

This method is obsolete and has been superseded by [Edge::Evaluate2](sldworksAPI.chm::/Edge/Edge__Evaluate2.htm).

Description

This method evaluates the edge at the specified parameter.

Syntax (OLE Automation)

retval = Edge.Evaluate ( Parameter)

| Input: | (double) Parameter | Value of the edge parameter |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray values containing the x,y,z value and derivative of the edge (see Remarks ) |

Syntax (COM)

status = Edge->IEvaluate ( Parameter, retval )

| Input: | (double) Parameter | Value of the edge parameter |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use Edge::GetCurveParams2 to determine the valid parameter range for this method.

This OLE implementation of this method returns an array of doubles as follows:

```vb
[ PointX, PointY, PointZ, TangentX, TangentY, TangentZ, Success ]
```

where the point values are in meters and Success is TRUE if successful and FALSE if not.

The return value for the COM implementation is different. To determine success, check the HRESULT return value. The array is as follows:

```vb
[ PointX, PointY, PointZ, TangentX, TangentY, TangentZ ]
```

where the point values are specified in meters.
