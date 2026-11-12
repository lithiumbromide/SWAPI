---
title: "CustomSymbol::GetTextHeightAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetTextHeightAtIndex.htm"
---

# CustomSymbol::GetTextHeightAtIndex

This method is obsolete and has been superseded by [Note::GetTextHeightAtIndex](sldworksAPI.chm::/Note/Note__GetTextHeightAtIndex.htm).

Description

This method gets the text height for the specified piece of text in this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetTextHeightAtIndex ( index)

| Input: | (long) index | Index of the text where the index begins at zero |
| --- | --- | --- |
| Return: | (double) retval | Text height for the specified text in meters |

Syntax (COM)

status = CustomSymbol->GetTextHeightAtIndex ( index, &retval )

| Input: | (long) index | Index of the text where the index begins at zero |
| --- | --- | --- |
| Output: | (double) retval | Text height for the specified text in meters |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
