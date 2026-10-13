---
title: "SketchEllipse::GetEndPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchEllipse/SketchEllipse__GetEndPoint.htm"
---

# SketchEllipse::GetEndPoint

This method is obsolete and has been superseded by [SketchEllipse::GetEndPoint2](sldworksAPI.chm::/SketchEllipse/SketchEllipse__GetEndPoint2.htm).

Description

This method gets the end point of this sketch ellipse.

Syntax (OLE Automation)

retval = SketchEllipse.GetEndPoint ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z), the ellipse end point |
| --- | --- | --- |

Syntax (COM)

status = SketchEllipse->IGetEndPoint ( retval )

| Output: | (double*) retval | Pointer to an array of 3 doubles (x,y,z), the ellipse end point |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
