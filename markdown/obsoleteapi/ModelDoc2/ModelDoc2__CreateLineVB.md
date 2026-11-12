---
title: "ModelDoc2::CreateLineVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateLineVB.htm"
---

# ModelDoc2::CreateLineVB

This method is obsolete and has been superseded by [ModelDoc2::CreateLine2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateLine2.htm).

Description

This method creates a line from P1 to P2. This method is provided for use in Visual Basic and other forms of Basic that do not support SafeArrays. This method also enables automatic relations for the line, which may not be suitable for creating very small segments in database.

Syntax (OLE Automation)

void ModelDoc2.CreateLineVB ( x1, y1, z1, x2, y2, z2)

| Input: | (double) x1 | Start point X in meters |
| --- | --- | --- |
| Input: | (double) y1 | Start point Y in meters |
| Input: | (double) z1 | Start point Z in meters |
| Input: | (double) x2 | End point X in meters |
| Input: | (double) y2 | End point Y in meters |
| Input: | (double) z2 | End point Z in meters |

Syntax (COM)

status = ModelDoc2->CreateLineVB ( x1, y1, z1, x2, y2, z2 )

| Input: | (double) x1 | Start point X in meters |
| --- | --- | --- |
| Input: | (double) y1 | Start point Y in meters |
| Input: | (double) z1 | Start point Z in meters |
| Input: | (double) x2 | End point X in meters |
| Input: | (double) y2 | End point Y in meters |
| Input: | (double) z2 | End point Z in meters |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
