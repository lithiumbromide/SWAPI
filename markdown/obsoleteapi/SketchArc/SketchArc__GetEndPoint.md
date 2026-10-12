---
title: "SketchArc::GetEndPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchArc/SketchArc__GetEndPoint.htm"
---

# SketchArc::GetEndPoint

This method is obsolete and has been superseded by [SketchArc::GetEndPoint2](sldworksAPI.chm::/SketchArc/SketchArc__GetEndPoint2.htm).

Description

This method gets the endpoint of this sketch arc.

Syntax (OLE Automation)

retval = SketchArc.GetEndPoint ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 3 doubles (x,y,z), the arc endpoint |
| --- | --- | --- |

Syntax (COM)

status = SketchArc->IGetEndPoint ( retval )

| Output: | (double*) retval | pointer to an array of 3 doubles (x,y,z), the arc endpoint |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
