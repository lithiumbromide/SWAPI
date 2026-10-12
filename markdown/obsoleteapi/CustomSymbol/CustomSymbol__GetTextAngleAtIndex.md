---
title: "CustomSymbol::GetTextAngleAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetTextAngleAtIndex.htm"
---

# CustomSymbol::GetTextAngleAtIndex

This method is obsolete and has been superseded by [Note::GetTextAngleAtIndex](sldworksAPI.chm::/Note/Note__GetTextAngleAtIndex.htm).

Description

This method gets the text angle for the specified piece of text in this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetTextAngleAtIndex ( index )

| Input: | (long) index | Index of the text where the index begins at zero |
| --- | --- | --- |
| Return: | (double) retval | Text angle for the specified piece of text in radians, measured CCW from the X-axis |

Syntax (COM)

status = CustomSymbol->GetTextAngleAtIndex ( index, &retval )

| Input: | (long) index | Index of the text where the index begins at zero |
| --- | --- | --- |
| Output: | (double) retval | Text angle for the specified piece of text in radians, measured CCW from the X-axis |
| Return: | (HRESULT) status | S_OK if successful |
