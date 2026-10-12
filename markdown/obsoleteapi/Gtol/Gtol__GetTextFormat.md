---
title: "Gtol::GetTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Gtol/Gtol__GetTextFormat.htm"
---

# Gtol::GetTextFormat

This method is obsolete and has been superseded by [Annotation::GetTextFormat](sldworksAPI.chm::/Annotation/Annotation__GetTextFormat.htm).

Description

This method gets the TextFormat object for the Gtol.

Syntax (OLE Automation)

retval = Gtol.GetTextFormat ( )

| Return: | (LPDISPATCH) retval | Dispatch object for the TextFormat object |
| --- | --- | --- |

Syntax (COM)

status = Gtol->IGetTextFormat ( &retval )

| Output: | (LPTEXTFORMAT) retval | Pointer to the TextFormat object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

This method returns the text formatting object for the Gtol. To modify the formatting, change the properties, then call Gtol::SetTextFormat.
