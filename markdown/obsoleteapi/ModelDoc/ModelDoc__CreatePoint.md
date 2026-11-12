---
title: "ModelDoc::CreatePoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePoint.htm"
---

# ModelDoc::CreatePoint

This method is obsolete and has been superseded by [ModelDoc::CreatePoint2](ModelDoc__CreatePoint2.htm).

Description

This method creates a point entity at the specified (x, y, z) location in the current sketch.

Syntax (OLE Automation)

retval = ModelDoc.CreatePoint ( pointX, pointY, pointZ)

| Input: | (double) pointX | x value of point in meters |
| --- | --- | --- |
| Input: | (double) pointY | y value of point in meters |
| Input: | (double) pointZ | z value of point in meters; this value is not recognized; points created in a sketch must be in the particular sketch plane; you should pass in a value of 0.0 for this argument |
| Return: | (BOOL) retval | TRUE if created |

Syntax (COM)

status = ModelDoc->CreatePoint ( pointX, pointY, pointZ, &retval )

| Input: | (double) pointX | x value of point in meters |
| --- | --- | --- |
| Input: | (double) pointY | y value of point in meters |
| Input: | (double) pointZ | z value of point in meters; this value is not recognized; points created in a sketch must be in the particular sketch plane; you should pass in a value of 0.0 for this argument |
| Output: | (VARIANT_BOOL) retval | TRUE if created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
