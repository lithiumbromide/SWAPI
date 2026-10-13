---
title: "ChamferFeatureData::SetEdgeChamferDistance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ChamferFeatureData/ChamferFeatureData__SetEdgeChamferDistance.htm"
---

# ChamferFeatureData::SetEdgeChamferDistance

This method is obsolete and has been superseded by [ChamferFeatureData2::SetEdgeChamferDistance](sldworksAPI.chm::/ChamferFeatureData2/ChamferFeatureData2__SetEdgeChamferDistance.htm).

Description

This method sets the edge chamfer distance on either side of the edge.

Syntax (OLE Automation)

void ChamferFeatureData.SetEdgeChamferDistance ( side, distance )

| Input: | (int) side | Feature direction, set to 0 or 1; for angle-distance chamfers, set to 0 |
| --- | --- | --- |
| Input: | (double) distance | Edge chamfer distance. |

Syntax (COM)

status = ChamferFeatureData ->SetEdgeChamferDistance ( side, distance )

| Input: | (int) side | Feature direction, set to 0 or 1; for angle-distance chamfers, set to 0 |
| --- | --- | --- |
| Input: | (double) distance | Edge chamfer distance. |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
