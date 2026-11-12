---
title: "CustomSymbol::SetText"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__SetText.htm"
---

# CustomSymbol::SetText

This method is obsolete and has been superseded by [CustomSymbol::GetNotesCount](CUSTOMSYMBOL__GETNOTECOUNT.HTM) and [CustomSymbol::GetNotes](CUSTOMSYMBOL__GETNOTES.HTM).

Description

This method sets one of the text strings in this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.SetText ( index, text )

| Input: | (long) index | Zero-based index of the string to be replaced by the text |
| --- | --- | --- |
| Input: | (BSTR) text | Text string |
| Return: | (BOOL) retval | TRUE if text was set successfully, FALSE if not |

Syntax (COM)

status = CustomSymbol->SetText ( index, text, &retval )

| Input: | (long) index | Zero-based index of the string to be replaced by the text |
| --- | --- | --- |
| Input: | (BSTR) text | Text string |
| Output: | (VARIANT_BOOL) retval | TRUE if text was set successfully, FALSE if not |
| Return: | (HRESULT) retval | S_OK if successful |

Remarks
