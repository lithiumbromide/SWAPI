---
title: "ModelDoc2::SketchChamfer"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchChamfer.htm"
---

# ModelDoc2::SketchChamfer

This method is obsolete and has been superseded by [SketchManager::CreateChamfe](sldworksAPI.chm::/SketchManager/SketchManager__CreateChamfer.htm)r.

Description

This method creates a chamfer between two selected sketch entities.

Syntax (OLE Automation)

void ModelDoc2.SketchChamfer ( angleORdist, dist1, options)

| Input: | (double) angleORdist | Angle of the chamfer if using the Angle-Distance option or the distance of the second distance if using the Distance-Distance option |
| --- | --- | --- |
| Input: | (double) dist1 | D1 Distance of the chamfer |
| Input: | (long) options | 0 = Angle - Distance Chamfer 1 = Distance - Distance Chamfer |

Syntax (COM)

status = ModelDoc2->SketchChamfer ( angleORdist, dist1, options )

| Input: | (double) angleORdist | Angle of the Chamfer if using the Angle-Distance option or the Distance of the second distance if using the Distance-Distance option |
| --- | --- | --- |
| Input: | (double) dist1 | D1 Distance of the chamfer |
| Input: | (long) options | 0 = Angle - Distance Chamfer 1 = Distance - Distance Chamfer |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
