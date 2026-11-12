---
title: "Note::GetTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Note/Note__GetTextFormat.htm"
---

# Note::GetTextFormat

This method is obsolete and has been superseded by [Annotation::GetTextFormat](sldworksAPI.chm::/Annotation/Annotation__GetTextFormat.htm).

Description

This method gets the TextFormat object for this note.

Syntax (OLE Automation)

retval = Note.GetTextFormat ( )

| Return: | (LPDISPATCH) retval | Dispatch object for the note, the TextFormat object |
| --- | --- | --- |

Syntax (COM)

status = Note->IGetTextFormat ( &retval )

| Output: | (LPTEXTFORMAT) retval | Pointer to the TextFormat object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns the text formatting object for the note. To modify the formatting change the properties, call Note::SetTextFormat.
