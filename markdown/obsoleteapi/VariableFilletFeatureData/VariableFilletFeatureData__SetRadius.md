---
title: "VariableFilletFeatureData::SetRadius"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/VariableFilletFeatureData/VariableFilletFeatureData__SetRadius.htm"
---

# VariableFilletFeatureData::SetRadius

This method is obsolete and has been superseded by [VariableFilletFeatureData2::SetRadius](sldworksAPI.chm::/VariableFilletFeatureData2/VariableFilletFeatureData2__SetRadius.htm).

Description

This method sets the radius value for specified fillet item.

Syntax (OLE Automation)

void VariableFilletFeatureData.SetRadius ( pVertex, radius )

| Input: | (LPDISPATCH) pVertex | Vertex at which the radius value is desired |
| --- | --- | --- |
| Input: | ( double ) radius | Radius value |

Syntax (COM)

status = VariableFilletFeatureData->ISetRadius ( pVertex, radius )

| Input: | (LPVERTEX) pVertex | Vertex at which the radius value is desired |
| --- | --- | --- |
| Input: | (double) radius | Radius value |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
