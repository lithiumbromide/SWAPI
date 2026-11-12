---
title: "Component2::EnumBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__EnumBodies.htm"
---

# Component2::EnumBodies

This method is obsolete and has been superseded by [Component2::EnumBodies2](sldworksAPI.chm::/Component2/Component2__EnumBodies2.htm).

Description

This method gets the bodies in the component in a multibody part.

Syntax (OLE Automation)

enumBodies = Component2.EnumBodies ( bodyType )

| Input: | (long) bodyType | Type of body as defined by swBodyType_e |
| --- | --- | --- |
| Output: | (LPENUMBODIES2) enumBodies | Pointer to list of bodies |

Syntax (COM)

status = Component2->EnumBodies ( bodyType, &enumBodies )

| Input: | (long) bodyType | Type of body as defined by swBodyType_e |
| --- | --- | --- |
| Output: | (LPENUMBODIES2) enumBodies | Pointer to list of bodies |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method only supports solid and sheet body types.
