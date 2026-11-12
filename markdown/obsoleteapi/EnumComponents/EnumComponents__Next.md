---
title: "EnumComponents::Next"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/EnumComponents/EnumComponents__Next.htm"
---

# EnumComponents::Next

This method is obsolete and has been superseded by [EnumComponents2::Next](sldworksAPI.chm::/EnumComponents2/EnumComponents2__Next.htm).

Description

This method gets the next component.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = EnumComponents->Next ( celt, rgelt, &pceltFetched )

| Input: | (long) celt | Number of component objects desired for the enumerated list |
| --- | --- | --- |
| Output: | (LPCOMPONENT)* rgelt | Pointer to an array of size celt of component objects |
| Output: | (long) pceltFetched | Pointer to the number of component objects returned from the list; this value can be less than celt if you ask for more component objects than exist, or it can be NULL if no more component objects exist |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
