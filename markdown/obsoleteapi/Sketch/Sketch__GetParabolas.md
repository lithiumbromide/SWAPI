---
title: "Sketch::GetParabolas"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__GetParabolas.htm"
---

# Sketch::GetParabolas

This method is obsolete and has been superseded by [Sketch::GetParabolas2](sldworksAPI.chm::/Sketch/Sketch__GetParabolas2.htm).

Description

This method gets all of the parabolas in the sketch.

Syntax (OLE Automation)

retval = Sketch.GetParabolas ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray (See Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Sketch->IGetParabolas ( &retval )

| Output: | (double) retval | Pointer to an array of doubles (See Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See Sketch::GetSketchSegments or Sketch::IEnumSketchSegments for access to individual SketchSegment and SketchParabola objects.

The return values are in an array of doubles:

[ Unused, LineType, Unused, Unused, StartPt[3], EndPt[3], FocusPt[3], ApexPt[3] ... ]

where:

| Unused : | This return value is unused and is returned as 0. |
| --- | --- |
| LineType : | Line type. Valid returns are defined in swLineTypes_e. A lineType is a combination of a lineStyle and lineWeight. |
| Unused : | This return value is unused and is returned as 0. |
| Unused : | This return value is unused and is returned as 0. |
| StartPt[3] : | Array of 3 doubles (X,Y,Z) describing the parabola start point |
| EndPt[3] : | Array of 3 doubles (X,Y,Z) describing the parabola end point. |
| FocusPt[3] : | Array of 3 doubles (X,Y,Z) describing the parabola focus point. |
| ApexPt[3] : | Array of 3 doubles (X,Y,Z) describing the parabola apex point. |

This set of data repeats for each parabola in the sketch. The size of the array is (NumParabolas * 16). To determine the number of parabolas, see Sketch::GetParabolaCount.
