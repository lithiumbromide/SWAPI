---
title: "Component::EnumRelatedBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__EnumRelatedBodies.htm"
---

# Component::EnumRelatedBodies

This method is obsolete and has been superseded by [Component2::EnumRelatedBodies](sldworksAPI.chm::/Component2/Component2__EnumRelatedBodies.htm).

Description

This method creates an enumerated list of bodies. The list contains only those bodies associated with reference surfaces. The list of bodies is related to the model, but it does not include the part body itself.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Component->EnumRelatedBodies ( &retval )

| Output: | (LPENUMBODIES*) retval | Pointer to the enumerated list of bodies |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

A reference surface feature might consist of one or more surfaces sewn together. SolidWorks represents each reference surface feature with two body objects; one to represent the front faces and one to represent the back faces. Each body object has 1 or more faces depending on whether the reference surface feature is a set of sewn surfaces or a single underlying surface. The corresponding faces for each body pair have opposite normal vectors.

To use the enumerated list, use EnumBodies2::Next, EnumBodies2::Skip, EnumBodies2::Reset, and EnumBodies2::Clone.

If a component is suppressed or lightweight, this method might return NULL because the component has not been loaded into memory by SolidWorks. For more information on lightweight components, refer to Working With Lightweight Components.
