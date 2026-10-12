---
title: "CustomSymbol::GetArcAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetArcAtIndex.htm"
---

# CustomSymbol::GetArcAtIndex

This method are obsolete and has been superseded by [Note::GetArcAtIndex](sldworksAPI.chm::/Note/Note__GetArcAtIndex.htm).

Description

This method gets information for the specified arc.

Syntax (OLE Automation)

retval = CustomSymbol.GetArcAtIndex ( index)

| Input: | (long) index | Index of the desired arc where the index begins at 0 |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles (see Remarks ) |

Syntax (COM)

status = CustomSymbol->IGetArcAtIndex ( index, retval )

| Input: | (long) index | Index of the desired arc where the index begins at 0 |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles (see Remarks ) |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3], centerPt[3], rotationDir ]

where:

| lineType | Line type as defined in swLineTypes_e |
| --- | --- |
| startPt [3] | XYZ arc start point |
| endPt [3] | XYZ arc end point |
| centerPt [3] | XYZ arc center point |
| rotationDir | Boolean returned as a double and represents the rotation direction, where CCW = TRUE and CW = FALSE |
