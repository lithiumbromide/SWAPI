---
title: "Sketch::GetArcs"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__GetArcs.htm"
---

# Sketch::GetArcs

This method is obsolete and has been superseded by [Sketch::GetArcs2](sldworksAPI.chm::/Sketch/Sketch__GetArcs2.htm).

Description

This method returns all of the arcs in this sketch.

Syntax (OLE Automation)

retval = Sketch.GetArcs ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of arc information |
| --- | --- | --- |

Syntax (COM)

status = Sketch->IGetArcs ( retval )

| Output: | (double*) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

See Sketch::GetSketchSegments or Sketch::IEnumSketchSegments for access to individual SketchSegment and SketchArc objects.

Return value is an array of doubles with the format:

[ LineType, StartPt[3], EndPt[3], CenterPt[3], RotDir, ... ]

where:

| LineType | Line type as defined in swLineTypes_e. A lineType is a combination of a lineStyle and lineWeight. |
| --- | --- |
| StartPt[3] | Array of 3 doubles (X,Y,Z) describing the arc start point. |
| EndPt[3] | Array of 3 doubles (X,Y,Z) describing the arc end point. If the arc is closed, then this will be the same point as the StartPt. |
| CenterPt[3] | Array of 3 doubles (X,Y,Z) describing the center point. |
| RotDir | Rotational direction (CW = -1, CCW = 1). |

This set of data repeats for each arc in the sketch. The size of the array is (NumArcs * 11). To determine the number of arcs, see Sketch::GetArcCount.
