---
title: "ModelDoc2::CreateEllipse"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateEllipse.htm"
---

# ModelDoc2::CreateEllipse

This method is obsolete and has been superseded by [ModelDoc2::CreateEllipse2](ModelDoc2__CreateEllipse2.htm).

Description

This method creates an ellipse.

Syntax (OLE Automation)

retval = ModelDoc2.CreateEllipse ( center, major, minor)

| Input: | (VARIANT) center | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis |
| --- | --- | --- |
| Input: | (VARIANT) major | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the major axis |
| Input: | (VARIANT) minor | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis |
| Return: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->ICreateEllipse ( center, major, minor )

| Input: | (double*) center | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis |
| --- | --- | --- |
| Input: | (double*) major | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the major axis |
| Input: | (double*) minor | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
