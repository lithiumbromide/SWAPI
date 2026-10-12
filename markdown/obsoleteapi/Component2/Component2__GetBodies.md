---
title: "Component2::GetBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__GetBodies.htm"
---

# Component2::GetBodies

This method is obsolete and has been superseded by [Component2::GetBodies2](sldworksAPI.chm::/Component2/Component2__GetBodies2.htm).

Description

This method gets the bodies in the component in a multibody environment.

Syntax (OLE Automation)

bodiesVar = Component2.GetBodies ( bodyType)

| Input: | (long) bodyType | Type of body as defined by swBodyType_e |
| --- | --- | --- |
| Output: | (VARIANT) bodiesVar | Array of all of the bodies in the component |

Syntax (COM)

status = Component2->GetBodies ( bodyType, &bodiesVar )

| Input: | (long) bodyType | Type of body as defined by swBodyType_e |
| --- | --- | --- |
| Output: | (VARIANT) bodiesVar | Array of all of the bodies in the component |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method only supports solid and sheet body types.
