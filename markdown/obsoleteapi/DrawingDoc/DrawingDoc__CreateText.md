---
title: "DrawingDoc::CreateText"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateText.htm"
---

# DrawingDoc::CreateText

This method is obsolete and has been superseded by [DrawingDoc::CreateText2](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateText2.htm).

Description

This method inserts text at the specified location in the current drawing.

Syntax (OLE Automation)

retval = DrawingDoc.CreateText ( textString, textX, textY, textZ, textHeight, textAngle)

| Input: | (BSTR) textString | User input text |
| --- | --- | --- |
| Input: | (double) textX | X text location in meters |
| Input: | (double) textY | Y text location in meters |
| Input: | (double) textZ | Z text location in meters |
| Input: | (double) textHeight | Text height in meters |
| Input: | (double) textAngle | Text angle for rotated text (in radians) |
| Return: | (BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = DrawingDoc->CreateText ( textString, textX, textY, textZ, textHeight, textAngle, &retval )

| Input: | (BSTR) textString | User input text |
| --- | --- | --- |
| Input: | (double) textX | X text location in meters |
| Input: | (double) textY | Y text location in meters |
| Input: | (double) textZ | Z text location in meters |
| Input: | (double) textHeight | Text height in meters |
| Input: | (double) textAngle | Text angle for rotated text (in radians) |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The location specifies the position of the upper-left corner of the box containing the text with respect to the lower-left corner of the drawing.
