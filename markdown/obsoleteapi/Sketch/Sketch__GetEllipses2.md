---
title: "Sketch::GetEllipses2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__GetEllipses2.htm"
---

# Sketch::GetEllipses2

This method is obsolete and has been superseded by [Sketch::GetEllipses3](sldworksAPI.chm::/Sketch/Sketch__GetEllipses3.htm).

Description

This method gets all of the ellipses in the sketch.

Syntax (OLE Automation)

retval = Sketch.GetEllipses2 ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Sketch->IGetEllipses2 ( &retval )

| Output: | (double) retval | Pointer to an array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

See Sketch::GetSketchSegments or Sketch::IEnumSketchSegments for access to individual SketchSegment and SketchEllipse objects.

The return values are in an array of doubles:

[ Unused, LineType, Unused, Unused, StartPt[3], EndPt[3], CenterPt[3], MajorPt[3], MinorPt[3],Direction ... ]

where:

| Unused : | This return value is unused,and is returned as 0. |
| --- | --- |
| LineType : | Line type. Valid returns are defined in swLineTypes_e. A lineType is a combination of a lineStyle and lineWeight. |
| Unused : | This return value is unused and is returned as 0. |
| Unused : | This return value is unused and is returned as 0. |
| StartPt[3] : | An array of 3 doubles (X,Y,Z) describing the ellipse start point |
| EndPt[3] : | An array of 3 doubles (X,Y,Z) describing the ellipse end point. If the ellipse is closed, then this will be the same point as the StartPt. |
| CenterPt[3] : | An array of 3 doubles (X,Y,Z) describing the ellipse center point. |
| MajorPt[3] : | An array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the major axis. |
| MinorPt[3] : | An array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the minor axis. |
| Direction : | -1 for clockwise, +1 for counter-clockwise. |

This set of data repeats for each ellipse in the sketch. The size of the array is (NumEllipses * 20). To determine the number of ellipses, see Sketch::GetEllipseCount.
