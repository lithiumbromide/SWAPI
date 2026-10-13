---
title: "Note::GetTextPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Note/Note__GetTextPoint.htm"
---

# Note::GetTextPoint

This method is obsolete and has been superseded by [Note::GetTextPoint2](sldworksAPI.chm::/Note/Note__GetTextPoint2.htm).

Description

This method returns the note's text reference point (the note origin). This is the upper-left corner of the bounding rectangle.

Syntax (OLE Automation)

retval = Note.GetTextPoint ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Note->IGetTextPoint ( retval )

| Output: | (double*) retval | Pointer to array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Format of return information is the following array of doubles:

- retval[0] = x coordinate of text reference point
- retval[1] = y coordinate of text reference point
- retval[2] = z coordinate of text reference point
