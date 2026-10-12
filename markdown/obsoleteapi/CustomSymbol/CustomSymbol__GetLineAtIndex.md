---
title: "CustomSymbol::GetLineAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetLineAtIndex.htm"
---

# CustomSymbol::GetLineAtIndex

This method is obsolete and has been superseded by [Note::GetLineAtIndex](sldworksAPI.chm::/Note/Note__GetLineAtIndex.htm).

Description

This method gets information for the specified line.

Syntax (OLE Automation)

retval = CustomSymbol.GetLineAtIndex ( index)

| Input: | (long) index | Index of the line where the index begins at 0 |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles |

Syntax (COM)

status = CustomSymbol->IGetLineAtIndex ( index, retval )

| Input: | (long) index | Index of the line where the index begins at 0 |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3] ]

lineType = Line type as defined in swLineTypes_e

startPt[3] = XYZ line start point

endPt[3] = XYZ line end point
