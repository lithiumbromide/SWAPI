---
title: "DisplayData::GetEllipseAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayData/DisplayData__GetEllipseAtIndex.htm"
---

# DisplayData::GetEllipseAtIndex

This method is obsolete and has been superseded by [DisplayData:GetEllipseAtIndex2](sldworksAPI.chm::/DisplayData/DisplayData__GetEllipseAtIndex2.htm).

Description

This method gets information for the specified ellipse.

Syntax (OLE Automation)

retval = DisplayData.GetEllipseAtIndex ( index)

| Input: | (long) index | Index of the desired ellipse where the index begins at zero |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles (see below) |

Syntax (COM)

status = DisplayData->IGetEllipseAtIndex ( index, retval )

| Input: | (long) index | Index of the desired ellipse where the index begins at zero |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles (see below) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles :

```vb
[ LineType, StartPt[3], EndPt[3], CenterPt[3], MajorPt[3], MinorPt[3], ... ]
```

| LineType | Line type. Valid returns are found in the swLineTypes_e. |
| --- | --- |
| StartPt [3] | Array of 3 doubles (X,Y,Z) describing the ellipse start point. |
| EndPt [3] | Array of 3 doubles (X,Y,Z) describing the ellipse end point. If the ellipse is closed, this is the same point as StartPt. |
| CenterPt [3] | Array of 3 doubles (X,Y,Z) describing the ellipse center point. |
| MajorPt [3] | Array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the major axis. |
| MinorPt [3] | Array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the minor axis. |
