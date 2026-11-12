---
title: "ChamferFeatureData::SetVertexChamferDistance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ChamferFeatureData/ChamferFeatureData__SetVertexChamferDistance.htm"
---

# ChamferFeatureData::SetVertexChamferDistance

This method is obsolete and has been superseded by [ChamferFeatureData2::SetVertexChamferDistanc](sldworksAPI.chm::/ChamferFeatureData2/ChamferFeatureData2__SetVertexChamferDistance.htm)e.

Description

This method sets the vertex chamfer distance.

Syntax (OLE Automation)

void ChamferFeatureData.SetVertexChamferDistance ( side, distance )

| Input: | (int) side | Feature direction, set to a value between 0 and 1 |
| --- | --- | --- |
| Input: | (double) distance | vertex chamfer distance |

Syntax (COM)

status = ChamferFeatureData ->SetVertexChamferDistance ( side, distance )

| Input: | (int) side | Feature direction, set to a value between 0 and 1 |
| --- | --- | --- |
| Input: | (double) distance | Vertex chamfer distance |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Relevant only for vertex-type chamfers. Currently, only vertex chamfers with three edges are supported.
