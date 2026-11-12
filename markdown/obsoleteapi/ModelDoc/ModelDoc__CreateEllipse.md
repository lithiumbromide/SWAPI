---
title: "ModelDoc::CreateEllipse"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateEllipse.htm"
---

# ModelDoc::CreateEllipse

This method is obsolete and has been superseded by [ModelDoc::CreateEllipse2](ModelDoc__CreateEllipse2.htm).

Description

This method creates an ellipse.

Syntax (OLE Automation)

retval = ModelDoc.CreateEllipse ( center, major, minor)

| Input: | (VARIANT) center | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis. |
| --- | --- | --- |
| Input: | (VARIANT) major | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the major axis |
| Input: | (VARIANT) minor | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis |
| Return: | (BOOL) retval | TRUE if successfully created, FALSE otherwise |

Syntax (COM)

status = ModelDoc->ICreateEllipse ( center, major, minor )

| Input: | (double*) center | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis. |
| --- | --- | --- |
| Input: | (double*) major | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the major axis |
| Input: | (double*) minor | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
