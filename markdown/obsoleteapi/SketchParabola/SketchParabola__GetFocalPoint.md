---
title: "SketchParabola::GetFocalPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchParabola/SketchParabola__GetFocalPoint.htm"
---

# SketchParabola::GetFocalPoint

This method is obsolete and has been superseded by [SketchParabola::GetFocalPoint2](sldworksAPI.chm::/SketchParabola/SketchParabola__GetFocalPoint2.htm).

Description

This method gets the focal point used to define this sketch parabola.

Syntax (OLE Automation)

retval = SketchParabola.GetFocalPoint ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z), the parabola focal point |
| --- | --- | --- |

Syntax (COM)

status = SketchParabola->IGetFocalPoint ( retval )

| Output: | (double*) retval | Pointer to an array of 3 doubles (x,y,z), the parabola focal point |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
