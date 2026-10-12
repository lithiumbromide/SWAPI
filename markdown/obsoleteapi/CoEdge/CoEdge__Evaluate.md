---
title: "CoEdge::Evaluate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CoEdge/CoEdge__Evaluate.htm"
---

# CoEdge::Evaluate

This method is obsolete and has been superseded by [CoEdge::Evaluate2](sldworksAPI.chm::/CoEdge/CoEdge__Evaluate2.htm).

Description

This method gets the (X,Y,Z) location and the tangency vector on the coedge at the specified position.

Syntax (OLE Automation)

retval = CoEdge.Evaluate ( param)

| Input: | (double) param | Curve parameter desired (U value desired for evaluation) |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray (see Remarks ) |

Syntax (COM)

status = CoEdge.IEvaluate ( param, retval )

| Input: | (double) param | Curve parameter desired (U value desired for evaluation) |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles (see Remarks ) |
| Return: | ( HRESULT ) status | S_OK if successful |

Remarks

The tangency vector is defined to be in the direction of the coedge.

The format of the return value is an array of 6 doubles:

- retval[0] x location on the curve
- retval[1] y location on the curve
- retval[2] z location on the curve
- retval[3] x vector describing the tangency at the parameter location on the coedge
- retval[4] y vector describing the tangency at the parameter location on the coedge
- retval[5] z vector describing the tangency at the parameter location on the coedge
- retval[6] TRUE for successful completion, otherwise FALSE
