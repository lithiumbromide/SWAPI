---
title: "SketchParabola::GetEndPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchParabola/SketchParabola__GetEndPoint.htm"
---

# SketchParabola::GetEndPoint

This method is obsolete and has been superseded by [SketchParabola::GetEndPoint2](sldworksAPI.chm::/SketchParabola/SketchParabola__GetEndPoint2.htm).

Description

This method gets the end point of this sketch parabola.

Syntax (OLE Automation)

retval = SketchParabola.GetEndPoint ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z), the parabola end point |
| --- | --- | --- |

Syntax (COM)

status = SketchParabola->IGetEndPoint ( retval )

| Output: | (double*) retval | Pointer to an array of 3 doubles (x,y,z), the parabola end point |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
