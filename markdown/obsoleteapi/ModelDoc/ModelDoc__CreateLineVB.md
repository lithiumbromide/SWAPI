---
title: "ModelDoc::CreateLineVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateLineVB.htm"
---

# ModelDoc::CreateLineVB

This method is obsolete and has been superseded by [ModelDoc::CreateLine2](ModelDoc__CreateLine2.htm).

Description

This method:

- Creates a line from P1 to P2
- Provided for use in Visual Basic and other forms of Basic that do not support SafeArrays.
- Enables automatic relations for the line, which may not be suitable for creating very small segments in database.

Syntax (OLE Automation)

void ModelDoc.CreateLineVB ( x1, y1, z1, x2, y2, z2)

| Input: | (double) x1 | Start Point X, in meters |
| --- | --- | --- |
| Input: | (double) y1 | Start Point Y, in meters |
| Input: | (double) z1 | Start Point Z, in meters |
| Input: | (double) x2 | End Point X, in meters |
| Input: | (double) y2 | End Point Y, in meters |
| Input: | (double) z2 | End Point Z, in meters |

Syntax (COM)

status = ModelDoc->CreateLineVB ( x1, y1, z1, x2, y2, z2 )

| Input: | (double) x1 | Start Point X, in meters |
| --- | --- | --- |
| Input: | (double) y1 | Start Point Y, in meters |
| Input: | (double) z1 | Start Point Z, in meters |
| Input: | (double) x2 | End Point X, in meters |
| Input: | (double) y2 | End Point Y, in meters |
| Input: | (double) z2 | End Point Z, in meters |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
