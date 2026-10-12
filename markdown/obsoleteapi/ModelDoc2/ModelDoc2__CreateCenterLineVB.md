---
title: "ModelDoc2::CreateCenterLineVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateCenterLineVB.htm"
---

# ModelDoc2::CreateCenterLineVB

This method is obsolete and has been superseded by [SketchManager::CreateCenterLine](sldworksAPI.chm::/SketchManager/SketchManager__CreateCenterLine.htm).

Description

This meothd creates a center line from P1 to P2 and can be used in Visual Basic and other forms of Basic that do not support SafeArrays.

Syntax (OLE Automation)

void ModelDoc2.CreateCenterLineVB ( x1, y1, z1, x2, y2, z2)

| Input: | (double) x1 | Location of first end point, in meters |
| --- | --- | --- |
| Input: | (double) y1 | Location of first end point, in meters |
| Input: | (double) z1 | Location of first end point, in meters |
| Input: | (double) x2 | Location of second end point, in meters |
| Input: | (double) y2 | Location of second end point, in meters |
| Input: | (double) z2 | Location of second end point, in meters |

Syntax (COM)

status = ModelDoc2->CreateCenterLineVB ( x1, y1, z1, x2, y2, z2 )

| Input: | (double) x1 | Location of first end point, in meters |
| --- | --- | --- |
| Input: | (double) y1 | Location of first end point, in meters |
| Input: | (double) z1 | Location of first end point, in meters |
| Input: | (double) x2 | Location of second end point, in meters |
| Input: | (double) y2 | Location of second end point, in meters |
| Input: | (double) z2 | Location of second end point, in meters |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can also create centerline construction geometry using ModelDoc2::CreateLine2 and SketchSegment::ConstructionGeometry.
