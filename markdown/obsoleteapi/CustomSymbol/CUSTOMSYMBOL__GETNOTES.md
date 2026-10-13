---
title: "CustomSymbol::GetNotes"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CUSTOMSYMBOL__GETNOTES.HTM"
---

# CustomSymbol::GetNotes

This method is obsolete and has been superseded by [BlockDefinition::GetNotes](../BlockDefinition/BlockDefinition__GetNotes.htm).

Description

This method gets the notes that are part of this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetNotes ( )

| Output: | (VARIANT) retval | Notes in this custom symbol |
| --- | --- | --- |

Syntax (COM)

status = CustomSymbol->IGetNotes ( Count, retval )

| Input: | (long) Count | Number of notes in this custom symbol |
| --- | --- | --- |
| Output: | (LPNOTE*) retval | Array of size Count |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
