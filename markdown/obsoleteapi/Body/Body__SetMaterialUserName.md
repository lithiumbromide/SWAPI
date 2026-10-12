---
title: "Body::SetMaterialUserName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__SetMaterialUserName.htm"
---

# Body::SetMaterialUserName

This method is obsolete and has been superseded by [Body2::SetMaterialUserName](../Body2/Body2__SetMaterialUserName.htm).

Description

This method sets the material user name for this body. This material name is visible to the user.

Syntax (OLE Automation)

retval = Body.SetMaterialUserName ( name)

| Input: | (BSTR) name | Material's user name property for this body |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the material user name was set successfully, FALSE if it was not |

Syntax (COM)

status = Body->SetMaterialUserName ( name, &retval )

| Input: | (BSTR) name | Material's user name property for this body |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the material user name was set successfully, FALSE if it was not |
| Return: | (HRESULT)status | S_OK if successful |
