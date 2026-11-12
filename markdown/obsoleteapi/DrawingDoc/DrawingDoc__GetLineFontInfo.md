---
title: "DrawingDoc::GetLineFontInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__GetLineFontInfo.htm"
---

# DrawingDoc::GetLineFontInfo

This method is obsolete and has been superseded by [DrawingDoc::GetLineFontInfo2](sldworksAPI.chm::/DrawingDoc/DrawingDoc__GetLineFontInfo2.htm).

Description

This method gets the detailed information about the line font style, including the line weight and segment lengths.

Syntax (OLE Automation)

retval = DrawingDoc.GetLineFontInfo ( index)

| Input: | (long) index | Index position of the line font |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT containing the line font style information |

Syntax (COM)

status = DrawingDoc->GetLineFontInfo ( index, &retval )

| Input: | (long) index | Index position of the Line font. |
| --- | --- | --- |
| Output: | (VARIANT) retval | VARIANT containing the line font style information |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use DrawingDoc::GetLineFontInfo2 to get line font information.

Lines are repeating patterns of space and solid segments. The segCount argument returns the number of segments that define the pattern, and segLengths[] specifies the length of each segment. A negative length value indicates space.

For example:

Solid line: segCount = 1, segLenghts[] = {0.5}

Dashed line: segCount = 2, segLengths[] = {0.25, -0.25}

VARIANT format:

double weight - THIN = 0.0, NORMAL = 1.0, LW_THICK = 2.0

double segCount - Number of segments in the pattern

double segLengths[segCount] - Length of each segment
