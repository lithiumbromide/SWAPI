---
title: "ModelDoc2::CreatePoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePoint.htm"
---

# ModelDoc2::CreatePoint

This method is obsolete and has been superseded by [ModelDoc2::CreatePoint2](ModelDoc2__CreatePoint2.htm).

Description

This method creates a point entity at the specified (x, y, z) location in the current sketch.

Syntax (OLE Automation)

retval = ModelDoc2.CreatePoint ( pointX, pointY, pointZ)

| Input: | (double) pointX | x value of point in meters |
| --- | --- | --- |
| Input: | (double) pointY | y value of point in meters |
| Input: | (double) pointZ | z value of point in meters; this value is not recognized; points created in a sketch must be in the particular sketch plane; you should pass in a value of 0.0 for this argument |
| Return: | (BOOL) retval | TRUE if created, FALSE if not |

Syntax (COM)

status = ModelDoc2->CreatePoint ( pointX, pointY, pointZ, &retval )

| Input: | (double) pointX | x value of point in meters |
| --- | --- | --- |
| Input: | (double) pointY | y value of point in meters |
| Input: | (double) pointZ | z value of point in meters; this value is not recognized; points created in a sketch must be in the particular sketch plane; you should pass in a value of 0.0 for this argument |
| Output: | (VARIANT_BOOL) retval | TRUE if created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
