---
title: "Component2::GetXform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__GetXform.htm"
---

# Component2::GetXform

This method is obsolete and has been superseded by [Component2::Transform](Component2__Transform.htm) .

Description

This method gets the transform of this component object.

Syntax (OLE Automation)

retval = Component2.GetXform ()

| Return: | (VARIANT) retval | VARIANT containing a SafeArray of 16 doubles |
| --- | --- | --- |

Syntax (COM)

status = Component2->IGetXform ( retval )

| Output: | (double*) retval | Pointer to an array of 16 doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If the current configuration is exploded, then SolidWorks returns the exploded transform, which is an array of 16 elements. The first 9 are elements of a standard 3x3 rotation matrix, the next 3 define translation, the next 1 is scaling, and the last 3 elements are unused.

SolidWorks returns the transform in relation to the root component. See Configuration::GetRootComponent for more information.
