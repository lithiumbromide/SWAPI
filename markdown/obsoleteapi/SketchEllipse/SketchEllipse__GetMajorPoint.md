---
title: "SketchEllipse::GetMajorPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchEllipse/SketchEllipse__GetMajorPoint.htm"
---

# SketchEllipse::GetMajorPoint

This method is obsolete and has been superseded by [SketchEllipse::GetMajorPoint2](sldworksAPI.chm::/SketchEllipse/SketchEllipse__GetMajorPoint2.htm).

Description

This method gets the major point used to define this sketch ellipse.

Syntax (OLE Automation)

retval = SketchEllipse.GetMajorPoint ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z), the ellipse major sketch point |
| --- | --- | --- |

Syntax (COM)

status = SketchEllipse->IGetMajorPoint ( retval )

| Output: | (double*) retval | Pointer to an array of 3 doubles (x,y,z), the ellipse major sketch point |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
