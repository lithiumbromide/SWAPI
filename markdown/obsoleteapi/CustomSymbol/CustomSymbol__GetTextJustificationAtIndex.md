---
title: "CustomSymbol::GetTextJustificationAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetTextJustificationAtIndex.htm"
---

# CustomSymbol::GetTextJustificationAtIndex

This method is obsolete and has been superseded by [Note::GetTextJustificationAtIndex](sldworksAPI.chm::/Note/Note__GetTextJustificationAtIndex.htm).

Description

This method gets the justification of the specified text item.

Syntax (OLE Automation)

retval = CustomSymbol.GetTextJustificationAtIndex ( index )

| Input: | (long) index | One-based index position of the text |
| --- | --- | --- |
| Return: | (long) retval | Justification of the text as defined in swTextJustification_e |

Syntax (COM)

status = CustomSymbol->GetTextJustificationAtIndex ( index, &retval )

| Input: | (long) index | One-based index position of the text |
| --- | --- | --- |
| Output: | (long) retval | Justification of the text as defined in swTextJustification_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
