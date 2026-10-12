---
title: "VariableFilletFeatureData2::GetRadius"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/VariableFilletFeatureData2/VariableFilletFeatureData2__GetRadius.htm"
---

# VariableFilletFeatureData2::GetRadius

This method is obsolete and has been superseded by [VariableFilletFeatureData2::GetRadius2](sldworksAPI.chm::/VariableFilletFeatureData2/VariableFilletFeatureData2__GetRadius2.htm).

Description

This method gets the radius value for specified fillet item.

Syntax (OLE Automation)

radius = VariableFilletFeatureData2.GetRadius ( pVertex )

| Input: | (LPDISPATCH) pVertex | Vertex at which the radius value is desired |
| --- | --- | --- |
| Return: | ( double ) radius | Radius value |

Syntax (COM)

status = VariableFilletFeatureData2->IGetRadius ( pVertex, &radius )

| Input: | (LPVERTEX) pVertex | Vertex at which the radius value is desired |
| --- | --- | --- |
| Output: | (double) radius | Radius value |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See Accessing Selections that Define Features for details on using this method.
