---
title: "SketchEllipse::GetStartPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchEllipse/SketchEllipse__GetStartPoint.htm"
---

# SketchEllipse::GetStartPoint

This method is obsolete and has been superseded by [SketchEllipse::GetStartPoint2](sldworksAPI.chm::/SketchEllipse/SketchEllipse__GetStartPoint2.htm).

Description

This method gets the startpoint of this sketch ellipse.

Syntax (OLE Automation)

retval = SketchEllipse.GetStartPoint ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z), the ellipse start sketch point |
| --- | --- | --- |

Syntax (COM)

status = SketchEllipse->IGetStartPoint ( retval )

| Output: | (double*) retval | Pointer to an array of 3 doubles (x,y,z), the ellipse start sketch point |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
