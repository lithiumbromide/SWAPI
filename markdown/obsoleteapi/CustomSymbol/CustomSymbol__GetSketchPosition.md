---
title: "CustomSymbol::GetSketchPosition"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetSketchPosition.htm"
---

# CustomSymbol::GetSketchPosition

This method is obsolete and was not superseded .

Description

This method gets the position of the custom symbol sketch.

Syntax (OLE Automation)

retval = CustomSymbol.GetSketchPosition ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles (see below) |
| --- | --- | --- |

Syntax (COM)

status = CustomSymbol->IGetSketchPosition ( &retval )

| Output: | (double*) retval | Pointer to an array of doubles (see below) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[ textPtX, textPtY, textPtZ ]

where these sketch position values are actually offset values from the origin of this custom symbol object.
