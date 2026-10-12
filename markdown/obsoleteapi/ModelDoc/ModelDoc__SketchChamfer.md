---
title: "ModelDoc::SketchChamfer"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchChamfer.htm"
---

# ModelDoc::SketchChamfer

This method is obsolete and has been superseded by [ModelDoc2::SketchChamfer](../ModelDoc2/ModelDoc2__SketchChamfer.htm).

Description

This method creates a chamfer between two selected sketch entities.

Syntax (OLE Automation)

void ModelDoc.SketchChamfer ( angleORdist, dist1, options)

| Input: | (double) angleORdist | Angle of the chamfer if using the angle-distance option or the distance of the second distance if using the distance-distance option |
| --- | --- | --- |
| Input: | (double) dist1 | Distance of the chamfer |
| Input: | (long) options | 0 = angle–distance chamfer 1 = distance–distance chamfer |

Syntax (COM)

status = ModelDoc->SketchChamfer ( angleORdist, dist1, options )

| Input: | (double) angleORdist | Angle of the chamfer if using the angle-distance option or the distance of the second distance if using the distance-distance option |
| --- | --- | --- |
| Input: | (double) dist1 | Distance of the chamfer |
| Input: | (long) options | 0 = angle–distance chamfer 1 = distance–distance chamfer |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
