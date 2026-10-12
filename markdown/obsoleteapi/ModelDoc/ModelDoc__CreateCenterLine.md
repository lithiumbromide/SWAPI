---
title: "ModelDoc::CreateCenterLine"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateCenterLine.htm"
---

# ModelDoc::CreateCenterLine

This method is obsolete and has been superseded by [ModelDoc2::CreateCenterLine](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateCenterLine.htm).

Description

This method creates a center line from P1 to P2. Use ModelDoc::CreateCenterLineVBin Visual Basic and other forms of Basic that do not support SafeArrays.

Syntax (OLE Automation)

retval = ModelDoc.CreateCenterLine ( P1, P2)

| Input: | (VARIANT) P1 | VARIANT of type SafeArrayof 3 doubles(x1, y1, z1) in meters that describe the first point of the line |
| --- | --- | --- |
| Input: | (VARIANT) P2 | VARIANT of type SafeArrayof 3 doubles(x2, y2, z2) in meters that describe the second point of the line |
| Return: | (BOOL) retval | TRUE if success, FALSE if fail |

Syntax (COM)

status = ModelDoc->ICreateCenterLine ( P1, P2 )

| Input: | (double*) P1 | Pointer to an array of 3 doubles (x,y,z) in meters that describe the line start point |
| --- | --- | --- |
| Input: | (double*) P2 | Pointer to an array of 3 doubles (x,y,z) in meters that describe the line start point |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can also create centerline construction geometry using ModelDoc::CreateLine2 and SketchSegment::ConstructionGeometry.
