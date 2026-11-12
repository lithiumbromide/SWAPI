---
title: "PartDoc::EnumRelatedBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__EnumRelatedBodies.htm"
---

# PartDoc::EnumRelatedBodies

This method is obsolete and has been superseded by [PartDoc::EnumRelatedBodies2](sldworksAPI.chm::/PartDoc/PartDoc__EnumRelatedBodies2.htm).

Description

This method creates an enumerated list of bodies. The list contains only those bodies associated with reference surfaces. What results is a list of bodies that is related to the model, but it does not include the part body itself.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = PartDoc->EnumRelatedBodies ( &retval )

| Output: | (LPENUMBODIES) retval | Pointer to the enumerated list of bodies |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

A Reference surface feature can consist of one or more surfaces knitted together.

Each reference surface feature has two Body objects:

- One to represent the front faces
- one to represent the back faces

Each Body object has one or more faces depending on whether the reference surface feature is a set of knitted surfaces or a single underlying surface. The corresponding faces for each body pair should have normal vectors that are opposite.

To use the enumerated list, see the EnumBodies object.
