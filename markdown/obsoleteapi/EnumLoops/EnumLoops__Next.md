---
title: "EnumLoops::Next"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/EnumLoops/EnumLoops__Next.htm"
---

# EnumLoops::Next

This method is obsolete and has been superseded by [EnumLoops2::Next](sldworksAPI.chm::/EnumLoops2/EnumLoops2__Next.htm).

Description

This method gets the next loop.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = EnumLoops->Next ( celt, &rgelt, &celtFetched )

| Input: | (long) celt | Number of loops desired for the enumerated list |
| --- | --- | --- |
| Output: | (LPLOOP) rgelt | Pointer to the enumerated list of loops |
| Output: | (long) celtFetched | Pointer to the number of loops returned from the list; this value can be less than celt if you ask for more loops than exist, or it can be NULL if no more loops exist |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
