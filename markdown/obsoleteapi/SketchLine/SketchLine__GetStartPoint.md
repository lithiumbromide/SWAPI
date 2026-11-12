---
title: "SketchLine::GetStartPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchLine/SketchLine__GetStartPoint.htm"
---

# SketchLine::GetStartPoint

This method is obsolete and has been superseded by [SketchLine::GetStartPoint2](sldworksAPI.chm::/SketchLine/SketchLine__GetStartPoint2.htm).

Description

This method gets the start point of this sketch line.

Syntax (OLE Automation)

retval = SketchLine.GetStartPoint ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z), the line start point |
| --- | --- | --- |

Syntax (COM)

status = SketchLine->IGetStartPoint ( retval )

| Output: | (double*) retval | Pointer to an array of 3 doubles (x,y,z), the line start point |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
