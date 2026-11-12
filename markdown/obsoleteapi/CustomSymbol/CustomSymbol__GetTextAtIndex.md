---
title: "CustomSymbol::GetTextAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetTextAtIndex.htm"
---

# CustomSymbol::GetTextAtIndex

This method is obsolete and has been superseded by [Note::GetTextAtIndex](sldworksAPI.chm::/Note/Note__GetTextAtIndex.htm).

Description

This method gets the specified text string from this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetTextAtIndex ( index)

| Input: | (long) index | Index of the text where the index begins at zero |
| --- | --- | --- |
| Return: | (BSTR) retval | Text string for the specified text |

Syntax (COM)

status = CustomSymbol->GetTextAtIndex ( index, &retval )

| Input: | (long) index | Index of the text where the index begins at zero |
| --- | --- | --- |
| Output: | (BSTR) retval | Text string for the specified text |
| Return: | (HRESULT) status | S_OK if successful |
