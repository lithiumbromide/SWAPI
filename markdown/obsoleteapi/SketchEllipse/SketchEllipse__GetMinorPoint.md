---
title: "SketchEllipse::GetMinorPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchEllipse/SketchEllipse__GetMinorPoint.htm"
---

# SketchEllipse::GetMinorPoint

This method is obsolete and has been superseded by [SketchEllipse::GetMinorPoint2](sldworksAPI.chm::/SketchEllipse/SketchEllipse__GetMinorPoint2.htm).

Description

This method gets the minor point used to define this sketch ellipse.

Syntax (OLE Automation)

retval = SketchEllipse.GetMinorPoint ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z), the ellipse minor sketch point |
| --- | --- | --- |

Syntax (COM)

status = SketchEllipse->IGetMinorPoint ( retval )

| Output: | (double*) retval | Pointer to an array of 3 doubles (x,y,z), the ellipse minor sketch point |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
