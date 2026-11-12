---
title: "Component::SetMaterialUserName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__SetMaterialUserName.htm"
---

# Component::SetMaterialUserName

This method is obsolete and has been superseded by [Component2::SetMaterialUserNam](sldworksAPI.chm::/Component2/Component2__SetMaterialUserName.htm)e.

Description

This method sets the material user name for this component. The value is visible to the user.

Syntax (OLE Automation)

retval = Component.SetMaterialUserName ( name)

| Input: | (BSTR) name | Material user name property for this component |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the material user name was set successfully, FALSE if not |

Syntax (COM)

status = Component->SetMaterialUserName ( name, &retval )

| Input: | (BSTR) name | Material user name property for this component |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the material user name was set successfully, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
