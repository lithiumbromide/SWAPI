---
title: "Curve::GetLength"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve__GetLength.htm"
---

# Curve::GetLength

This method is obsolete and has been superseded by [Curve::GetLength2](Curve__GetLength2.htm).

Description

This method gets the length of the curve between the specified parameters.

Syntax (OLE Automation)

retval = Curve.GetLength ( startParam, endParam)

| Input: | (double) startParam | Start parameter |
| --- | --- | --- |
| Input: | (double) endParam | End parameter |
| Return: | (double) retval | Curve length between the two parameters |

Syntax (COM)

status = Curve->GetLength ( startParam, endParam, &retval )

| Input: | (double) startParam | Start parameter |
| --- | --- | --- |
| Input: | (double) endParam | End parameter |
| Output: | (double) retval | Curve length between the two parameters |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can use Edge::GetCurve to get the Curve object from the Edge object.

Use [Edge::GetCurveParams](../Edge/Edge__GetCurveParams.htm) to determine the startParam and endParam input for this method.
