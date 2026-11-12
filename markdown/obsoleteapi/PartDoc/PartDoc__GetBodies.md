---
title: "PartDoc::GetBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__GetBodies.htm"
---

# PartDoc::GetBodies

This method is obsolete and has been superseded by [PartDoc::GetBodies2](sldworksAPI.chm::/PartDoc/PartDoc__GetBodies2.htm).

Description

This method gets all of the bodies in a part.

Syntax (OLE Automation)

bodies = PartDoc.GetBodies ( bodyType )

| Input: | ( long ) bodyType | Type of bodies to obtain as defined in swBodyType_e |
| --- | --- | --- |
| Return: | (VARIANT) bodies | VARIANT of type SafeArray of Dispatch pointers to the bodies |

Syntax (COM)

status = PartDoc->GetBodies ( bodyType, &bodies )

| Input: | ( long ) bodyType | Type of bodies to obtain as defined in swBodyType_e |
| --- | --- | --- |
| Output: | (VARIANT) bodies | VARIANT of type SafeArray of Dispatch pointers to the bodies |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Only solid and sheet body types are supported. If swSolidBody is used, only one solid is returned for this part; if swSheetBody is used, all the sheet bodies for the part are returned.
