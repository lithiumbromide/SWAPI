---
title: "Curve::GetLength2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve__GetLength2.htm"
---

# Curve::GetLength2

This method is obsolete and has been superseded by [Curve::Length3](sldworksAPI.chm::/Curve/Curve__GetLength3.htm).

Description

This method gets the length of a curve between the specified parameters.

Syntax (OLE Automation)

retval = Curve.GetLength2 ( startParam, endParam )

| Input: | (double) startParam | Start parameter |
| --- | --- | --- |
| Input: | (double) endParam | End parameter |
| Output: | (double) retval | Length of the curve between the two parameters |

Syntax (COM)

status = Curve->GetLength2 ( startParam, endParam, &retval )

| Input: | (double) startParam | Start parameter |
| --- | --- | --- |
| Input: | (double) endParam | End parameter |
| Output: | (double) retval | Length of the curve between the two parameters |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
