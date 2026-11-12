---
title: "SketchArc::GetCenterPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchArc/SketchArc__GetCenterPoint.htm"
---

# SketchArc::GetCenterPoint

This method is obsolete and has been superseded by [SketchArc::GetCenterPoint2](sldworksAPI.chm::/SketchArc/SketchArc__GetCenterPoint2.htm).

Description

This method gets the centerpoint of this sketch arc.

Syntax (OLE Automation)

retval = SketchArc.GetCenterPoint ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z), the arc centerpoint |
| --- | --- | --- |

Syntax (COM)

status = SketchArc->IGetCenterPoint ( retval )

| Output: | (double*) retval | pointer to an array of 3 doubles (x,y,z), the arc centerpoint |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
