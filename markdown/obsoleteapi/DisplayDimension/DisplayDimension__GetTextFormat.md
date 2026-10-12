---
title: "DisplayDimension::GetTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetTextFormat.htm"
---

# DisplayDimension::GetTextFormat

This method is obsolete and has been superseded by [Annotation::GetTextFormat](sldworksAPI.chm::/Annotation/Annotation__GetTextFormat.htm).

Description

This method gets the TextFormat object for this display dimension.

Syntax (OLE Automation)

retval = DisplayDimension.GetTextFormat ( )

| Return: | (LPDISPATCH) retval | Dispatch object for the TextFormat object |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->IGetTextFormat ( &retval )

| Output: | (LPTEXTFORMAT) retval | Pointer to the TextFormat object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

To modify the formatting, change the properties and call DisplayDimension::SetTextFormat to implement your changes.
