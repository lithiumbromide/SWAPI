---
title: "CustomSymbol::GetText"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetText.htm"
---

# CustomSymbol::GetText

This method is obsolete and has been superseded by [CustomSymbol::GetNotesCount](CUSTOMSYMBOL__GETNOTECOUNT.HTM) and [CustomSymbol::GetNotes](CUSTOMSYMBOL__GETNOTES.HTM).

Description

This method gets one of the text strings in this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetText ( index )

| Input: | (long) index | 0-based index into the array of strings in this custom symbol |
| --- | --- | --- |
| Return: | (BSTR) retval | Text string |

Syntax (COM)

status = CustomSymbol->GetText ( index, &retval )

| Input: | (long) index | 0-based index into the array of strings in this custom symbol |
| --- | --- | --- |
| Output: | (BSTR) retval | Text string |
| Return: | (HRESULT) retval | S_OK if successful |

Remarks
