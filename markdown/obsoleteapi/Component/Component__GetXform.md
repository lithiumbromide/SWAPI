---
title: "Component::GetXform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetXform.htm"
---

# Component::GetXform

This method is obsolete and has been superseded by [Component2::GetXform](../Component2/Component2__GetXform.htm).

Description

This method gets the transform of this Component object. The transform is returned in relation of the root component (see Configuration::GetRootComponent).

Syntax (OLE Automation)

retval = Component.GetXform ()

| Return: | (VARIANT) retval | VARIANT containing a SafeArray of 16 doubles |
| --- | --- | --- |

Syntax (COM)

status = Component->IGetXform ( retval )

| Output: | (double*) retval | Pointer to an array of 16 doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If this configuration is exploded, then this method returns an exploded transform.

This method returns the transform as an array of 16 elements. The first 9 are elements of a standard 3x3 rotation matrix, the next 3 define translation, the next 1 is scaling. The last 3 elements are unused.

The transform is returned in relation to the root component.
