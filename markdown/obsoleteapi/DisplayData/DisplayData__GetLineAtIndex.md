---
title: "DisplayData::GetLineAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayData/DisplayData__GetLineAtIndex.htm"
---

# DisplayData::GetLineAtIndex

This method is obsolete and has been superseded by [DisplayData:GetLineAtIndex2](DisplayData__GetLineAtIndex2.htm).

Description

This method gets information for the specified line.

Syntax (OLE Automation)

retval = DisplayData.GetLineAtIndex ( index)

| Input: | (long) index | Index of the desired line where the index begins at zero |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles (see below) |

Syntax (COM)

status = DisplayData->IGetLineAtIndex ( index, retval )

| Input: | (long) index | Index of the desired line where the index begins at zero |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles (see below) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles :

```vb
[ lineType, startPt[3], endPt[3] ]
```

where

| lineType | Line type as defined in swLineTypes_e |
| --- | --- |
| startPt [3] | XYZ line start point |
| endPt [3] | XYZ line end point |
