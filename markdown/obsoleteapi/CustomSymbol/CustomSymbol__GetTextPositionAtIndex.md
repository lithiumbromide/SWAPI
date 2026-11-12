---
title: "CustomSymbol::GetTextPositionAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetTextPositionAtIndex.htm"
---

# CustomSymbol::GetTextPositionAtIndex

This method is obsolete and has been superseded by [Note::GetTextPositionAtIndex](sldworksAPI.chm::/Note/Note__GetTextPositionAtIndex.htm).

Description

This method gets the text item's offset relative to the custom symbol text point.

Syntax (OLE Automation)

retval = CustomSymbol.GetTextPositionAtIndex ( index)

| Input: | (long) index | Index of the text where the index begins at 0 |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles |

Syntax (COM)

status = CustomSymbol->IGetTextPositionAtIndex ( index, retval )

| Input: | (long) index | Index of the text where the index begins at 0 |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[ textPtX, textPtY, textPtZ ]

where the text position values are offset values from the origin of this custom symbol object.
