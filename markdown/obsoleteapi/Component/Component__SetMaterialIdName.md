---
title: "Component::SetMaterialIdName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__SetMaterialIdName.htm"
---

# Component::SetMaterialIdName

This method is obsolete and has been superseded by [Component2::SetMaterialIdName](sldworksAPI.chm::/Component2/Component2__SetMaterialIdName.htm).

Description

This method sets the material ID for this component.

Syntax (OLE Automation)

retval = Component.SetMaterialIdName ( name )

| Input: | (BSTR) name | Material ID name for this component |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the material ID name was set successfully, FALSE if it was not |

Syntax (COM)

status = Component->SetMaterialIdName ( name, &retval )

| Input: | (BSTR) name | Material ID name for this component |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the material ID name was set successfully, FALSE if it was not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This value is not visible to the user.
