---
title: "DisplayData::GetLineAtIndex2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayData/DisplayData__GetLineAtIndex2.htm"
---

# DisplayData::GetLineAtIndex2

This method is obsolete and has been superseded by [DisplayData::GetLineAtIndex3](sldworksAPI.chm::/DisplayData/DisplayData__GetLineAtIndex3.htm).

Description

This method gets information for the specified line.

Syntax (OLE Automation)

retval = DisplayData.GetLineAtIndex2 ( index)

| Input: | (long) index | Index of the desired line where the index begins at zero |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles (see Remarks ) |

Syntax (COM)

status = DisplayData->IGetLineAtIndex2 ( index, retval )

| Input: | (long) index | Index of the desired line where the index begins at zero |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles:

```vb
[ color, lineType, Unused, Unused, startPt[3], endPt[3] ]
```

where:

| color | COLORREF returned as an integer; return value can be 0 or -1 for default color |
| --- | --- |
| lineType | Line type as defined in swLineTypes_e |
| startPt[3] | x, y, z line start point |
| endPt[3] | x, y, z line end point |
