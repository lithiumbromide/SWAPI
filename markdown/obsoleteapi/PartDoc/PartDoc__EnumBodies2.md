---
title: "PartDoc::EnumBodies2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__EnumBodies2.htm"
---

# PartDoc::EnumBodies2

This method is obsolete and has been superseded by [PartDoc::EnumBodies3](sldworksAPI.chm::/PartDoc/PartDoc__EnumBodies3.htm).

Description

This method enumerates the bodies in a part.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = PartDoc->EnumBodies2 ( bodyType, &retval )

| Input: | (long) bodyType | Type of body to obtain as defined in swBodyType_e |
| --- | --- | --- |
| Output: | (LPENUMBODIES2) retval | Pointer to the EnumBodies2 object containing the list of bodies |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
