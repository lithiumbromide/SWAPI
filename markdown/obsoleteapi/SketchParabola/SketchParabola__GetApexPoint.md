---
title: "SketchParabola::GetApexPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchParabola/SketchParabola__GetApexPoint.htm"
---

# SketchParabola::GetApexPoint

This method is obsolete and has been superseded by [SketchParabola::GetApexPoint2](sldworksAPI.chm::/SketchParabola/SketchParabola__GetApexPoint2.htm).

Description

This method get sthe apex point used to define this sketch parabola.

Syntax (OLE Automation)

retval = SketchParabola.GetApexPoint ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z), the parabola apex point |
| --- | --- | --- |

Syntax (COM)

status = SketchParabola->IGetApexPoint ( retval )

| Output: | (double*) retval | Pointer to an array of 3 doubles (x,y,z), the parabola apex point |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This value can be used to allocate your memory for a call to the COM version of SketchSpline::GetPoints.
