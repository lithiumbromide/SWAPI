---
title: "Component2::RemoveMaterialProperty"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__RemoveMaterialProperty.htm"
---

# Component2::RemoveMaterialProperty

This method is obsolete and has been superseded by [Component2::RemoveMaterialProperty2](sldworksAPI.chm::/Component2/Component2__RemoveMaterialProperty2.htm).

Description

This method removes material property values from the component.

Syntax (OLE Automation)

retval = Component2.RemoveMaterialProperty ( )

| Return: | (BOOL) retval | TRUE if the material property was removed, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = Component2->RemoveMaterialProperty ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the material property was removed, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) retval | S_OK if successful |

Remarks

This method is intended to be used on components whose material property value has changed; for example, color.
