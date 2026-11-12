---
title: "DisplayData::GetArcAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayData/DisplayData__GetArcAtIndex.htm"
---

# DisplayData::GetArcAtIndex

This method is obsolete and has been superseded by [DisplayData::GetArcAtIndex2](sldworksAPI.chm::/DisplayData/DisplayData__GetArcAtIndex2.htm).

Description

This method gets information for the specified arc.

Syntax (OLE Automation)

retval = DisplayData.GetArcAtIndex ( index)

| Input: | (long) index | Index of the desired arc where the index begins at zero |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles (see below) |

Syntax (COM)

status = DisplayData->IGetArcAtIndex ( index, retval )

| Input: | (long) index | Index of the desired arc where the index begins at zero |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles (see below) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3], centerPt[3], rotationDir ]

| lineType | Line type as defined in swLineTypes_e |
| --- | --- |
| startPt [3] | XYZ arc start point |
| endPt [3] | XYZ arc end point |
| centerPt [3] | XYZ arc center point |
| rotationDir | Boolean returned as a double and represents the rotation direction, where CCW = TRUE and CW = FALSE |
