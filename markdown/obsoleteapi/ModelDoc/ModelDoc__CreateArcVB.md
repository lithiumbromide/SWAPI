---
title: "ModelDoc::CreateArcVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateArcVB.htm"
---

# ModelDoc::CreateArcVB

This method is obsolete and has been superseded by [ModelDoc::CreateArc2](ModelDoc__CreateArc2.htm).

Description

This method creates an arc from P1 as center, from P2 to P3, and may be used in Visual Basic and other forms of Basic that do not support SafeArrays.

Syntax (OLE Automation)

void ModelDoc.CreateArcVB ( p1x, p1y, p1z, p2x, p2y, p2z, p3x, p3y, p3z, dir)

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) p2x | Start point x value in meters |
| Input: | (double) p2y | Start point y value in meters |
| Input: | (double) p2z | Start point z value in meters |
| Input: | (double) p3x | End point x value in meters |
| Input: | (double) p3y | End point y value in meters |
| Input: | (double) p3z | End point z value in meters |
| Input: | (short) dir | Direction of arc ( +1 or -1) |

Syntax (COM)

status = ModelDoc->CreateArcVB ( p1x, p1y, p1z, p2x, p2y, p2z, p3x, p3y, p3z, dir )

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) p2x | Start point x value in meters |
| Input: | (double) p2y | Start point y value in meters |
| Input: | (double) p2z | Start point z value in meters |
| Input: | (double) p3x | End point x value in meters |
| Input: | (double) p3y | End point y value in meters |
| Input: | (double) p3z | Eend point z value in meters |
| Input: | (short) dir | Direction of arc ( +1 or -1) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The ModelDoc::SetAddToDB method increases performance during entity creation by adding entities directly to the SolidWorks database, and it also avoids inferencing.
