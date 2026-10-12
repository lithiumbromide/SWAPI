---
title: "ModelDoc::CreateEllipticalArcByCenter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateEllipticalArcByCenter.htm"
---

# ModelDoc::CreateEllipticalArcByCenter

This method is obsolete and has been superseded by [ModelDoc::CreateEllipticalArc2](ModelDoc__CreateEllipticalArc2.htm).

Description

This method creates an elliptical arc trimmed between two points.

Syntax (OLE Automation)

retval = ModelDoc.CreateEllipticalArcByCenter ( center, major, minor, start, end)

| Input: | (VARIANT) center | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe the ellipse center. |
| --- | --- | --- |
| Input: | (VARIANT) major | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the major axis. |
| Input: | (VARIANT) minor | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis. |
| Input: | (VARIANT) start | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe the start point of the ellipse |
| Input: | (VARIANT) end | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe the end point of the ellipse |
| Return: | (BOOL) retval | TRUE if successfully created, FALSE otherwise |

Syntax (COM)

status = ModelDoc->ICreateEllipticalArcByCenter ( center, major, minor, start, end )

| Input: | (double*) center | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe the ellipse center. |
| --- | --- | --- |
| Input: | (double*) major | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the major axis. |
| Input: | (double*) minor | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis. |
| Input: | (double*) start | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe the CCW start point of the ellipse |
| Input: | (double*) end | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe the CCW end point of the ellipse |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Specify the start and end arguments in a counter-clockwise manner.
