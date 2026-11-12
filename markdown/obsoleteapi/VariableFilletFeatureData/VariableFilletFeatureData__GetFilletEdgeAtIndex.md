---
title: "VariableFilletFeatureData::GetFilletEdgeAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/VariableFilletFeatureData/VariableFilletFeatureData__GetFilletEdgeAtIndex.htm"
---

# VariableFilletFeatureData::GetFilletEdgeAtIndex

This method is obsolete and has been superseded by [VariableFilletFeatureData2::GetFilletEdgeAtIndex](sldworksAPI.chm::/VariableFilletFeatureData2/VariableFilletFeatureData2__GetFilletEdgeAtIndex.htm).

Description

This method gets the filleted edge at the specified index.

Syntax (OLE Automation)

pFilletEdge = VariableFilletFeatureData.GetFilletEdgeAtIndex ( index )

| Input: | (int) index | Index at which filleted edge is required |
| --- | --- | --- |
| Return: | (LPDISPATCH) pFilletEdge | Pointer to a dispatch object, the filleted edge or NULL if the operation fails |

Syntax (COM)

status = VariableFilletFeatureData ->IGetFilletEdgeAtIndex ( index, &pFilletEdge )

| Input: | (int) index | Index at which filleted edge is required |
| --- | --- | --- |
| Output: | (LPEDGE) pFilletEdge | Pointer the filleted edge or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
