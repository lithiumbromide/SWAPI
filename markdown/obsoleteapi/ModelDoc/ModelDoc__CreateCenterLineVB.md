---
title: "ModelDoc::CreateCenterLineVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateCenterLineVB.htm"
---

# ModelDoc::CreateCenterLineVB

This method is obsolete and has been superseded by [ModelDoc2::CreateCenterLineVB](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateCenterLineVB.htm).

Description

This method creates a center line from P1 to P2 and may be used in Visual Basic and other forms of Basic that do not support SafeArrays.

Syntax (OLE Automation)

void ModelDoc.CreateCenterLineVB ( x1, y1, z1, x2, y2, z2)

| Input: | (double) x1 | Location of first end point, in meters |
| --- | --- | --- |
| Input: | (double) y1 | Location of first end point, in meters |
| Input: | (double) z1 | Location of first end point, in meters |
| Input: | (double) x2 | Location of second end point, in meters |
| Input: | (double) y2 | Location of second end point, in meters |
| Input: | (double) z2 | Location of second end point, in meters |

Syntax (COM)

status = ModelDoc->CreateCenterLineVB ( x1, y1, z1, x2, y2, z2 )

| Input: | (double) x1 | Location of first end point, in meters |
| --- | --- | --- |
| Input: | (double) y1 | Location of first end point, in meters |
| Input: | (double) z1 | Location of first end point, in meters |
| Input: | (double) x2 | Location of second end point, in meters |
| Input: | (double) y2 | Location of second end point, in meters |
| Input: | (double) z2 | Location of second end point, in meters |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can also create centerline construction geometry using ModelDoc::CreateLine2 and SketchSegment::ConstructionGeometry.
