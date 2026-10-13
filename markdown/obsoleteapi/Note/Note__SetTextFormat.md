---
title: "Note::SetTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Note/Note__SetTextFormat.htm"
---

# Note::SetTextFormat

This method is obsolete and has been superseded by [Annotation::SetTextFormat](sldworksAPI.chm::/Annotation/Annotation__SetTextFormat.htm).

Description

This method sets the text format parameters.

Syntax (OLE Automation)

retval = Note.SetTextFormat ( useDocFormat, textFormat )

| Input: | (long) useDocFormat | Controls whether the note uses the documents text format or the textFormat argument values |
| --- | --- | --- |
| Input: | (LPDISPATCH) textFormat | Formatting values (see Remarks ) |
| Return: | (BOOL) retval | TRUE if successfully set, FALSE if not |

Syntax (COM)

status = Note->ISetTextFormat ( useDocFormat, textFormat, &retval )

| Input: | (long) useDocFormat | Controls whether the note uses the documents text format or the textFormat argument values |
| --- | --- | --- |
| Input: | (LPTEXTFORMAT) textFormat | Formatting values (see Remarks ) |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully set, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The note's text format is set to the document's text format if useDocFormat is 1 or to the format specified in the textFormat argument if useDocFormat is 0.
