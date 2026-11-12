---
title: "ChamferFeatureData::GetVertexChamferDistance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ChamferFeatureData/ChamferFeatureData__GetVertexChamferDistance.htm"
---

# ChamferFeatureData::GetVertexChamferDistance

This method is obsolete and has been superseded by [ChamferFeatureData2::GetVertexChamferDistance](sldworksAPI.chm::/ChamferFeatureData2/ChamferFeatureData2__GetVertexChamferDistance.htm).

Description

This method gets the vertex chamfer distance.

Syntax (OLE Automation)

distance = ChamferFeatureData.GetVertexChamferDistance ( side )

| Input: | (int) side | Feature direction, set to a value between 0 and 1 |
| --- | --- | --- |
| Return: | (double) distance | Vertex chamfer distance |

Syntax (COM)

status = ChamferFeatureData ->GetVertexChamferDistance ( side, &distance )

| Input: | (int) side | Feature direction, set to a value between 0 and 1 |
| --- | --- | --- |
| Output: | (double) distance | Vertex chamfer distance |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Relevant only for vertex-type chamfers.
