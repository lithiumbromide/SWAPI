---
title: "CustomSymbol::GetTriangleAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetTriangleAtIndex.htm"
---

# CustomSymbol::GetTriangleAtIndex

This method is obsolete and has been superseded by [Note::GetTriangleAtIndex](sldworksAPI.chm::/Note/Note__GetTriangleAtIndex.htm).

Description

This method gets the triangle at the specified index.

Syntax (OLE Automation)

retval = CustomSymbol.GetTriangleAtIndex ( index)

| Input: | (long) index | Index of the triangle where the index begins at zero |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles (see below) |

Syntax (COM)

status = CustomSymbol->IGetTriangleAtIndex ( index, retval )

| Input: | (long) index | Index of the triangle where the index begins at zero |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles (see below) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[ vertexPt1[3], vertexPt2[3], vertexPt3[3], isFilled, lineType ]

| vertexPt1 [3] | First XYZ vertex point |
| --- | --- |
| vertexPt2 [3] | Second XYZ vertex point |
| vertexPt3 [3] | Third XYZ vertex point |
| isFilled | Boolean returned as a double and is TRUE if the triangle is filled, FALSE otherwise |
| lineType | Line type as defined in swLineTypes_e |
