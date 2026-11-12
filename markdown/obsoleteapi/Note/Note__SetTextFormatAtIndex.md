---
title: "Note::SetTextFormatAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Note/Note__SetTextFormatAtIndex.htm"
---

# Note::SetTextFormatAtIndex

This method is obsolete and has been superseded by [Annotation::SetTextFormat](sldworksAPI.chm::/Annotation/Annotation__SetTextFormat.htm).

Description

This method sets the specified text item's format.

Syntax (OLE Automation)

void Note.SetTextFormatAtIndex ( index, textFormat )

| Input: | (long) index | Index position of the text |
| --- | --- | --- |
| Input: | (LPDISPATCH) textFormat | Dispatch pointer to the TextFormat object containing the desired settings |

Syntax (COM)

status = Note->ISetTextFormatAtIndex ( index, textFormat )

| Input: | (long ) index | Index position of the text |
| --- | --- | --- |
| Input: | (LPTEXTFORMAT )textFormat | Pointer to the TextFormat object containing the desired settings |
| Return: | (HRESULT )status | S_OK if successful |

Remarks
