---
title: "CustomSymbol::GetTextInvertAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetTextInvertAtIndex.htm"
---

# CustomSymbol::GetTextInvertAtIndex

This method is obsolete and has been superseded by [Note::GetTextInvertAtIndex](sldworksAPI.chm::/Note/Note__GetTextInvertAtIndex.htm).

Description

This method gets the specified text item's invert flag. The invert flag specifies whether the text has been mirrored (reflected) about the X axis. Any reflection is applied after text rotation.

Syntax (OLE Automation)

retval = CustomSymbol.GetTextInvertAtIndex ( index)

| Input: | (long) index | Index of the text where the index begins at zero |
| --- | --- | --- |
| Return: | (long) retval | Text item invert flag |

Syntax (COM)

status = CustomSymbol->GetTextInvertAtIndex ( index, &retval )

| Input: | (long) index | Index of the text where the index begins at zero |
| --- | --- | --- |
| Output: | (long) retval | Text item invert flag |
| Return: | (HRESULT) status | S_OK if successful |
