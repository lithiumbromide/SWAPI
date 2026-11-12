---
title: "CustomSymbol::GetTextRefPositionAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetTextRefPositionAtIndex.htm"
---

# CustomSymbol::GetTextRefPositionAtIndex

This method is obsolete and has been superseded by [Note::GetTextRefPositionAtIndex](sldworksAPI.chm::/Note/Note__GetTextRefPositionAtIndex.htm).

Description

This method gets the specified text item reference position in this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetTextRefPositionAtIndex ( index)

| Input: | (long) index | Index of the text where the index begins at 0 |
| --- | --- | --- |
| Return: | (long) retval | Reference position of the specified text item as defined in swTextPosition_e |

Syntax (COM)

status = CustomSymbol->GetTextRefPositionAtIndex ( index, &retval )

| Input: | (long) index | Index of the text where the index begins at 0 |
| --- | --- | --- |
| Output: | (long) retval | Reference position of the specified text item as defined in swTextPosition_e |
| Return: | (HRESULT) status | S_OK if successful |
