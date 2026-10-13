---
title: "ModelDoc::CreateCircleByRadius"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateCircleByRadius.htm"
---

# ModelDoc::CreateCircleByRadius

This method is obsolete and has been superseded by [ModelDoc::CreateCircleByRadius2](ModelDoc__CreateCircleByRadius2.htm).

Description

This method creates a circle with P1 as the center point and with radius as the radius.

Syntax (OLE Automation)

retval = ModelDoc.CreateCircleByRadius ( P1, radius)

| Input: | (VARIANT) P1 | VARIANT of type SafeArray of 3 doubles (x1,y1, z1) in meters that describe the center point of the arc |
| --- | --- | --- |
| Input: | (double) radius | Radius of circle in meters |
| Return: | (BOOL) retval | TRUE if success, FALSE if fail |

Syntax (COM)

status = ModelDoc->ICreateCircleByRadius ( P1, radius )

| Input: | (double*) P1 | Pointer to an array of 3 doubles (x1,y1, z1) in meters that describe the center point of the arc. |
| --- | --- | --- |
| Input: | (double) radius | Radius of circle in meters |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
