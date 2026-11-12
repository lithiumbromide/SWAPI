---
title: "Sketch::GetUserPoints"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__GetUserPoints.htm"
---

# Sketch::GetUserPoints

This method is obsolete and has been superseded by [Sketch::GetUserPoints2](sldworksAPI.chm::/Sketch/Sketch__GetUserPoints2.htm).

Description

This method returns all of the user points in this sketch.

Syntax (OLE Automation)

retval = Sketch.GetUserPoints ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = Sketch->IGetUserPoints ( retval )

| Output: | (double*) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

See Sketch::GetSketchPoints or Sketch::IEnumSketchPoints for access to individual SketchPoint objects.

The return value is an array of 3 doubles with the format:

- 0,1,2 XYZ of first point
- 3,4,5 XYZ of next point
- ...

size = Number of Points * 3

To determine the number of points in the sketch, see Sketch::GetUserPointsCount.

The data returned from this method is in terms of sketch space. If you want the data in terms of model space, then you should combine this data with the transform property Sketch::ModelToSketchXform.
