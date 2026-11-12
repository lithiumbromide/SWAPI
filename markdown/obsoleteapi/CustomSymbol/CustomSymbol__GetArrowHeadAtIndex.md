---
title: "CustomSymbol::GetArrowHeadAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetArrowHeadAtIndex.htm"
---

# CustomSymbol::GetArrowHeadAtIndex

This method is obsolete and has been superseded by [Note::GetArrowHeadAtIndex](sldworksAPI.chm::/Note/Note__GetArrowHeadAtIndex.htm).

Description

This method gets information on the specified arrow head in this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetArrowHeadAtIndex ( index)

| Input: | (long) index | Index of the desired arrow head where the index begins at zero |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles |

Syntax (COM)

status = CustomSymbol->IGetArrowHeadAtIndex ( index, retval )

| Input: | (long) index | Index of the desired arrow head where the index begins at zero |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is an array of doubles in the following format:

[ arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle ]

| arrowHeadPt [3] | XYZ arrow head tip location |
| --- | --- |
| arrowHeadDir [3] | XYZ arrow head direction |
| arrowHeadWidth | Arrow head width where the width is measured along the arrow head direction |
| arrowHeadHeight | Arrow head height |
| arrowHeadStyle | Arrow head style as defined in swArrowStyle_e |
