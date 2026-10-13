---
title: "Sketch::GetLines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__GetLines.htm"
---

# Sketch::GetLines

This method is obsolete and has been superseded by [Sketch::GetLines2](sldworksAPI.chm::/Sketch/Sketch__GetLines2.htm).

Description

This method returns information about each line in this sketch.

Syntax (OLE Automation)

retval = Sketch.GetLines ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = Sketch->IGetLines ( retval )

| Output: | (double*) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[ LineType, StartPtX, StartPtY, StartPtZ, EndPtX, EndPtY, EndPtZ, ... ]

where this array of 7 values repeats itself for each line in the sketch. The number of doubles returned is (lineCount * 7). To determine the number of lines in the sketch, see Sketch::GetLineCount.

LineStyle may take one of the values in swLineTypes_e.

See Sketch::GetSketchSegments or Sketch::IEnumSketchSegments for access to individual SketchSegment and SketchLine objects.
