---
title: "PartDoc::EnumBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__EnumBodies.htm"
---

# PartDoc::EnumBodies

This method is obsolete and has been superseded by [PartDoc::IEnumBodies2](PartDoc__EnumBodies2.htm).

Description

This method enumerates the bodies in a part

Syntax (OLE Automation)

Not Available.

Syntax (COM)

status = PartDoc->EnumBodies ( bodyType, &retval )

| Input: | (long) bodyType | Type of body to obtain as defined in swBodyType_e |
| --- | --- | --- |
| Output: | (LPENUMBODIES) retval | Pointer to the EnumBodies object containing the list of bodies |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Only solid and sheet body types are supported. If swSolidBody is used, only one solid is returned for this part; if swSheetBody is used, all the sheet bodies for the part are returned.
