---
title: "EnumFaces::Next"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/EnumFaces/EnumFaces__Next.htm"
---

# EnumFaces::Next

This method is obsolete and has been superseded by [EnumFaces2::Next](sldworksAPI.chm::/EnumFaces2/EnumFaces2__Next.htm).

Description

This method gets the next face.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = EnumFaces->Next ( celt, rgelt, &pceltFetched )

| Input: | (long) celt | Number of faces desired for the enumerated list |
| --- | --- | --- |
| Output: | (LPFACE)* rgelt | Pointer to the list of face |
| Output: | (long) pceltFetched | Pointer to the number of faces returned from the list; this value can be less than celt if you ask for more faces than exist, or it can be NULL if no more faces exist |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
