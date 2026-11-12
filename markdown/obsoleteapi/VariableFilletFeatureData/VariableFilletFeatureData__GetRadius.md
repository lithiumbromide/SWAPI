---
title: "VariableFilletFeatureData::GetRadius"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/VariableFilletFeatureData/VariableFilletFeatureData__GetRadius.htm"
---

# VariableFilletFeatureData::GetRadius

This method is obsolete and has been superseded by [VariableFilletFeatureData2::GetRadius](../VariableFilletFeatureData2/VariableFilletFeatureData2__GetRadius.htm).

Description

This method gets the radius value for specified fillet item.

Syntax (OLE Automation)

radius = VariableFilletFeatureData.GetRadius ( pVertex )

| Input: | (LPDISPATCH) pVertex | Vertex at which the radius value is desired |
| --- | --- | --- |
| Return: | ( double ) radius | Radius value |

Syntax (COM)

status = VariableFilletFeatureData->IGetRadius ( pVertex, &radius )

| Input: | (LPVERTEX) pVertex | Vertex at which the radius value is desired |
| --- | --- | --- |
| Output: | (double) radius | Radius value |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
