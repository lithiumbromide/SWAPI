---
title: "DisplayData::GetPolyLineAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayData/DisplayData__GetPolyLineAtIndex.htm"
---

# DisplayData::GetPolyLineAtIndex

This method is obsolete and has been superseded by [DisplayData::GetPolyLineAtIndex2](sldworksAPI.chm::/DisplayData/DisplayData__GetPolylineAtIndex2.htm).

Description

This method gets the number of polylines in this display item.

Syntax (OLE Automation)

retval = DisplayData.GetPolyLineAtIndex ( index )

| Input: | (long) index | Index of the desired line where the index begins at zero |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles (see below) |

Syntax (COM)

status = DisplayData->GetPolyLineAtIndex ( index, retval )

| Input: | (long) index | Index of the desired line where the index begins at zero |
| --- | --- | --- |
| Output: | (double*) retval | Array of doubles (see below) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Format of return values is an array of doubles with the format:

```vb
[ Color, LineType, Unused, Unused, NumPolyPoints, [x,y,z] ]
```

where the [x,y,z] parameter is an array of NumPolyPoints and LineType is the line type as defined in swLineTypes_e.

Use [DisplayData::GetPolyLineSizeAtIndex](DisplayData__GetPolyLineSizeAtIndex.htm) to determine the number of elements returned in this array.
