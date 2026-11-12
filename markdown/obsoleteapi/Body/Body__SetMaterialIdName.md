---
title: "Body::SetMaterialIdName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__SetMaterialIdName.htm"
---

# Body::SetMaterialIdName

This method is obsolete and has been superseded by [Body2::SetMaterialIdName](../Body2/Body2__SetMaterialIdName.htm).

Description

This method sets the material ID for this body. This value is not visible to the user.

Syntax (OLE Automation)

retval = Body.SetMaterialIdName ( name)

| Input: | (BSTR) name | Material's ID name for this body |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the material ID name is set successfully, FALSE if not |

Syntax (COM)

status = Body->SetMaterialIdName ( name, &retval )

| Input: | (BSTR) name | Material's ID name for this body |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the material ID name is set successfully, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
