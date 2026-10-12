---
title: "Note::GetTextFormatAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Note/Note__GetTextFormatAtIndex.htm"
---

# Note::GetTextFormatAtIndex

This method is obsolete and has been superseded by [Annotation::GetTextFormat](sldworksAPI.chm::/Annotation/Annotation__GetTextFormat.htm).

Description

This method gets the specified text item's format.

Syntax (OLE Automation)

retval = Note.GetTextFormatAtIndex ( index )

| Input: | (long) index | Index of text item |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the TextFormat object |

Syntax (COM)

status = Note->IGetTextFormatAtIndex ( index, &retval )

| Input: | (long) index | Index of text item |
| --- | --- | --- |
| Output: | (LPTEXTFORMAT) retval | Pointer to TextFormat object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
